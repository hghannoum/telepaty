from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class ContactSerializer(serializers.ModelSerializer):

	temp = int()
	lamp = bool()
	
	class Meta:
		model = models.Contact
		fields = (
			'lamp',
			'temp',
			'currentTemp'
		)