# URL Shortener API

A simple and efficient RESTful URL shortening service built with Django and Django REST Framework. 
Developed as Task 1 for the CodeAlpha Backend Development Internship.

## Features

- **Short Link Generation:** Creates a unique 6-character code for any valid URL.
- **Redirection:** Handles HTTP 302 redirects from the short code to the original destination.
- **Analytics Tracking:** Safely tracks click counts using Django's `F()` expressions to ensure atomic database updates and prevent race conditions.
- **Validation:** Enforces strict URL validation logic at the serializer level.

## Tech Stack

- Python 3.12
- Django 6.1.1
- Django REST Framework 3.18.1
- SQLite

## API Endpoints

- `POST /api/shorten/`
  - Payload: `{"original_url": "https://example.com"}`
  - Returns: JSON object with the generated short code and metadata.

- `GET /<short_code>/`
  - Returns: 302 Redirect to the original URL.

- `GET /api/analytics/<short_code>/`
  - Returns: JSON object containing total clicks and creation date.

## Local Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/ahmed-morsi-ai/CodeAlpha_URLShortener.git](https://github.com/ahmed-morsi-ai/CodeAlpha_URLShortener.git)
   cd CodeAlpha_URLShortener