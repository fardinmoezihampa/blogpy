from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index_page'),
    path('contact/', views.ContactView.as_view(), name='contact_page'),
]
