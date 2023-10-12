from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()), # for class based views
    # path("", views.review),
    path("thank-you", views.thank_you)
]