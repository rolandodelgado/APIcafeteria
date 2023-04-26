from rest_framework import serializers
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer): 
    group_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'group_name']

    def get_group_name(self, obj):
        group = Group.objects.filter(user=obj).first()
        return group.name if group else None
    