from django.contrib import admin
from .models import NumberList

class ShowAttribute(admin.ModelAdmin):
	list_display = ('number_list', 'algorithm')
	list_filter = ('algorithm',)
	search_fields = ('number_list', 'algorithm')
	exclude = ('file_field',)


admin.site.register(NumberList, ShowAttribute)
