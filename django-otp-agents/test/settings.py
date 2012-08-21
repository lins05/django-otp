# django-otp-agents test project

from os.path import dirname, join, abspath

def project_path(path):
    return abspath(join(dirname(__file__), path))

DEBUG = True

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django_otp',
    'django_otp.plugins.otp_static',
    'django_agent_trust',
    'otp_agents',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django_agent_trust.middleware.AgentMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATE_DIRS = [
    project_path('templates'),
]

SECRET_KEY = 'iNkqvGrLybbwdtUSWgTeutLPUp4pe0Y1Mhfdo05x6OIeDHhbUI9uCJA1gNVAdLhp'

ROOT_URLCONF = 'otp_agents.tests.urls'
LOGIN_URL = '/login/'
