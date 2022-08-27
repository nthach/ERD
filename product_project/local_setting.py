# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-94ka@y#2ndal--d(3$q*rn+gl+kw38@m&_j^alwk0c8n&3j*qn'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'product_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}