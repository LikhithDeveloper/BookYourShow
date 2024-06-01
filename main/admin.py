from django.contrib import admin
from .models import Book,BookedSeat,Slot_Register,Show,Days,Timeings,Total

# Register your models here.
admin.site.register(Book)
admin.site.register(BookedSeat)
admin.site.register(Slot_Register)
admin.site.register(Show)
admin.site.register(Days)
admin.site.register(Timeings)
admin.site.register(Total)
