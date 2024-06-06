from django.contrib import admin
from newsApp.models import category,Post,contact
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
admin.site.register(category)
admin.site.register(Post,PostAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'phone', 'email', 'images', 'video')  # or 'video_url' for URLField
    search_fields = ('fname', 'lname', 'phone', 'email')

admin.site.register(contact, ContactAdmin)
