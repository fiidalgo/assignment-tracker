# Assignment Tracker

A simple web-based task management application built using Flask. This application allows users to create, read, update, and delete (CRUD) assignments. Users can also filter assignments by searching for specific keywords related to the assignment name or class name.

## Purpose

The purpose of this project is to provide a straightforward tool for managing academic assignments. It serves as a demonstration of basic CRUD operations using Python and Flask, and it includes features such as search filtering to help users find assignments quickly.

## Features

- **Add Assignments**: Create new assignments with details like assignment name, class name, and due date.
- **View Assignments**: Display a list of all assignments.
- **Update Assignments**: Edit details of existing assignments.
- **Delete Assignments**: Remove assignments that are no longer needed.
- **Search Functionality**: Filter assignments by keywords in real-time.
- **View All Button**: Reset the view to display all assignments after filtering.

## Technologies Used

- **Python**: Programming language used for backend logic.
- **Flask**: Lightweight WSGI web application framework used for building the application.
- **SQLite**: A C-language library that provides a relational database management system. Used for storing assignment data.
- **HTML/CSS/JavaScript**: Frontend technologies used for the user interface and interactivity.

## Project Structure

```plaintext
assignment-tracker/
├── static/                   # Directory for static files like CSS and JavaScript
│   ├── styles.css            # CSS file for styling the application
│   └── scripts.js            # JavaScript file for dynamic filtering functionality
├── templates/                # Directory for HTML templates
│   ├── index.html            # Main page template to display and manage assignments
│   └── update.html           # Template for updating an assignment
├── app.py                    # Main Flask application file
├── database.db               # SQLite database file (created after running the app)
└── README.md                 # Project description and instructions (this file)
```

## Dependencies

To run this project, you'll need to have the following dependencies installed:

- **Flask**: Web framework for Python.
- **SQLite3**: Used for the database, which is included with Python.

You can install Flask using pip:

```bash
pip install Flask
```

## How to Run the Project

Follow these steps to run the project on your local machine:

1. **Clone the repository:**

```bash
git clone git@github.com:yourusername/assignment-tracker.git
cd assignment-tracker
```

2. **Set up a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate # for Windows use `venv\Scripts\activate`
```

3. **Install dependencies:**

```bash
pip install Flask
```

4. **Initialize the database:**

* The database will be automatically created when you run the Flask application for the first time.

5. **Run the application:**

```bash
python app.py
```

6. **Access the application:**

* Open your web browser and navigate to `http://127.0.0.1:5000/` to start managing your assignments.