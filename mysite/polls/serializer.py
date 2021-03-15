from rest_framework import serializers
from .models import *

class SudentSerializer(serializers.ModelSerializer):

    class Meta:
        model= Student
        fields = ['name','roll','address']