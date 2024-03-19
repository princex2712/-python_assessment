from rest_framework import serializers
from .models import todoApiModel

class todoApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoApiModel
        fields = "__all__"
        