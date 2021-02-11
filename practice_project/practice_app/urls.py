from django.conf.urls import url
from practice_app import views

app_name='practice_app'

urlpatterns=[
  url(r'^user_login',views.user_login,name='user_login'),
]
