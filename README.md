# Filmhouse API Documentation
Welcome to the Filmhouse API documentation! This API allows users to manage movie sales and rentals online.

### Table of Contents
Introduction
Getting Started
Authentication
Base URL
Endpoints
Movies
Users
Rentals
Sales
Admins
Request and Response Formats
Error Handling
#### Introduction
The Filmhouse API is designed to facilitate movie sales and rentals. Users can stream rented movies live for 72 hours, and if a movie is sold, they will have access to the download link.

#### Getting Started
Authentication
Authentication is required for certain endpoints. Include an API key in the request headers for authentication.

#### Base URL
All API endpoints are relative to the base URL:


https://api.filmhouse.com/v1
#### Endpoints
##### Movies
Get All Movies
Endpoint: /movies
Method: GET
Description: Get a list of all movies.
Get Movie by ID
Endpoint: /movies/{movie_id}
Method: GET
Description: Get details of a specific movie by its ID.
Rent Movie
Endpoint: /movies/{movie_id}/rent
Method: POST
Description: Rent a movie. Returns a streaming link for the rented movie.
Buy Movie
Endpoint: /movies/{movie_id}/buy
Method: POST
Description: Buy a movie. Returns a download link for the purchased movie.
##### Users
Get All Users
Endpoint: /users
Method: GET
Description: Get a list of all users.
Get User by ID
Endpoint: /users/{user_id}
Method: GET
Description: Get details of a specific user by their ID.
##### Rentals
Get All Rentals
Endpoint: /rentals
Method: GET
Description: Get a list of all rentals.
Get Rental by ID
Endpoint: /rentals/{rental_id}
Method: GET
Description: Get details of a specific rental by its ID.
##### Sales
Get All Sales
Endpoint: /sales
Method: GET
Description: Get a list of all sales.
Get Sale by ID
Endpoint: /sales/{sale_id}
Method: GET
Description: Get details of a specific sale by its ID.
##### Admins
Get All Admins
Endpoint: /admins
Method: GET
Description: Get a list of all administrators.
Get Admin by ID
Endpoint: /admins/{admin_id}
Method: GET
Description: Get details of a specific administrator by their ID.
#### Request and Response Formats
Request Format: JSON
Response Format: JSON
#### Error Handling
The API returns standard HTTP status codes and includes error details in the response body.







