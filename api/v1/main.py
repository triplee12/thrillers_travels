#!/usr/bin/env python3
"""Technical Assessment: Building a Flight Search API."""

from typing import Dict
import requests
from fastapi import FastAPI, HTTPException, status
from api.v1.settings import settings

FLIGHT_API_URL: str = settings.FLIGHT_API_URL

HEADERS: Dict[str, str] = {
    "X-RapidAPI-Key": settings.X_RapidAPI_Key,
    "X-RapidAPI-Host": settings.X_RapidAPI_Host
}

app = FastAPI(
    title="Technical Assessment: Building a Flight Search API",
    description="Building a Flight Search API.",
    version="0.1.0"
)


@app.get("/api/v1/search/", tags=["search"], status_code=200)
async def search(query: str, limit: str = 10) -> Dict:
    """
    Search for a flight and returns relevant flight data.

    Methods:
        GET /api/v1/search/?query=<query>&limit=<limit>
        query *(REQUIRED): A string parameter specifying the query to search
        limit (OPTIONAL): A string parameter specifying the limit of the result
    Args:
        query (str): The query to search
            (e.g., departure airport, arrival airport, date)
        limit (str): The limit of results to return
    Returns:
        dict: returns relevant flight data
    """
    if query and limit:
        querystring: Dict[str, str] = {"query": query, "limit": limit}
        try:
            response = requests.get(
                FLIGHT_API_URL,
                headers=HEADERS,
                params=querystring,
                timeout=3
            )
            if len(response.json()['results']) > 0:
                return response.json()
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No results found"
            )
        except requests.exceptions.Timeout as time_out:
            raise HTTPException(
                status_code=status.HTTP_408_REQUEST_TIMEOUT,
                detail="Request timed out. Try again later."
            ) from time_out
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail="Unprocessable Entity. Make sure you use 'query' parameter."
    )
