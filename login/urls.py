from django.urls import path


from .views import IndexLogin


urlpatterns = [

   path('', IndexLogin.as_view()),

]
