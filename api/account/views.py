from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.views.generic.edit import FormView

class Signup(FormView):
    template_name = 'account/signup.html'
    form_class = TestForm
    success_url = '/login/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
    
    
    
def signin(request):

    form = TestForm()
    return render(request, 'account/signup.html', {'form': form})
