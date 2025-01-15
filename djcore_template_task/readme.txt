# Project Overview

In this project, I have set up a Django application to demonstrate the use of templates. The key tasks completed include:

1. **Project Setup**: Initialized a new Django project and configured the necessary settings.
2. **Application Creation**: Created a Django app within the project to handle template rendering.
3. **Template Creation**: Developed multiple HTML templates to render different views.
4. **Context Data**: Implemented views to pass dynamic context data to the templates.
5. **Template Inheritance**: Utilized Django's template inheritance feature to create a base template and extend it for other pages.
6. **Static Files Management**: Configured and managed static files such as CSS and JavaScript for the templates.
7. **URL Routing**: Set up URL routing to map URLs to the appropriate views and templates.

This project serves as a practical example of how to effectively use Django templates to create dynamic and reusable web pages.

# Steps to Render HTML Templates

## 1. Configure `settings.py`
Ensure the `TEMPLATES` setting is correctly configured to include the directory where your templates are stored.
```python
// filepath: /C:/Users/shubh/Projects/Django_tasks/djcore_template_task/settings.py
// ...existing code...
TEMPLATES = [
    {
        // ...existing code...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        // ...existing code...
    },
]
// ...existing code...
```

## 2. Create Views in `views.py`
Define views that render the HTML templates and pass context data if needed.
```python
// filepath: /C:/Users/shubh/Projects/Django_tasks/djcore_template_task/views.py
from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Home Page',
        'content': 'Welcome to the Home Page!'
    }
    return render(request, 'home.html', context)

def about_view(request):
    context = {
        'title': 'About Page',
        'content': 'Learn more about us on this page.'
    }
    return render(request, 'about.html', context)
```

## 3. Define URL Patterns in `urls.py`
Map URLs to the corresponding views.
```python
// filepath: /C:/Users/shubh/Projects/Django_tasks/djcore_template_task/urls.py
from django.contrib import admin
from django.urls import path
from .views import home_view, about_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
]
```

## 4. Create HTML Templates
Place your HTML templates in the `templates` directory.
```html
<!-- filepath: /C:/Users/shubh/Projects/Django_tasks/djcore_template_task/templates/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ content }}</h1>
</body>
</html>
```

```html
<!-- filepath: /C:/Users/shubh/Projects/Django_tasks/djcore_template_task/templates/about.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ content }}</h1>
</body>
</html>
```

By following these steps, you can render HTML templates in your Django project and pass dynamic context data to them.


