from rest_framework.routers import DefaultRouter
from .views import *

library_router=DefaultRouter()
library_router.register(r'book',BookView)