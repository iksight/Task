# Application definition

INSTALLED_APPS = [
    # user apps
    'Task.apps.products.apps.ProductsConfig',

    # adminlte2
    'django_adminlte',
    'django_adminlte_theme',

    # common
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
