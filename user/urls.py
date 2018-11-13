from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^user/index/$",views.index,name="index"),
    url(r"^user/response_redirect",views.response_redirect)

]

