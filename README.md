# Airline Passengers

A small Django application for keeping track of airports, flights, and passengers. The interface is in French, and the project uses SQLite for local data storage.

## Features

- List flights with their origin, destination, duration, and passengers.
- List airports and passengers, including the flights associated with each passenger.
- Create airport, flight, and passenger records through forms.
- Manage records through Django's built-in admin site.

## Requirements

- Python
- Git

The Python dependency is pinned in `requirements.txt` (Django 6.1.1).

## Clone and run on Windows

Open PowerShell and run:

```powershell
git clone <repository-url> airline-passagers-create
cd airline-passagers-create
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Replace `<repository-url>` with the URL of this Git repository. If PowerShell blocks virtual-environment activation, allow scripts for the current PowerShell process and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Open <http://127.0.0.1:8000/flights/> in your browser. The development server stops when you press `Ctrl+C` in the terminal.

## Tests

With the virtual environment activated, run:

```powershell
python manage.py test
```

## Project structure

- `airline_passengers/` contains the Django project configuration and the root URL configuration.
- `flights/models.py` defines the data: an airport has a three-character unique code and a city; a flight connects origin and destination airports and has a duration in minutes; a passenger can be associated with multiple flights.
- `flights/forms.py` defines the forms used to create those records.
- `flights/views.py` loads and displays records and handles form submissions.
- `flights/urls.py` maps the flight app's pages to their views.
- `flights/templates/flights/` contains the HTML pages and shared layout.
- `flights/migrations/` contains database schema migrations.
- `db.sqlite3` is the local SQLite database. Run migrations after cloning to create the database schema.

## Pages

| URL                           | Page               |
| ----------------------------- | ------------------ |
| `/flights/`                   | Flight list        |
| `/flights/airports/`          | Airport list       |
| `/flights/passengers/`        | Passenger list     |
| `/flights/airports/create/`   | Create an airport  |
| `/flights/create/`            | Create a flight    |
| `/flights/passengers/create/` | Create a passenger |
| `/admin/`                     | Django admin       |

To sign in to the admin site, create a local administrator account with `python manage.py createsuperuser` and follow the prompts.


