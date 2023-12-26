from django.urls import path


from .views import CurrentDateView, rand, hellow, IndexView


urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('random/', rand),
   path('hello/', hellow),
   path('', IndexView.as_view()),

]

