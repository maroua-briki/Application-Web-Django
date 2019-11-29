from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm


# def user_login(request):
#     username = form.cleaned_data.get("username")
#     password = form.cleaned_data.get("password")
#     user = authenticate(username=username, password=password)
#     user = authenticate(user, password)
#     if user is not None:
#         login(request, user)
#
#         if user is Professorx:  # just a sudo code
#             return HttpResponseRedirect('indexUSER')
#         elif user is Studentx:
#             return HttpResponseRedirect('index')
#         else:
# may be here you want to redirect somewhere
# if not a customer or merchant
# def user_login(request):
#  return render(request,  'registration/login.html')








def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/exam/indexUSER')

    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
