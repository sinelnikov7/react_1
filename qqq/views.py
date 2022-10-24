import rest_framework
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .filter import ServiseFilter
from .models import Category, Service, Salon
from .serializers import ServiceSerializer, CategorySerializer, AddServiceSerializer, SalonSerializer, \
    AddSalonSerializer


class ServiceApi(generics.ListAPIView):

    serializer_class = ServiceSerializer
    model = Service
    queryset = Service.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ServiseFilter
    # print("eeeeeeeeee")
    # print(Service.objects.get(id=1).salon_set.values_list())
    # print(dir(Service.objects.get(id=3).salon_set))

class AddServiceApi(generics.CreateAPIView):

    serializer_class = AddServiceSerializer
    model = Service
    queryset = Service.objects.all()


class CategoryApi(generics.ListAPIView, generics.CreateAPIView):

    serializer_class = CategorySerializer
    model = Category
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        b = Category.objects.filter(service__salon__id=1)
        print(b)
        return self.list(request, *args, **kwargs)

@api_view()
def get_category_for_salon(request, pk):
    category_list = Category.objects.filter(service__salon__id=pk).distinct()
    serializer = CategorySerializer(category_list, many=True)
    return Response(serializer.data)

@api_view()
def get_services_for_title(request, text):
    service = get_object_or_404(Category, name=text)
    serializer = CategorySerializer(service)
    print(service)
    print(dir(service))
    # time.sleep(10)
    return Response(serializer.data)


class SalonsApi(generics.ListAPIView):

    serializer_class = SalonSerializer
    model = Salon
    queryset = Salon.objects.all()



class AddSalonsApi(generics.CreateAPIView):

    serializer_class = AddSalonSerializer
    model = Salon
    queryset = Salon.objects.all()

# @api_view()
# def get_services_for_title(request, text):
#     service = Service.objects.filter(category__name=text)
#     serializer = ServiceSerializer(service, many=True)
#     return Response(serializer.data)