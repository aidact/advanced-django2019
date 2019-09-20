from django.contrib import admin

from demo.api.models import Company, Review


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'rating',
                    'title',
                    'company',
                    'created_by')
