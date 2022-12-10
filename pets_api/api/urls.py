from django.urls import include, path

urlpatterns = [
    path('pets/', include('pets.urls'))
]
