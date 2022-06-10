from rest_framework import serializers


class RequestSerializer(serializers.Serializer):
    user = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)
    request = serializers.CharField()
    response = serializers.CharField()
