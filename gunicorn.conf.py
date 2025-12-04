# gunicorn.conf.py
import os
# Bind the application to the port provided by Railway
bind = '0.0.0.0:' + os.environ.get('PORT', '5000')

# Specify the WSGI application entry point: file_name:app_object_name
# This explicitly tells Gunicorn to look inside app.py for the object named 'app'
wsgi_app = 'app:app'

# Set the worker type for compatibility (optional, but often helps)
worker_class = 'gthread'

# Set the number of workers (e.g., 2 workers)
workers = 2 

# Enable logging and UTF-8 output (to help with your emoji/encoding issue)
accesslog = '-'
errorlog = '-'
log_file = '-'
# This helps enforce UTF-8 for logs, but is secondary to LANG/LC_ALL
# log_config = 'logging.conf' 

# Set Python Path explicitly (crucial for ModuleNotFoundError)
pythonpath = '.'