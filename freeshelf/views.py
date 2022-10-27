from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Resource, Category
# from django.contrib.auth import login, authenticate
# from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
@login_required
def homepage(request):
    resources = Resource.objects.all()
    return render(request, 'freeshelf/homepage.html', {'resources': resources})

def resource_detail(request, pk):
    resource = Resource.objects.get(pk=pk)
    return render(request, 'freeshelf/resource_detail.html', {'resource': resource})

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'freeshelf/category_detail.html', {'category': category})

# def delete(request,pk):   
#         Details.objects.filter(id=pk).delete()
#         return redirect('retrieve')