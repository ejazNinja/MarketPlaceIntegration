# Marketplace Events Integration and Backend Service

This repository contains two applications for managing marketplace events data: a FastAPI application for integrating with marketplace APIs and a Django-based backend service for storing and querying events data.

## 1. FastAPI Application

The FastAPI application is responsible for:

- Polling marketplace events API periodically.
- Parsing and formatting event data.
- Making API calls to the backend service to save events in the database.

## 2. Django Backend Service

The Django backend service provides APIs for::

- Saving marketplace events data to the database.
- Client-facing APIs for querying events data.
- Serving the cached API response for better performance
- **[Client facing API Swagger](http://localhost:8000/swagger/)**

## Key Features

- **Efficient Data Fetching**: Dynamically fetches events based on start and end times through RESTful endpoints.
- **Caching**: Implements caching event data to speed up repeated requests.
- **Asynchronous Support**: Utilizes asynchronous programming paradigms across database and network operations to improve I/O efficiency.
- **Scalability**: Built to handle between 1,000 to 5,000 requests per minute, suitable for high-load environments.

## 🎯 Reason for Dividing the Project

We divided the project into two distinct sections for specific reasons:

- **Independent Polling Service:** The FastAPI application serves as a dedicated polling service for marketplace events. By separating this functionality, we ensure that the polling process can operate independently, allowing for scalability and flexibility in handling diverse marketplace APIs and data sources.

- **Robust Client-Facing Backend:** The Django backend service focuses on providing robust, scalable APIs for storing and querying events data. This separation ensures that client-facing applications can interact efficiently with our backend, leveraging Django's ORM capabilities for reliable data storage and retrieval.

## Technologies Used

- **Django**: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It provides built-in features like an ORM, admin interface, authentication, and routing.

- **Django REST Framework**: Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django. It provides serializers, authentication, pagination, and more.
- **FastAPI**: Modern, fast (high-performance), web framework for building APIs.
- **HTTPX**: Fully featured HTTP client for Python 3, which provides synchronous and asynchronous APIs.

## Project Structure

```plaintext

├── EventsMarketPlace/ # Django based client facing API app
│ ├── common/ # Implements common utility
│ │
│ ├── events/ # Implements events functionality
└── polling_app # Implements fastapi based polling app
└── README.md
└── requirements.txt
```

## Setup and Installation

### Prerequisites

- Python 3.8+

### Installation Steps

1. **Clone the repository**
2. **Install dependencies**

   ```bash
   pip install --user -r requirements.txt
   ```

3. **Configure the environment**

   Set django settings.py file as per usage

4. **Run the application**

   Start the django server first

   ```bash
   python EventsMarketPlace/manage.py runserver
   ```

   Start the FastAPI server

   ```bash
   python polling_app/main.py
   ```

## Usage

Access the API through the endpoint:

- **API Documentation**: Navigate to `http://localhost:8000/swagger` in your browser to view the Swagger UI which provides interactive documentation.
- **Django admin panel**: Navigate to `http://localhost:8000/admin` use credentials, username=admin and password=123

## Contributing

Contributions are welcome! Please fork the project and submit a pull request with your features or fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
