from django.urls import path, include
from rest_framework import routers

from .views import *

# from .APIViews import *

router = routers.DefaultRouter()
router.register("Uer_reg", user_reg_view, basename='User_reg')
router.register("book_api", Book_View, basename='book_api')
router.register("teacher", Teacher, basename='teacher')
router.register("student", Student_View, basename='student')


urlpatterns = [

    path('', include(router.urls)),

]
