from django.contrib import admin

from .models import employee,area,burial

class areaAdmin(admin.ModelAdmin):

    list_display = ('number', 'title', 'employee_support')
    list_display_links = ('title',)

class employeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'middlename','birth')
    list_display_links = ('surname',)   

class burialAdmin(admin.ModelAdmin):
    list_display = ('area_number','number_burial','surname_person','birth_person','death_person')
    list_display_links = ('number_burial',)

admin.site.register(area,areaAdmin)
admin.site.register(employee,employeeAdmin)
admin.site.register(burial,burialAdmin)
