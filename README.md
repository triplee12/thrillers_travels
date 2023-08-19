# Thrillers Travels - Junior Backend Engineer Assessment

Building a Flight Search API

## Technical Assessment: Building a Flight Search API

In this assessment, your task is to create a Flight Search API using a freely available flight search API provider, such as Flight Radar on Rapid API, or any other suitable flight search API. Your solution should enable users to search for flight information based on specific parameters.

## Requirements

Make sure you have python3 installed in your machine before running commands below.

## Installation

To successfully run the flight search program, you need to install the required libraries in the requirements.txt file. To install the required libraries, create a virtual environment and run the following command

- Install the required libraries

  ``
  pip install -r requirements.txt
  ``

## Running

Run the following command in the command-line

- To navigate to the project directory

  ``
  cd thrillers_travels
  ``

- Run uvicorn command to start the project server

  ``
  uvicorn app.v1.main:app --reload
  ``

To stop the project server press ``Ctrl`` + ``C`` or ``command`` + ``C`` depending on your machine.

### Test

To run the tests, make sure you have started the server.

- Run pytest command in the same directory in the command-line

  ``
  pytest -vv tests
  ``

## API Documentation

Search API documentation

### API Route

- GET ```http://127.0.0.1:8000/api/v1/search/?query=FD3210&limit=10```:
  - Description: Query for a flight data.
  - Method: GET
  - Parameters:
    - ``query`` *(REQUIRED): A string parameter specifying the query to search.
    - ``limit`` (OPTIONAL): A string parameter specifying the limit of the result
  - Response: returns relevant flight data in json.

### Status Codes

- ``200``: Success
- ``404``: Not Found
- ``408``: Request Timeout
- ``422``: Unprocessable Entity

## AUTHOR

Ejie Emmanuel Chukwuebuka <tripleeoliver@gmail.com>
