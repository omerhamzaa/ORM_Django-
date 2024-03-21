from django.contrib import admin

from django.contrib import admin
from .models import Student, Teacher, Management, ITDepartment, BBIT


from django.contrib import admin
from .models import BBIT, Student


# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'get_bbit')
#
#     def BBIT_list(self, obj):
#         return ", ".join([BBIT.some_field for BBIT in obj.BBIT_set.all()])
#
#     get_BBIT.short_description = 'BBIT'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = Student.Display_fields






#
#
#
# class AdminBBIT(admin.ModelAdmin):
#     search_fields = ['name']


# Register your models here.
# admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Management)
admin.site.register(ITDepartment)
admin.site.register(BBIT)


