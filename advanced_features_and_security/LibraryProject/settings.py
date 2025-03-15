# LibraryProject/settings.py

import os
from pathlib import Path

# Base directory for your project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings (set a secret key in production)
SECRET_KEY = 'your-secret-key-here'

# Debug mode (set to False in production)
DEBUG = False
SECURE_BROWSER_XSS_FILTER = True  # Protect against cross-site scripting (XSS)
X_FRAME_OPTIONS = 'DENY'  # Prevent your site from being embedded in a frame to avoid clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from interpreting files as something else
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are only sent over HTTPS
SECURE_SSL_REDIRECT = True


# Allowed hosts (use '*' to allow all, but be more restrictive in production)
ALLOWED_HOSTS = []

# Installed apps (add your app and required apps here)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # Add your app here
    'csp'
]

# Middleware for handling requests
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'",)

# URL configuration
ROOT_URLCONF = 'LibraryProject.urls'

# Templates settings (for rendering HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database configuration (SQLite for simplicity)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization settings (date/time formats, language, timezone)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files settings (for serving CSS, JS, images)
STATIC_URL = '/static/'

# Media files settings (for user-uploaded files like images)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Custom user model - set this to the path of your custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Other optional settings (for example, if you want to add logging, caching, etc.)
