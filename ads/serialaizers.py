from rest_framework import serializers

from ads.models import Selection


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field="name")

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'
