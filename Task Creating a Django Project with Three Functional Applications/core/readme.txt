# Django Project with Three Functional Applications

This project is a Django-based web application that includes three functional applications: `myapp`, `myapp1`, and `myapp2`. Each application serves different purposes and provides various functionalities.

## Project Structure

- `core/`: Contains the main project settings and configurations.
  - `asgi.py`: ASGI configuration.
  - `settings.py`: Project settings.
  - `urls.py`: URL routing for the project.
  - `wsgi.py`: WSGI configuration.
- `myapp/`: First application with basic functionalities.
  - `admin.py`: Admin site registration.
  - `apps.py`: Application configuration.
  - `models.py`: Database models.
  - `myapp_urls.py`: URL routing for `myapp`.
  - `views.py`: View functions for `myapp`.
- `myapp1/`: Second application with additional functionalities.
  - `admin.py`: Admin site registration.
  - `apps.py`: Application configuration.
  - `models.py`: Database models.
  - `myapp1_urls.py`: URL routing for `myapp1`.
  - `views.py`: View functions for `myapp1`.
- `myapp2/`: Third application with more functionalities.
  - `admin.py`: Admin site registration.
  - `apps.py`: Application configuration.
  - `models.py`: Database models.
  - `myapp2urls.py`: URL routing for `myapp2`.
  - `views.py`: View functions for `myapp2`.

## Functionalities

### `myapp`
- `dashboard`: Displays the dashboard.
- `profile`: Displays the profile page.
- `settings`: Displays the settings page.
- `notifications`: Displays notifications.
- `logout`: Logs out the user.

### `myapp1`
- `home`: Displays the home page.
- `user`: Displays the user page.
- `shubham`: Displays a personalized page for the user.
- `shubham_login`: Displays the login page for the user.
- `user2`: Displays the second user page.
- `onkar`: Displays a personalized page for the second user.
- `onkar_login`: Displays the login page for the second user.

### `myapp2`
- `main_page`: Displays the main page.
- `about_us`: Displays the about us page.
- `contact_us`: Displays the contact us page.
- `services`: Displays the services page.
- `faq`: Displays the FAQ page.

## How to Run

1. Install the required dependencies:
   ```sh
   pip install -r requirements.txt