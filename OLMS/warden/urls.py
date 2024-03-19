from django.urls import path
from . import views
urlpatterns=[
    path("show-all-leaves/",views.showAllLeaves,name="show-all-leaves"),
    path("show-all-outings/",views.showAllOutings,name="show-all-outings"),
]