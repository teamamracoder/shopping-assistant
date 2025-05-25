# 🛒 Shopping Assistant
--------------------------

## 💻 Local setup.

### 1. Install required softwares
> 🐍 Python version
- 3.12.3

> 📂 PostgreSQL version
- psql (PostgreSQL) 16.6 (Ubuntu 16.6-0ubuntu0.24.04.1)

### 2. Create and activate virtual environment
> python -m venv venv

> venv\Scripts\activate

### 3. Install packages
> pip install -r requirements.txt

### 4. Migrate
> python manage.py makemigrations

> python manage.py migrate

### 6. Run
> python manage.py runserver

##### OR

> daphne -b 127.0.0.1 -p 8000 idp.asgi:application