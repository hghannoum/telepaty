
from django.db import models
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

class Contact(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	
	):

      
	lamp = models.BooleanField(verbose_name= True)
	temp= models.IntegerField(verbose_name= 0)
	currentTemp= models.IntegerField(verbose_name= 0)


