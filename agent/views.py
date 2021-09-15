from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def profile_information(request) :
    
    return render(request,'agent/home_agent.html')



