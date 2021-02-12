from django.contrib import admin
from todo.models import ToDo

# Register your models here.


class Date(admin.ModelAdmin):
    readonly_fields = ('creation_date',)


admin.site.register(ToDo, Date)
