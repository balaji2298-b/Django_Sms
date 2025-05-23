from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from django.http import HttpResponse

@csrf_exempt
def sms_form(request):
	if request.method == "POST":
		to = request.POST.get('to')
		message_body = request.POST.get('message')

		account_sid = 'AC25b3adf5a44976b55fb2512723e6adac'
		auth_token = '1a7bea279473685ce21a8bc71f3feedf'
		from_number = '+12705136113'


		try:
			client = Client(account_sid, auth_token)
			message = client.messages.create(
				body=message_body,
				from_=from_number,
				to=to
			)
			return HttpResponse("SMS sent successfully!")
		except Exception as e:
			return HttpResponse(f"Failed to send SMS: {e}")

	return render(request,'index.html')

def index(request):
	return render(request,"index.html")

