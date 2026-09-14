\# Enterprise URL Shortener API



A high-performance, lightweight RESTful URL Shortener service built with Python 3.12, Django 6.1, and Django REST Framework (DRF). Designed with robust input validation, thread-safe analytics counter, and built-in redirection logic.



Developed as part of the \*\*CodeAlpha Backend Development Internship\*\* (Task 1).



\---



\## 🏗️ Architecture \& Key Features



\* \*\*Short Code Generation\*\*: Generates unique, compact short keys for submitted long URLs.

\* \*\*Atomic Analytics Counter\*\*: Uses Django `F()` expressions to increment click counts at the database level, preventing race conditions during concurrent redirects.

\* \*\*URL Sanitization \& Validation\*\*: Enforces strict URL validation logic to prevent invalid formats and malicious redirects (SSRF mitigation).

\* \*\*RESTful Endpoints\*\*: Built using DRF views for clean separation of request validation, processing, and response generation.

\* \*\*Embedded Test Suite\*\*: Covered by automated Django unit tests validating creation, lookup, redirect HTTP status codes, and non-existent code handling (404).



\---



\## 🛠️ Tech Stack



\* \*\*Language\*\*: Python 3.12

\* \*\*Framework\*\*: Django 6.1.1

\* \*\*API Framework\*\*: Django REST Framework 3.18.1

\* \*\*Database\*\*: SQLite

\* \*\*Tooling\*\*: Git, PowerShell, Django Test Suite



\---



\## 🚀 API Endpoints



| Method | Endpoint | Description | Sample Payload / Query |

| :--- | :--- | :--- | :--- |

| `POST` | `/api/shorten/` | Generates a short code for a long URL | `{"original\_url": "https://example.com/very/long/path"}` |

| `GET` | `/<short\_code>/` | Redirects (`302 Found`) to the original long URL | N/A |

| `GET` | `/api/analytics/<short\_code>/` | Returns URL statistics \& click count | N/A |



\---



\## 💻 Local Setup \& Installation



1\. \*\*Clone the Repository\*\*:

&#x20;  ```bash

&#x20;  git clone \[https://github.com/ahmed-morsi-ai/CodeAlpha\_URLShortener.git](https://github.com/ahmed-morsi-ai/CodeAlpha\_URLShortener.git)

&#x20;  cd CodeAlpha\_URLShortener

