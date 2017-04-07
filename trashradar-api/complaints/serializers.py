from rest_framework import serializers

from complaints.models import Entity


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = (
            'id'
        )


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = (
            'id', 'name', 'twitter', 'phone'
        )
