import rest_framework
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .filter import ServiseFilter
from .models import Category, Service, Salon, ProstoModel
from .serializers import ServiceSerializer, CategorySerializer, AddServiceSerializer, SalonSerializer, \
    AddSalonSerializer, ProstoModelSerializer, SaveSalonSerializer, NewServiceSerializer


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
    # category_list = Category.objects.filter(service__salon__id=pk).distinct()
    # serializer = CategorySerializer(category_list, many=True)

    categories = Category.objects.prefetch_related("service_set").all()
    category_list = categories.filter(service__salon__id=pk).distinct()
    serializer = CategorySerializer(category_list, many=True)
    print(categories)
    return Response(serializer.data)

@api_view()
def get_services_for_title(request, text):
    service = get_object_or_404(Category, name=text)
    serializer = CategorySerializer(service)
    print(service)
    print(dir(service))
    # time.sleep(10)
    return Response(serializer.data)

@api_view()
def get_services_for_salon(request, pk):

    services = Service.objects.prefetch_related("salon_set")
    services_list = services.filter(salon__id=pk)
    serializer = ServiceSerializer(services_list, many=True)
    print(services, "Все сервисы???????????????")
    print(services_list, "Сервисы по салону!!!!!!!!!!!!!!!")
    return Response(serializer.data)


class SalonsApi(generics.ListAPIView, generics.CreateAPIView):

    serializer_class = SalonSerializer
    model = Salon
    queryset = Salon.objects.all()




class AddSalonsApi(generics.CreateAPIView):

    serializer_class = AddSalonSerializer
    model = Salon
    queryset = Salon.objects.all()

class ProstoModelViewSet(viewsets.ModelViewSet):

    queryset = ProstoModel.objects.all()
    serializer_class = ProstoModelSerializer

class AdddSalonsApi(APIView):

    def post(self, request):
        data = SaveSalonSerializer(data=request.data)
        if data.is_valid():
            instanse = Salon(name=request.data["name"], slug=request.data["slug"])
            instanse.save()
            for i in request.data["services"]:
                instanse.services.add(i)
            instanse.save()
            return Response({"data":AddSalonSerializer(Salon.objects.all(), many=True).data})
        else:
            return Response({"status": "NotOk"})


class NewServiceApi(APIView):
    def get(self, request):
        queryset = Service.objects.all()
        serializers = NewServiceSerializer(queryset, many=True)
        return Response({"data": serializers.data})

    def post(self, request):
        serializer = NewServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.create(serializer.validated_data)
        return Response(NewServiceSerializer(response).data)
