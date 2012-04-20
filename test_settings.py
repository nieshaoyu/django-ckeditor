DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'ckeditor.test.db',                      
    }
}

INSTALLED_APPS = [
    'ckeditor',
]

CKEDITOR_MEDIA_PREFIX = '/media/'
CKEDITOR_UPLOAD_PATH = '/tmp'
