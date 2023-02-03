from django.urls import path
from .views import *

urlpatterns = [
    path('', Dashboard.as_view()),
    # path('add-data', data_entry),
    path('api', FetchData.as_view(), name='api'),
    # path('api/<int:pk>', )
]