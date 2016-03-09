"""django_realfavicongenerator URL Configuration """

from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [

    # home page:
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # favicons:
    url('', include('realfavicongenerator.urls')),

]
