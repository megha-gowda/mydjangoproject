from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('sports/',views.sports,name='sports'),
    path('politics/',views.politics,name='politics'),
    path('bollywood/',views.bollywood,name='bollywood'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('signup_user/',views.signup_user,name='signup_user'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout/',views.logout,name='logout'),
    path('validate_otp',views.validate_otp,name='validate_otp'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('query/',views.query,name='query'),
    path('book_event/<int:pk1>/<int:pk2>/',views.book_event,name='book_event'),
    path('mybooking/',views.mybooking,name='mybooking'),
    path('cancel_booking/<int:pk>/',views.cancel_booking,name='cancel_booking'),
]