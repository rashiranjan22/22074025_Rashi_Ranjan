from django.urls import path
from . import views


urlpatterns = [
    path('short-urls/', views.short_url_list, name='short_url_list'),
    # url to view the list of urls
    path('', views.shorten_url, name='shorten_url'),
    path('<str:short_code>/', views.redirect_to_original_url, name='redirect_to_original_url'),

]
