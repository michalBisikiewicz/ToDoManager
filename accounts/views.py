from django.shortcuts import render, redirect
from accounts.models import User
from django.db import IntegrityError
from django.contrib.auth.password_validation import validate_password # do validacji hasła
from  django.core.exceptions import ValidationError # potrzebne do walidacji hasła
from django.core.mail import EmailMessage
from accounts.forms import SignUpForm
from verify_email.email_handler import send_verification_email

# Create your views here.


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupuser.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['email'], request.POST['password1'])
            except IntegrityError:
                error = 'This username is already taken.'
                return render(request, 'accounts/signupuser.html', {'error': error})
            try:
                validate_password(request.POST['password1'], user=user)
            except ValidationError as e:
                #password_error = list(e)[0]
                return render(request, 'accounts/signupuser.html', {'password_error': e})
            else:
                """
                sprawdzenie wysyłania maila
                msg = EmailMessage('New account', "You've created a new account.", 'ToDo Manager<mikegorlomi@gmail.com>',
                                  [request.POST['email']])
                msg.send()
                """
                inactive_user = send_verification_email(request, form=SignUpForm(request.POST))
                #powyższa funkcja już zapisuje usera
                # user.save()
                return redirect('home')
        else:
            not_match_error = "Password didn't match. Try again!"
            return render(request, 'accounts/signupuser.html', {'not_match_error': not_match_error})
