from django.contrib import admin

# Register your models here.
from .models import Member, Group


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name','birth_date','gender','grade','email','club','zekken','jacket','joined')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Member, MemberAdmin)
admin.site.register(Group, GroupAdmin)
