from django.urls import path, include

from .views import CategoryApi, ServiceApi, get_services_for_title, AddServiceApi, SalonsApi, AddSalonsApi, get_category_for_salon

app_name = 'api'

urlpatterns = [
    path('services/', ServiceApi.as_view()),
    path('add_service/', AddServiceApi.as_view()),
    path('category/', CategoryApi.as_view()),
    path('salons/', SalonsApi.as_view()),
    path('add_salon/', AddSalonsApi.as_view()),
    path('services/<str:text>', get_services_for_title),
    path('categories_for_salon/<int:pk>', get_category_for_salon),

]
