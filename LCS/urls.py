from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from LCS import views
from django.conf import settings

urlpatterns = [
    
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("joinus", views.joinus, name='joinus'),
    path("contact", views.contact_form, name='contact'),
    path("review", views.review_form, name='review'),
    path("donate", views.donate, name='donate'),
    path("volunteer", views.volunteer_form, name='volunteer'),
    path("sponsorship", views.sponsorship_form, name='sponsorship'),
    path("login", views.handel_login, name='handel_login'),
    path("signup/", views.handel_signup, name='handel_login'),
    path("logout", views.handel_logout, name='handel_logout'),
    path("success", views.success, name='success'),
    path("cancel", views.cancel, name='cancel'),
    path('checkout', views.checkout, name='checkout'),
    path('create_checkout_session', views.create_checkout_session, name='create_checkout_session'),
    path('send_email/', views.send_email_to_volunteers, name='send_email'),
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('up-events/', views.upcoming_events, name='up-events'),
    path('error/', views.error_page, name='error_page'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<int:event_id>/', views.event_detail, name='event_detail'),
]


    
    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)