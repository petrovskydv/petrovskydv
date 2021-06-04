from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from main.models import Category, Person, Tag, PersonalItem, Car, Service, ArchivedPost, Profile


class FlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Person)
# admin.site.register(Post)
admin.site.register(ArchivedPost)
admin.site.register(Tag)
admin.site.register(PersonalItem)
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Profile)
