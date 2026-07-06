# Inventory Management System API

## Overview

The Inventory Management System API is a Flask-based REST API developed for a retail company to manage inventory items. The application allows users to perform CRUD (Create, Read, Update, Delete) operations on inventory and integrates with the OpenFoodFacts API to retrieve real-time product information using a barcode.

A command-line interface (CLI) is also included to make interacting with the API simple.

---

## Features

* View all inventory items
* View a single inventory item
* Add new inventory items
* Update existing inventory items
* Delete inventory items
* Search products by barcode using the OpenFoodFacts API
* Command Line Interface (CLI)
* Unit tests for API endpoints

---

## Technologies Used

* Python 3
* Flask
* Requests
* REST API
* OpenFoodFacts API
* unittest
* Git & GitHub

---

## Project Structure

```
Python-Rest-Api/
│
├── app.py
├── inventory.py
├── external_app.py
├── cli.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│
└── tests/
    └── test_app.py
```

---

## Installation

Clone the repository:

```bash
git clone git@github.com:HexCipher224/Python-Rest-Api.git
```

Move into the project directory:

```bash
cd Python-Rest-Api
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

---

## API Endpoints

| Method | Endpoint           | Description                          |
| ------ | ------------------ | ------------------------------------ |
| GET    | /                  | Home route                           |
| GET    | /items             | Retrieve all inventory items         |
| GET    | /items/<id>        | Retrieve one inventory item          |
| POST   | /items             | Add a new item                       |
| PATCH  | /items/<id>        | Update an existing item              |
| DELETE | /items/<id>        | Delete an item                       |
| GET    | /product/<barcode> | Search a product using OpenFoodFacts |

---

## Running the CLI

Open another terminal while the Flask server is running and execute:

```bash
python cli.py
```

The CLI allows users to:

* View inventory
* Add inventory items
* Update inventory items
* Delete inventory items
* Search products using a barcode

---

## Running Tests

Execute the test suite:

```bash
python -m unittest discover tests
```

---

## External API

This project integrates with the OpenFoodFacts API.

Example:

```
https://world.openfoodfacts.org/api/v0/product/737628064502.json
```

---

## Author

**Duncan**

Software Engineering Student

Moringa School

GitHub: https://github.com/HexCipher224

---

## License

This project was created for educational purposes as part of the Moringa School Software Engineering Program.
