from django.urls import path
from .views import *

urlpatterns =[
  path('', GetTokenApiView.as_view()),
  path('get_token', GetTokenApiView.as_view()),
  path('goods', list_goods),
  path('new_good', new_good),
  path('get_token/', GetTokenApiView.as_view()),
  path('goods/', list_goods),
  path('new_good/', new_good),
]
