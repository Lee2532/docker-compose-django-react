import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

            
# SECURITY WARNING: don't run with debug turned on in production!

# Application definition

# AUTH_USER_MODEL = 'accounts.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_spectacular',
    'rest_framework',
    'crispy_forms', #css 보기 좋게
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')],
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



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), "static"),
]


WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases




DB_NAME = os.environ.get("POSTGRES_DB", None)
DB_USER = os.environ.get("POSTGRES_USER", None)
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", None)
DB_HOST = os.environ.get("POSTGRES_HOST", None)
DB_PORT = os.environ.get("POSTGRES_PORT", None)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }

}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

REST_FRAMEWORK = {
    # YOUR SETTINGS  drf의 schema 클래스를 drf-specacular의 AutoSchema로 교체해줍니다.
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    # General schema metadata. Refer to spec for valid inputs
    # https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#openapi-object
    'TITLE': 'drf-spectacular API Document',

    'DESCRIPTION': 'drf-specatular 를 사용해서 만든 API 문서입니다.',
    'CONTACT': {'name': 'Lee2532', 'email': 'seungoh1020@naver.com'},
    # Swagger UI를 좀더 편리하게 사용하기위해 기본옵션들을 수정한 값들입니다.
    'SWAGGER_UI_SETTINGS': {
        # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/  # 사용 가능한 옵션들
        'dom_id': '#swagger-ui',  # required(default)
        'layout': 'BaseLayout',  # required(default)
        'deepLinking': True,  # API를 클릭할때 마다 SwaggerUI의 url이 변경됩니다. (특정 API url 공유시 유용하기때문에 True설정을 사용합니다)
        'persistAuthorization': True,  # True 이면 SwaggerUI상 Authorize에 입력된 정보가 새로고침을 하더라도 초기화되지 않습니다.
        'displayOperationId': True,  # True이면 API의 urlId 값을 노출합니다. 대체로 DRF api name둘과 일치하기때문에 api를 찾을때 유용합니다.
        'filter': True,  # True 이면 Swagger UI에서 'Filter by Tag' 검색이 가능합니다
    },
    # Optional: MUST contain "name", MAY contain URL
    'LICENSE': {
        'name': 'MIT License',
        'url': 'https://github.com/KimSoungRyoul/DjangoBackendProgramming/blob/main/LICENSE',
    },
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,  # OAS3 Meta정보 API를 비노출 처리합니다.

    # https://www.npmjs.com/package/swagger-ui-dist 해당 링크에서 최신버전을 확인후 취향에 따라 version을 수정해서 사용하세요.
    'SWAGGER_UI_DIST': '//unpkg.com/swagger-ui-dist@3.38.0',  # Swagger UI 버전을 조절할수 있습니다.
}


