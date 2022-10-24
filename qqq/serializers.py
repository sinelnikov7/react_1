from rest_framework import serializers

from .models import Category, Service, Salon


class AddSalonSerializer(serializers.ModelSerializer):
    "Для добавления салона"
    class Meta:
        model = Salon
        fields = ("id", "name", "slug", "services")


class ServiceSerializer(serializers.ModelSerializer):
    "Для получения всех сервисов и сортировки на фронте"
    # salon_set = AddSalonSerializer(many=True)
    class Meta:
        model = Service
        depth = 1
        fields = ('id', 'title', 'slug', 'price', 'category', 'salon_set')


class AddServiceSerializer(serializers.ModelSerializer):
    "Для добавления сервиса"
    class Meta:
        model = Service
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    "Для получения всех категорий"
    class Meta:
        model = Category
        # depth = 1
        fields = ('id', 'name', 'slug', 'service_set')


class SalonSerializer(serializers.Serializer):
    "Для получения всех салонов"
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    slug = serializers.CharField()
    services = ServiceSerializer(many=True)










