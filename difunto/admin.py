from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Deudo, Difunto
# Register your models here.
admin.site.register(Deudo, SimpleHistoryAdmin)
admin.site.register(Difunto, SimpleHistoryAdmin)