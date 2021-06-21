from rest_framework import serializers

from .models import Coach


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ["id", "last_name", "first_name", "categeory"]
