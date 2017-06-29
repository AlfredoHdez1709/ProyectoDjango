from django.shortcuts import render

# Create your views here.
from django.views.generic import View

# Create your views here.
class main(View):
	def get(self,request):
		template_name = 'home/index.html'
		return render(request,template_name)