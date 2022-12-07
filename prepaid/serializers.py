from rest_framework import serializers
from .models import recharge

class registerserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=recharge
		fields=('Phonenumber', 'Serviceprovider', 'Plan')