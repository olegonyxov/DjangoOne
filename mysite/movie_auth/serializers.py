from rest_framework import serializers




class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=50)
class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=100)
    dob = serializers.DateField()