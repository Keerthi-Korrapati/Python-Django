from django.urls import path
from . import views


'''urlpatterns = [
    path("january", views.january),
    path("february", views.february),
    path("march", views.march),
    #path("<month>", views.monthy_challenge) # Dynamic path segment i.e., placeholder for a dynamic part of the URL
]'''

urlpatterns = [
    path("",views.index, name="index"), # /challenges/
    path("<int:month>", views.challenge_by_number), # /challenges/1
    path("<str:month>", views.monthly_challenge, name="monthly_challenge") # /challenges/january  # Named URL
]