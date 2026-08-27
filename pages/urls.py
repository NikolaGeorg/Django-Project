from django.urls import path
<<<<<<< HEAD
from .views import home_page_view
urlpatterns = [
    path("", home_page_view),
=======

from .views import home_page_view, about_page_view
     
urlpatterns = [
        path("about/", about_page_view),
	path("", home_page_view),
>>>>>>> 37081ae (initial commit)
]
