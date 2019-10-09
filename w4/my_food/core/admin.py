from django.contrib import admin

from core.models import Food, Compatibility, Recommendation, Wall


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type',
        'quantity'
    )

    fields = ('name', 'type', 'quantity')


@admin.register(Compatibility)
class CompatibilityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'count'
    )

    fields = ('count',)


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'analysis',
        'recommend'
    )

    fields = ('analysis', 'recommend')


@admin.register(Wall)
class WallAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'food',
        'water',
        'recommendation',
    )

    fields = ('user', 'food', 'water', 'recommendation', 'compatibility')
