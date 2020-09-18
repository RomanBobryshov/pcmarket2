from django.contrib import admin
from .models import Processor, VideoCard, RAM, Motherboard, SSD, Product


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoCard)
class VideoCardAdmin(admin.ModelAdmin):
    pass


@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    pass


@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    pass


@admin.register(SSD)
class SSDAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass



