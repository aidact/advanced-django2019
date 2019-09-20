from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Company(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Review(models.Model):
    rating = models.PositiveIntegerField()
    title = models.CharField(max_length=64)
    summary = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='date')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.rating} {self.title} {self.summary}'
