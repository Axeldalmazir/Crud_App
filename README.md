# CRUD Application - Flask & React

## Description

This project is a web-based CRUD (Create, Read, Update, Delete) application utilizing Flask for the back-end API and React for the front-end interface. Users can perform CRUD operations on database records through the web interface.

## Features

-   **Create** new records in the database
-   **Read** existing records
-   **Update** records
-   **Delete** records

## Technologies Used

-   **Back-end**: Flask, SQLAlchemy (database ORM)
-   **Front-end**: React, Axios (HTTP client for API requests)
-   **Database**: SQLite/PostgreSQL

## Prerequisites

-   Python 3.x and `pip` for installing Flask and dependencies
-   Node.js and `npm` for installing React dependencies

## Installation

### 1. Clone the Repository

bash

Copier le code

`git clone https://github.com/Axeldalmazir/flask_crud_app.git
cd flask_crud_app` 

### 2. Install Back-end Dependencies

bash

Copier le code

`pip install -r requirements.txt` 

### 3. Install Front-end Dependencies

bash

Copier le code

`cd client
npm install` 

### 4. Configure the Database

Adjust the database configuration in the Flask settings file and run any migrations needed.

### 5. Start the Application

-   **Back-end (Flask)**:
    
    bash
    
    Copier le code
    
    `python app.py` 
    
-   **Front-end (React)**:
    
    bash
    
    Copier le code
    
    `cd client
    npm start`
