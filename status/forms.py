from django.forms import ModelForm
from .models import Corona

class CovidForm(ModelForm):
	class Meta:
		model = Corona
		fields = ['country']

