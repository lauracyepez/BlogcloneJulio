from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
# This URL pattern maps the 'signup/' path to the SignUpView, which handles user registration.
# The name 'signup' can be used to refer to this URL in templates or redirects.