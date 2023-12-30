from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=25)
    surname = serializers.CharField(max_length=25)
    age = serializers.IntegerField()

    def validate(self, attrs):
        if attrs['age'] <= 0:
            raise ValidationError('User cannot have negative age!')

        return super().validate(attrs)
