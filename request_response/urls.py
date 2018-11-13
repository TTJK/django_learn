from django.conf.urls import url
from . import views

urlpatterns = [
    url (r"weather1/([a-z]+)/(\d{4})/$", views.weather1),
    url (r"weather2/([a-z]+)/(\d{4})/$", views.weather2),
    url (r"weather3/(?P<city>[a-z]+)/(?P<year>\d{4})/$", views.weather3),
    url (r"weather4/(?P<city>[a-z]+)/(?P<year>\d{4})/$", views.weather4),
    url (r"^get_body_form/$", views.get_body_form),
    url (r"^get_body_json/$", views.get_body_json),
    url (r'^response_json/$', views.response_json),
    url (r'^response_json1/$', views.response_json1),
    url (r'^response_json2/$', views.response_json2),
    url (r"^cookie_demo/$", views.cookie_demo),
    url (r"^session_demo/$",views.session_demo),
]
