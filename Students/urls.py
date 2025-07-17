from django.urls import path 
from .views import *

urlpatterns = [
    path('api/',StudentAPI.as_view()),
    path('api/<int:stud_id>/',StudentAPI.as_view()),
    path('task/api/',TaskAPI.as_view()),
    path('task/api/<int:task_id>/',TaskAPI.as_view()),
    # path('task/api/<int:task_id>/',TaskAPIById.as_view()) ;is no need ;because of dynamic get method used ,create separate path for same class with id path
    path('rank/',RankView.as_view()),
    path('rank/<int:id>/',RankView.as_view())
]

