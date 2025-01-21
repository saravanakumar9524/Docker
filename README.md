Feedback App
A simple web application to collect feedback from users, with a frontend served by Nginx, a backend powered by Flask, and PostgreSQL as the database. This project is containerized using Docker and orchestrated with Docker Compose.


Project Overview
This Feedback App allows users to submit feedback via a simple form. The feedback is collected through the frontend (HTML form), sent to the backend (Flask API), and stored in a PostgreSQL database.

Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python, Flask
Database: PostgreSQL
Web Server: Nginx (to serve the frontend)
Containerization: Docker
Orchestration: Docker Compose


Access the frontend at:

http://localhost:8080

The backend API is available at:

http://localhost:5000


Usage
Once the app is running, you can:

Submit feedback through the form on the frontend.
The backend will receive the feedback and print it to the console.
The feedback is stored in the PostgreSQL database.