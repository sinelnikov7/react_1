from django.contrib import admin

from .models import Category, Service, Salon


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

class SalonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register( Salon, SalonAdmin)
