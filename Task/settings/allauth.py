AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend'
)

SITE_ID = 2

ACCOUNT_EMAIL_REQUIRED = True
LOGOUT_URL = "/accounts/logout/"
LOGIN_REDIRECT_URL = "/"
