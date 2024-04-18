from django.contrib import admin
from .models import Service, Subscription, Fake_News, FAQ, Info, Message

class MessageAdmin (admin.ModelAdmin):
    
    list_display = ("date", "email",)
    search_fields = ['email']

admin.site.register(Service)
admin.site.register(Subscription)
admin.site.register(Fake_News)
admin.site.register(FAQ)
admin.site.register(Info)

admin.site.register(Message, MessageAdmin)