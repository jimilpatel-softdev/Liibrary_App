# Library Management System

This is a Django-based Library Management System API project. It allows users to manage books, members, and loans, including borrowing and returning books.

## Features
- Book Management: Add, update, delete, and search books by title, author, or genre.
- Member Management: Create and manage members who can borrow books.
- Loan System: Borrow books, check loan status, and return books.

## Prerequisites

Before setting up the project, ensure you have the following installed:
- Python 3.11 or higher
- PostgreSQL database
- pip (Python package manager)

## Setup Instructions

Follow the steps below to set up the project locally:

### 1. Clone the Repository
Clone this repository to your local machine:
```
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```
### 2: Create a Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
# venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```
### 3: Configure Database
```
1. Ensure you have PostgreSQL installed and running. Create a new database:
CREATE DATABASE library_system;

2. Update the database configuration in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_system',
        'USER': 'your-db-username',
        'PASSWORD': 'your-db-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

### 4: Create a Superuser
```
python manage.py createsuperuser
```
### 5: Run the Development Server
```
python manage.py runserver
```
The application should now be running at http://127.0.0.1:8000/.
You can access the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials you created earlier.

### API Endpoints
GET /api/books/: List all books.
POST /api/books/: Add a new book.
GET /api/books/{id}/: View a specific book's details.
POST /api/loans/{book_id}/borrow/: Borrow a book by book ID.
POST /api/loans/{loan_id}/return/: Return a borrowed book by loan ID.
GET /api/members/{id}/my_loans/: List all loans for a specific member.


