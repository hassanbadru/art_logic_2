from rest_framework import serializers
from art_logic_app.models import UserAction

class UserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = ('operation', 'input', 'result')
        # fields = '__all__'
