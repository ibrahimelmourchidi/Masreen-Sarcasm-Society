from django.contrib import admin
from .forms import *
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['id','title','user','time']
	list_display_links = ['title']
	list_editable = []
	list_filter = ['time','category','user']
	search_fields = ['title']
	class Meta:
		model = Post

admin.site.register(Post,PostAdmin)
admin.site.register(Followers)

class admin_messages_admin(admin.ModelAdmin):
	list_display = ['id','title','user','time']
	list_display_links = ['title']
	list_editable = []
	list_filter = ['time','user']
	search_fields = ['title']
	class Meta:
		model = admin_messages

admin.site.register(admin_messages,admin_messages_admin)

