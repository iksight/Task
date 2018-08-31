from split_settings.tools import include

include(
    'common.py',
    'apps.py',
    'database.py',
    'allauth.py',

    scope=globals()
)
