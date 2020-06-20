"""poke_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from api_app.api import pokemonList, movesList, pokemonDetails,movesDetails

# from api_app.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/pokemon_list$',pokemonList.as_view(),name = 'Pokemon_List'),
    url(r'^api/pokemon_list/(?P<pk>\d+)/$',pokemonDetails.as_view(),name = 'Pokemon_Details'),
    url(r'^api/moves_list$',movesList.as_view(),name = 'Moves_List'),
    url(r'^api/moves_list/(?P<pk>[a-zA-Z ]+)$',movesDetails.as_view(),name = 'Moves_Details')
    # path('',landing)
]
