"""
Django settings for Hackathon project.

Generated by 'django-admin startproject' using Django 4.1.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g*k^ov)wr*c5&fn*fg+cu6#=6&5xd*^e)!+6u)9!a*(ll%uo&i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AI.apps.AiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'Hackathon.urls'

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

WSGI_APPLICATION = 'Hackathon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# settings.py에서 Trusted Origins 설정 확인:
# Django 프로젝트의 settings.py 파일에 있는 CSRF_TRUSTED_ORIGINS 설정을 확인하세요.
# ngrok의 URL을 허용하는지 확인하고 필요한 경우 추가하세요. 예를 들어:
CSRF_TRUSTED_ORIGINS = [
    "https://2bca-39-126-154-116.ngrok-free.app",
    "http://backxchang.com",
    "http://backxchang.com:8000",

]
# settings.py에서 CSRF_COOKIE_SECURE 설정 변경:
# 개발 단계에서는 settings.py 파일에서 CSRF_COOKIE_SECURE를 False로 변경할 수 있습니다.
# 하지만 실제 운영 환경에서는
# 이 값을 True로 설정하여 보안을 유지하는 것이 좋습니다. 개발 중에만 잠시 변경하고,
# 운영 환경에서는 다시 True로 변경하세요:

CSRF_COOKIE_SECURE = False  # 개발 중에만 사용

# CORS_ALLOWED_ORIGINS = [
#     "https://www.clarifai.com/",  # 예시: 클라리파이 서버 도메인
#     # 추가적인 도메인이 있다면 여기에 추가
# ]
CORS_ALLOW_ALL_ORIGINS = True
# 또는 특정 원본 허용
# CORS_ALLOW_ORIGINS = [
#     "http://example.com",
#     "https://example.com",
# ]
CORS_ALLOW_METHODS = [
    'GET',  # 기본적으로 GET 요청 허용
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
