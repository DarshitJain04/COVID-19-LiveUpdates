import requests
from django.shortcuts import render
from .models import Corona
from .forms import CovidForm

def index(request):

	url = 'https://covid-193.p.rapidapi.com/statistics'

	headers = {
	'x-rapidapi-host': "covid-193.p.rapidapi.com",
	'x-rapidapi-key': "62d2ddb3eemsh595ff2d85b2be4ep1856fdjsn5f3dae8c2f5d"
	}

	error_message = ''
	message = ''
	message_type = ''

	if request.method == 'POST':
		form = CovidForm(request.POST)

		if form.is_valid():
			new_country = form.cleaned_data['country']
			count = Corona.objects.filter(country=new_country).count()
			if count == 0:
					form.save()
			else:
				error_message = 'Countnry already exists in the data!'

		if error_message :
			message = error_message
			message_type = 'danger'
		else :
			message = 'Country added successfully!'
			message_type = 'success'

	form = CovidForm()

	countries = Corona.objects.all().order_by('-id')

	current_status = []

	for country in countries:

		response = requests.request("GET", url, headers=headers, params={"country":country.country}).json() #response = requests.get(url, headers=headers) 

		country_status = {
			'country' : country.country ,
			'cases' : response['response'][0]['cases']['total'] ,
			'deaths' : response['response'][0]['deaths']['total'] ,
			'recovered' : response['response'][0]['cases']['recovered'], 
		}

		current_status.append(country_status)

	context = {'current_status':current_status, 'form':form, 'message':message, 'message_type':message_type}

	return render(request,'status/home.html',context)
