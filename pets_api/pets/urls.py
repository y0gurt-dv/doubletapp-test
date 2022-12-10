from pets.views import pet as pet_views
from django.urls import path


urlpatterns = [
    path('', pet_views.PetListCreateDeleteView.as_view()),
    path('<uuid:id>/photo/', pet_views.AddPhotoToPetView.as_view()),
]
