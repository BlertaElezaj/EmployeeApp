# EmployeeApp

**EmployeeApp** is a Python application built using Kivy and KivyMD. It provides a login interface and a dynamic two-panel layout for managing user roles and features. The app allows users to log in, navigate between different user features, and sign out.

## Features

- **Login Screen**: Users enter their username and password to authenticate.
- **Role-based Navigation**: Depending on the user role, different feature buttons are displayed in the navigation panel.
- **Dynamic Content Panel**: The content panel updates based on the selected feature from the navigation panel.
- **Sign Out**: Users can log out, which closes the app.

## Technologies

- **Python**: The main programming language for the application.
- **Kivy**: A Python library for building multi-touch applications.
- **KivyMD**: Material Design components for Kivy.
- **LoginController**: A custom controller for handling login and authentication logic.
- **AuthorizationService**: Manages user features based on roles.
