from rest_framework import serializers

from .models import Category, Service, Salon, ProstoModel


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
        depth = 0
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

class SaveSalonSerializer(serializers.Serializer):
    "Для получения всех салонов"

    name = serializers.CharField(max_length=255)
    slug = serializers.CharField()
    services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)

class ProstoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProstoModel
        fields = '__all__'
    # services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)


class NewServiceSerializer(serializers.Serializer):
    "Для получения всех салонов"
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    slug = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    salon_set = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)


    def create(self, validated_data):

        new_service = Service(title=validated_data["title"], slug=validated_data["slug"],
                                             price=validated_data["price"], category_id=validated_data["category"].id)
        new_service.save()
        for i in validated_data["salon_set"]:
            new_service.salon_set.add(i.id)

        return new_service









