from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from Blog.models import Post
from django import forms


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


# Register your models here.
admin.site.register(Post)
admin.site.register(Blogtitle)
admin.site.register(Day)
admin.site.register(Department)
admin.site.register(Task)
admin.site.register(Customer)
admin.site.register(Region)
admin.site.register(Product)
admin.site.register(Calendar)