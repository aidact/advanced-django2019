from rest_framework import serializers

from core.models import Wall, Recommendation, Compatibility, Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class CompatibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Compatibility
        fields = '__all__'


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'


class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = '__all__'
        read_only_fields = ('user',)
