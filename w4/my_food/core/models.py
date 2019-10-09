from django.db import models

from users.models import User
from utils.constants import TYPES, BREAKFAST


class Food(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPES, default=BREAKFAST)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Food'

    def __str__(self):
        return f'{self.name}: {self.type}, {self.quantity}'


class Recommendation(models.Model):
    analysis = models.CharField(max_length=255)
    recommend = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'

    def __str__(self):
        return f'{self.recommend}, {self.analysis}'


class Compatibility(models.Model):
    count = models.IntegerField()

    class Meta:
        verbose_name = 'Compatibility'
        verbose_name_plural = 'Compatibilities'

    def __str__(self):
        return f'{self.count}'


class Wall(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    water = models.IntegerField()
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)
    compatibility = models.ManyToManyField(Compatibility)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Wall'
        verbose_name_plural = 'Walls'

    def __str__(self):
        return f'{self.user}: {self.food}'
