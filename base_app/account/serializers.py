from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import *
from dashboard.models import Dashboard


class UserSerializer(serializers.ModelSerializer):
    dashboard_id = serializers.SerializerMethodField('get_dashboard_id')
    
    def get_dashboard_id(self, instance):
        try:
            result = Dashboard.objects.get(account__user__username=str(instance)).id
        except:
            result = ''
        return result
    
    class Meta:
        model = User
        fields = ('username', 'dashboard_id',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    dashboard_id = serializers.SerializerMethodField('get_dashboard_id')
    
    def get_dashboard_id(self, instance):
        try:
            result = Dashboard.objects.get(account__user__username=str(instance)).id
        except:
            result = ''
        return result
    
    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'dashboard_id')


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('pk', 'name')
