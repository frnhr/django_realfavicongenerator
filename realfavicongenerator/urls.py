import os

from django.conf import settings
from django.conf.urls import url
from django.views.static import serve


realfavicongenerator_static_dir = os.path.join(settings.STATIC_ROOT,
                                               'realfavicongenerator')
file_names = os.listdir(realfavicongenerator_static_dir)

urlpatterns = [
    url(r'^' + file_name + '$', serve, kwargs={
        'path': file_name,
        'document_root': realfavicongenerator_static_dir,
    }) for file_name in file_names
]
