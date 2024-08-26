from django.db.models import fields
from rest_framework import serializers
from .models import *


class SerializeToken(serializers.ModelSerializer):
  class Meta:
    model = Token
    fields=('token',)

class SerializeGoods(serializers.ModelSerializer):

  class Meta:
      model = Good
      fields = '__all__'
  
  def validate_amount(self, value):
      if value <= 0:
          raise serializers.ValidationError("Amount must be more than 0")
      return value
  
  def validate_price(self, value):
      if value <= 0:
          raise serializers.ValidationError("Price must be more than 0")
      return value
