from django.contrib import admin
from .models import User,Event,Contact,BookEvent
# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(BookEvent)