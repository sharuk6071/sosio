from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    if request.method == 'EXPENSES':
        form = UserCreationForm(request.EXPENSES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('$')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html',{'form': form})
