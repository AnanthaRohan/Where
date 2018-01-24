from django.shortcuts import render,redirect
from .models import Places,Goods
from .forms import RegistrationForm,EditProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

# def home(request):
#     return redirect('home/home.html')

def about(request):
    return render(request,'home/about.html')

def editit(request):
    return render(request,'home/catalog.html')

def show_places(request):
    goods = Goods.objects.all()
    arg = {'goods':goods}
    return render(request,'home/home.html',arg)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/calatog')
    else:
        form = RegistrationForm()


    return render(request,'home/reg_form.html',{'form':form})


def search(request):
    query = request.GET.get("q")
    if query:
        items = Goods.objects.filter(Q(name__icontains=query)|Q(price__icontains=query)).distinct()

    return render(request,'home/home.html',{'items':items})

# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance = request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts/profile')
#     else:
#         form = EditProfileForm(instance = request.user)
#         args = {'form': form}
#         return render(request, 'accounts/edit_profile.html', args)