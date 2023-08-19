#!/usr/bin/env python3
"""Test file for main module."""

from typing import Dict
import requests


def test_search_valid() -> None:
    """Test for valid search query."""
    parameter: Dict[str, str] = {"query": "FD3210", "limit": "25"}
    query = requests.get(
        url="http://127.0.0.1:8000/api/v1/search/",
        params=parameter,
        timeout=3
    )
    assert query.status_code == 200


def test_search_invalid() -> None:
    """Test for invalid search query."""
    parameter: Dict[str, str] = {"q": "FD3210"}
    query = requests.get(
        url="http://127.0.0.1:8000/api/v1/search/",
        params=parameter,
        timeout=3
    )
    assert query.status_code == 422


def test_search_without_limit() -> None:
    """Test for search query without limit parameter."""
    parameter: Dict[str, str] = {"query": "FD3210"}
    query = requests.get(
        url="http://127.0.0.1:8000/api/v1/search/",
        params=parameter,
        timeout=3
    )
    assert query.status_code == 200


def test_search_with_limit() -> None:
    """Test for search query with limit parameter."""
    parameter: Dict[str, str] = {"query": "FD3210", "limit": "10"}
    query = requests.get(
        url="http://127.0.0.1:8000/api/v1/search/",
        params=parameter,
        timeout=3
    )
    assert query.status_code == 200


def test_search_not_found_response() -> None:
    """Test for search query not found response."""
    parameter: Dict[str, str] = {"query": "1", "limit": "25"}
    query = requests.get(
        url="http://127.0.0.1:8000/api/v1/search/",
        params=parameter,
        timeout=3
    )
    msg: Dict[str, str] = {"detail": "No results found"}
    assert query.status_code == 404
    assert query.json() == msg
