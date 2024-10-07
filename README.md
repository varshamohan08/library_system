## library_system
This Django project provides a simple API to manage a bookstore's collection of books. It includes CRUD operations for books, with validations on ISBN and price. Pagination is implemented for the list view.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **CRUD Operations**: Create, Read, Update, and Delete books in the bookstore.
- **Validations**: 
  - ISBN must be exactly 13 characters.
  - Price must be a positive value.
- **Pagination**: Supports pagination for listing books with the option to specify page size.
- **Transaction Management**: Ensures that data changes are atomic and rolled back if any error occurs.
- **Filter by Title/Author**: Option to filter books by title and/or author.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/varshamohan08/library_system.git
   ```
2. Navigate to the project directory:
   ```
   cd library_system
   ```
3. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required packages
   ```
   pip install -r requirements.txt
   ```
5. Apply database migrations:
   ```
   python manage.py migrate
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage
- To get a list of all books, you can make a GET request to /api/books/.
- Filter the books using the query parameters title and/or author, eg. /api/books?title={title}&author={author}/.
- To create a new book, send a POST request to /api/books/ with the required book details.
- Update book details by sending a PUT request to /api/books/{id}/.
- To delete a book, send a DELETE request to /api/books/{id}/.
