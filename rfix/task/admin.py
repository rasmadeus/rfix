from django.contrib import admin
from rfix.task.models import State
from rfix.task.models import Priority


admin.site.register(State)
admin.site.register(Priority)
