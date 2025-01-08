# DjangoAuthSystem

## Project Description

**DjangoAuthSystem** is a comprehensive authentication system built using Django and JWT (JSON Web Tokens). This project implements a robust and secure authentication mechanism including user login, registration, refresh token functionality, and access control to a user-specific dashboard.

## Features

- **Login**: 
  - Users can log in with their credentials and receive a JWT token for session management.
  
- **Registration**: 
  - New users can create an account with unique credentials. 
  - Passwords are stored securely using Django's built-in password hashing mechanisms.
  
- **Token Refresh**: 
  - A refresh token mechanism is implemented to allow users to obtain new access tokens without re-entering their credentials.
  
- **Dashboard Access**: 
  - Access to the user-specific dashboard is restricted to authenticated users only.
  - Middleware ensures token validity on protected routes.

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/RofixWork/Secure_django-auth_system.git
```    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    - Open your web browser and go to `http://localhost:8000`.

## API Endpoints

- **User Registration:**
    ```
    POST /api/auth/register/
    ```
    - Request Body: `{ "username": "", "email": "", "password": ", "passwrod2: "" }`

- **User Login:**
    ```
    POST /api/auth/login/
    ```
    - Request Body: `{ "username": "", "password": "" }`

- **Token Refresh:**
    ```
    POST /api/auth/token/refresh/
    ```
    - Request Body: `{ "refresh": "" }`

- **Access Dashboard:**
    ```
    GET /api/dashboard/
    ```
    - Requires a valid JWT token in the request headers.

## Technologies Used

- Django
- Django REST Framework
- djangorestframework-simplejwt
- bcrypt

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

If you have any questions or suggestions, feel free to reach out at [wourkout123@gmail.com].
