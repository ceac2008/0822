from django.contrib import admin
from django_web2.models import  Person,Contact,Tag
# Register your models here.

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )

admin.site.register(Contact,ContactAdmin)
#admin.site.register(Tag)#如果一个就可以只写Person
admin.site.register(Person)

