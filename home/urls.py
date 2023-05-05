from django.urls import path
from . import views
from home.views import aboutView,indexView,contactView,loginView

urlpatterns = [
    path("", indexView.as_view(), name='index'),
    path("index", indexView.as_view(), name='index'),  # django'ya göstermesi gereken web sayfası tanımlanır.
    path("about", aboutView.as_view(), name='about'),
    path("contact", contactView.as_view(), name='contact'),
    path("login", loginView.as_view(), name='login'),
    # iki parametre alır birincisi route ikincisi ise ilgili olan view'i yazar
    # ek olarak kısayol isminide alır

]
