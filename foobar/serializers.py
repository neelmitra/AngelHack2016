from rest_framework import serializers
from .models import Tab,Items


class TabSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tab
        fields = ('owner', 'active', 'created', 'bar_name', 'items')


