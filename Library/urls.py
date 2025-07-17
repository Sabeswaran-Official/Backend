from django.urls import path,include
from .router import *

urlpatterns = [
    path('api/',include(library_router.urls)),
    path('laptop/',LaptopView.as_view()),
    path('laptop/<int:pk>/',LaptopViewByID.as_view())
]
