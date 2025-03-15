# settings.py

# SECURITY SETTINGS
import os

# Set debug mode off in production
DEBUG = False

# List of allowed hosts (change according to your domain)
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Ensure cookies are secure and sent over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Enabling the browser XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Preventing clickjacking by denying framing of the site
X_FRAME_OPTIONS = 'DENY'

# Preventing content type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Redirect all HTTP traffic to HTTPS
SECURE_SSL_REDIRECT = True
# Enforce HTTPS connections for 1 year (in seconds)
SECURE_HSTS_SECONDS = 31536000
# Apply HSTS to all subdomains as well
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# Allow your site to be included in the HSTS preload list
SECURE_HSTS_PRELOAD = True
# Ensure session cookies are only transmitted over HTTPS
SESSION_COOKIE_SECURE = True
# Ensure CSRF cookies are only transmitted over HTTPS
CSRF_COOKIE_SECURE = True
# Prevent the site from being embedded in an iframe
X_FRAME_OPTIONS = 'DENY'
# Prevent browsers from sniffing the content type
SECURE_CONTENT_TYPE_NOSNIFF = True
# Enable browser XSS filtering
SECURE_BROWSER_XSS_FILTER = True


# CSP (Content Security Policy) settings (Optional - Add `django-csp` middleware if using)
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'")
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")

# Database configuration (adjust these according to your database)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # example for PostgreSQL
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Other necessary Django settings can be added here
