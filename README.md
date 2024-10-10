# Library Management API

This project is a Django RESTful API for managing books and authors, with user authentication (JWT), search functionality, and a recommendation system for users' favorite books.

## Features

- **Books API**:
  - Retrieve a list of all books (`GET /books`)
  - Retrieve a specific book by ID (`GET /books/:id`)
  - Create a new book (protected, `POST /books`)
  - Update an existing book (protected, `PUT /books/:id`)
  - Delete a book (protected, `DELETE /books/:id`)
  
- **Authors API**:
  - Retrieve a list of all authors (`GET /authors`)
  - Retrieve a specific author by ID (`GET /authors/:id`)
  - Create a new author (protected, `POST /authors`)
  - Update an existing author (protected, `PUT /authors/:id`)
  - Delete an author (protected, `DELETE /authors/:id`)

- **User Authentication**:
  - JWT-based authentication
  - Register a new user (`POST /register`)
  - Login to receive tokens (`POST /login`)

- **Search Functionality**:
  - Search for books by title or author name (`GET /books?search=query`)

- **Recommendation System**:
  - Users can mark books as favorites.
  - The system suggests up to 5 recommended books based on a user's favorites.
  - A user can have a maximum of 20 favorite books.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or later
- Django REST Framework
- PostgreSQL (or any other supported database)
- DRF-yasg for API documentation
- Simple JWT for authentication

### Installation

1. **Clone the Repository**:

    ```bash
    git clone
    cd library-api
    ```

2. **Create and Activate a Virtual Environment**:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**:
   - Update your `DATABASES` setting in `settings.py` to configure your database (e.g., PostgreSQL).
   - Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser (Optional)**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Server**:

    ```bash
    python manage.py runserver
    ```

### API Endpoints

- **Books**:
  - `GET /books` - Retrieve all books.
  - `GET /books/:id` - Retrieve a specific book by ID.
  - `POST /books` - Create a new book (JWT protected).
  - `PUT /books/:id` - Update an existing book (JWT protected).
  - `DELETE /books/:id` - Delete a book (JWT protected).

- **Authors**:
  - `GET /authors` - Retrieve all authors.
  - `GET /authors/:id` - Retrieve a specific author by ID.
  - `POST /authors` - Create a new author (JWT protected).
  - `PUT /authors/:id` - Update an existing author (JWT protected).
  - `DELETE /authors/:id` - Delete an author (JWT protected).

- **User Authentication**:
  - `POST /register` - Register a new user.
  - `POST /login` - Login and receive JWT tokens.

- **Favorites & Recommendations**:
  - `POST /favorites` - Add a book to the user's favorites list (JWT protected).
  - `GET /favorites/recommendations` - Get book recommendations based on favorites.

### Search Functionality

To search for books by title or author name:

```bash
GET /books?search=search_term
```

### Swagger Documentation

You can access the interactive API documentation via Swagger UI at:

```bash
http://localhost:8000/swagger/
```

### Running Tests

To run tests for the project, use:

```bash
python manage.py test
```

### Response Time Testing

You can test the response time of any endpoint using tools like Postman or cURL.

## Code Structure

```
library/
│
├── books/                # Book app (models, views, serializers, etc.)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── library/              # Main project folder
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
│
└── manage.py             # Django management script
```

## Technologies Used

- **Django**: Web framework
- **Django REST Framework**: For building the RESTful API
- **PostgreSQL**: Database
- **Simple JWT**: For handling JWT authentication
- **Swagger UI**: For API documentation (via `drf-yasg`)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)


### Key Sections:
- **Features**: Lists API capabilities.
- **Getting Started**: Provides installation and setup instructions.
- **API Endpoints**: Documents each API endpoint clearly.
- **Search Functionality & Swagger**: Explains search and Swagger UI.
- **Technologies Used**: Lists the key technologies used.
- **Code Structure**: Provides an overview of the folder structure.
- **Contributing**: Welcomes contributions.

Feel free to adjust the specifics to match your project!