#!/bin/bash
# Requires the database to be up
FLASK_ENV=development DATABASE_URI=sqlite:///database.db python manage.py
