# Overview

In this project, I accomplished a web application with Django. The purpose of this application is to make a reservation website where client can have access to different rentals published by different owners. It uses a database (sqlite) to store data about rentals, rooms, and owners. The web app will then use this data to display the information of each category with the use of Django.

To start a web server, you will have to open the terminal and run the following command:

```
python manage.py runserver
```

This web server is very basic in the design because it is mainly focused on showing the different functionalities of Django. This web app is interactive, and the clients can log in with their account and every page will be dynamic by showing specific information about what the user chose to research or click.

[Software Demo Video](https://youtu.be/_HzjDK17rvA)

# Web Pages

catalog/ Index of the website, it displays the number of rooms, rentals, and owner from the database.
catalog/rentals/ It displays the list of the rentals in the website.
catalog/rentals/<int:pk>/ It displays the details from a specific rental of the list given in the previous link.
catalog/myreservations/ It displays the list of reservations for a specific user, you have to be log in the website to access this data.

# Development Environment

Web Framework - Danjgo
Python (Use of several Django libraries for the functioning of the website.)
Html
Css (Use of the bootstrap library)

# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/en/3.0/contents/)
* [Quick Guide](https://www.tutorialspoint.com/django/django_quick_guide.htm)
* [Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)
* [Other resources for inspiration](https://realpython.com/get-started-with-django-1/)

# Future Work

* The "My Reservations" page doesn't fully work, and I will have to work on that in the future to display all the reservations of an user in the website.
* The use of a form to register on the website and reserve a room can be useful for clients to choose the room they want online.
* The website is very basic, and it will need more css to make it more attractive for clients. (The main focus of this project was to use Django functionalities first)