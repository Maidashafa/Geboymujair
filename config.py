import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kunci-rahasia-super-panjang-dan-acak-123456'
    
    # Email
    MAIL_SERVER = os.environ.get('SMTP_HOST') 
    MAIL_PORT = int(os.environ.get('SMTP_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') == 'True'
    MAIL_USERNAME = os.environ.get('SMTP_USER')
    MAIL_PASSWORD = os.environ.get('SMTP_PASS')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@geboymujair.my.id')
    
    
    # Supabase
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')