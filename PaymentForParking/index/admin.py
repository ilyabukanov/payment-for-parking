from django.contrib import admin
from .models import Parking,tickets,paidparking,paidseasontickets,users

class IndexAdmin(admin.ModelAdmin):
    list_display = ('adress','starttime','endtime','minimaltimeforpayment', 'price', 'numberofavailableseats', 'Абонементы')
    list_display_links = ('adress',)
    search_fields = ('adress',)

    def Абонементы(self, obj):
        return ', '.join(obj.tickets.values_list('nameseasontickets', flat=True))

class ticketsAdmin(admin.ModelAdmin):
    list_display = ('nameseasontickets','numberofdays', 'time', 'price')
    list_display_links = ('nameseasontickets',)
    search_fields = ('nameseasontickets',)

class paidparkingAdmin(admin.ModelAdmin):
        list_display = ('adress', 'carnumber', 'amountoftime', 'price', 'telephone','email','expirationdate','expirationtime','enddateandtime')
        list_display_links = ('adress',)
        search_fields = ('carnumber',)

class paidseasonticketsAdmin(admin.ModelAdmin):
        list_display = ('nametickets','carnumber','price','telephone','email','expirationdate','expirationtime','enddateandtime')
        list_display_links = ('nametickets',)
        search_fields = ('carnumber',)


class usersAdmin(admin.ModelAdmin):
    list_display = (
    'user_id','phonenumber')
    list_display_links = ('user_id',)
    search_fields = ('phonenumber',)

admin.site.register(Parking, IndexAdmin)
admin.site.register(tickets, ticketsAdmin)
admin.site.register(paidparking, paidparkingAdmin)
admin.site.register(paidseasontickets,paidseasonticketsAdmin)
admin.site.register(users,usersAdmin)
admin.site.site_title = 'Управление парковочными пространствами'
admin.site.site_header = 'Управление парковочными пространствами'
