# ecom-admin-fast-api-engine
A robust back-end API built with FastAPI (Python), designed to power a web-based admin dashboard tailored for e-commerce managers. This API provides comprehensive insights into sales performance, revenue trends, and current inventory status. E-commerce admins can register new products, update inventory levels, and monitor product availability in real-time. It offers advanced revenue analytics with support for weekly, monthly, yearly, or custom date range evaluations, helping businesses make data-driven decisions. The system also highlights low-stock inventory to enable timely restocking. Furthermore, the API maintains a complete history of inventory changes for audit and tracking purposes. All endpoints are RESTful, well-documented, and secured, ensuring seamless integration with front-end dashboards and other services.



## Prerequisites

Python 3.10 or higher
SQLite (bundled with Python, no separate install needed)

## Recommended: virtual environment tool (venv or virtualenv)

## Setup Instructions
Clone the repository

```bash
git clone https://github.com/abdullahaleem355/ecom-admin-fastapi-engine.git
cd ecom-admin-fastapi-engine
```

## Create and activate a virtual environment

```bash
python -m venv venv
```
## Windows
```bash
venv\Scripts\activate
```
## Linux/Mac
```bash
source venv/bin/activate
```
## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
uvicorn main:app --reload
```
## Accessing the API Documentation
Once the app is running, open your browser and go to:

http://127.0.0.1:8000/docs

This opens the interactive Swagger UI where you can explore and test all API endpoints.

## Note
Reference Scripts for Amazon like dummy data as well as all API endpoints description is available in artifacts folder present in root directory.
