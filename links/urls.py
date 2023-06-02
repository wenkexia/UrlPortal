from django.urls import path
from . import views

urlpatterns = [
    path(r'<short_code>', views.redirect_to_original), ]
