from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('uid','uname', 'name', 'email', 'street','suite','city','zipcode')
       


