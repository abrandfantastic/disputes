from django.contrib import admin
from .models import Contacts
# Register your models here.


class ContactsAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'from_email', 'subject', 'added')
	list_display_links = ('name')
	search_fields = ('name', 'from_email')
	list_per_page = 25



admin.site.register(Contacts, ContactsAdmin)



