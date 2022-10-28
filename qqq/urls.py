from django.urls import path, include
from rest_framework import routers

from .views import CategoryApi, get_services_for_salon, ServiceApi, get_services_for_title, AddServiceApi, SalonsApi, \
    AdddSalonsApi, get_category_for_salon, ProstoModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'prosto_model', ProstoModelViewSet)
# router.register(r'salons', SalonsApi)

urlpatterns = [
    path('services/', ServiceApi.as_view()),
    path('add_service/', AddServiceApi.as_view()),
    path('category/', CategoryApi.as_view()),
    path('salons/', SalonsApi.as_view()),
    path('add_salon/', AdddSalonsApi.as_view()),
    path('services/<str:text>', get_services_for_title),
    path('categories_for_salon/<int:pk>', get_category_for_salon),
    path('services_for_salon/<int:pk>', get_services_for_salon),
    # path('', include(router.urls)),

]

urlpatterns += router.urls
print(router)
print(router.urls)
print(urlpatterns)
