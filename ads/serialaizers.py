from rest_framework import serializers

from ads.models import Selection


class NotTrueValidator:
    def __call__(self, value):
        if value:
            raise serializers.ValidationError("New ad can not be published")


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


class AdCreateSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[NotTrueValidator()])

    class Meta:
        model = Selection
        fields = '__all__'
