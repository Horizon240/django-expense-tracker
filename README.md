# Personal Expense Tracker (Django + Microsoft SQL Server)

A multi-user full-stack web application for logging, categorizing, filtering, and visualizing personal expenses, built with **Python**, **Django**, and **Microsoft SQL Server**.

## Features

* **User Authentication & Data Isolation:** Secure user registration, login, and logout using Django's authentication system. Every expense record is tied to a specific user (`ForeignKey`) so accounts remain strictly private.
* **Full CRUD Operations:** Create, view, edit, and delete expenses using validated Django `ModelForm`s and `POST`-only deletion with CSRF protection.
* **Dynamic Search & Filtering:** Search expenses by title (`icontains`) and filter by category via `GET` query parameters with real-time total recalculation.
* **Interactive Analytics:** Visualizes category-wise spending breakdowns using **Chart.js** powered by SQL Server ORM aggregations (`Sum` + `GROUP BY`).
* **Environment-Based Configuration:** Keeps database credentials and Django's `SECRET_KEY` isolated via `python-dotenv` and `.env`.

## Tech Stack

* **Backend:** Python 3.13, Django 5.2
* **Database:** Microsoft SQL Server (`mssql-django`, `pyodbc`, ODBC Driver 17)
* **Frontend:** HTML5, Bootstrap 5, Chart.js, Django Templates

## Local Setup & Installation

### 1. Prerequisites
* Python 3.10+
* Microsoft SQL Server (Express or Developer Edition)
* Microsoft ODBC Driver 17 (or 18) for SQL Server

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/django-expense-tracker.git](https://github.com/YOUR_USERNAME/django-expense-tracker.git)
cd django-expense-tracker