from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from stereoit.djangoapps.tagcloud.models import Tag, TagCloud

class TagAdmin(admin.ModelAdmin):
	list_display = ['name','intensity','created','active']
	list_filter = ['intensity','active']
	search_fields = ['name']
	ordering = ['name','-created']
	prepopulated_fields = {'slug': ('name',)}

	fieldsets = (
		(None, {
			'fields': ('name','slug','intensity','active','description')
		}),
		('Wikipedia', {
			'classes': ('collapse',),
			'fields': ('wiki_powered','wiki_keyword')
		}),	
	)

class TagCloudAdmin(admin.ModelAdmin):
	list_display = ['name','list_of_tags','active','created']
	list_filter = ['active','created']
	search_fields = ['name','description']
	ordering = ['name']
	filter_horizontal = ['tags']	
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag,TagAdmin)
admin.site.register(TagCloud,TagCloudAdmin)
