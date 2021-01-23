from django.shortcuts import render, redirect
from accounts.models import User
from django.db import IntegrityError

# Create your views here.


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['email'], request.POST['password1'])
            except IntegrityError:
                error = 'This username is already taken.'
                return render(request, 'signupuser.html', {'error': error})
            else:
                user.save()
                return render(request, 'signupuser.html')
