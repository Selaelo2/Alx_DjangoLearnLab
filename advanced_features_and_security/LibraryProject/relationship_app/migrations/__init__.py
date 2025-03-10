# Make migration files for model changes (including custom permissions)
python manage.py makemigrations # type: ignore

# Apply the migrations to the database
python manage.py migrate
