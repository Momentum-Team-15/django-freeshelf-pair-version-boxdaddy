"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# brings in admin structure from django library
from django.contrib import admin
from django.urls import path, include
# imports views from freeshelf folder
from freeshelf import views


#sets up URL structure for the site 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.homepage, name="home",),
    path('resource/<int:pk>/', views.resource_detail, name="resource_detail"),
    path('category/<slug:slug>', views.category_detail, name="category_detail"),
    # path('resource/<int:pk>', views.delete, name="delete"),
]
