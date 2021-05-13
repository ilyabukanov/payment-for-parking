from django.urls import path
from . import views
import debug_toolbar
from django.conf import settings
from django.urls import include, path

from .views import ParkingView


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
    #БОТ
    path('botparking/', views.botparking),
    path('save_phonenumber/', views.save_phonenumber),
]


