from django.urls import path
from . import views
import debug_toolbar
from django.conf import settings
from django.urls import include, path

from .views import ParkingView
from django.views.generic import RedirectView
urlpatterns = [
    path('', views.index, name='home'),
    path('authorization',views.enter, name='authorization'),
    path('pricingplans',views.pricingplans, name='pricingplans'),
    path('payment',views.payment, name='payment'),
    path('paymentrickets',views.paymenttickets, name='paymenttickets'),
    path('valuesubstitution', views.valuesubstitution, name='valuesubstitution'),
    path('seasonticketprice', views.seasonticketprice, name='seasonticketprice'),
    path('personalaccount', views.personalaccount, name='personalaccount'),
    path('exit', views.exit, name='exit'),
    path('session', views.session, name='session'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/statistics', views.view_func),
    path('admin/date', views.statistics),
    path('parking/', ParkingView.as_view()),
    path('admin/print', views.print_func),
    path('admin/video_images_from_cameras', views.video_images_from_cameras),
    path('admin/video',views.video),
    path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    #БОТ
    path('botparking/', views.botparking),
    path('save_phonenumber/', views.save_phonenumber),
    path('minimum_time_for_payment/',views.minimum_time_for_payment),
    path('adress_parking/', views.adress_parking),
    path('season_tickets/',views.season_tickets),
    path('price_tickets/', views.price_tickets),
    path('number_of_days_tickets/', views.number_of_days_tickets),
    path('save_payment_parking/', views.save_payment_parking),
    path('start_time_end_time/',views.start_time_end_time),
    path('save_payment_tickets/',views.save_payment_tickets)
]



