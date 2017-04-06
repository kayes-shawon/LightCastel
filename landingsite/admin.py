from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from django import forms
from import_export import resources


class NewsletterSubscriberResource(resources.ModelResource):
    class Meta:
        model = NewsletterSubscriber
        fields = ('email')


class NewsletterModelAdmin(ImportExportModelAdmin):
    resource_class = NewsletterSubscriberResource



admin.site.register(MainSlider)
admin.site.register(ServicesSlider)
# admin.site.register(CaseStudiesSlider, admin_class=CaseStudiesAdmin)
admin.site.register(CaseStudiesSlider)
admin.site.register(InitiativeSlider)
admin.site.register(ClientsSlider)
admin.site.register(WordsOfEncouragementSlider)
admin.site.register(ManagementPeople)
admin.site.register(Advisor)
admin.site.register(Patron)
admin.site.register(OP_ED)
admin.site.register(Magazine)
admin.site.register(Interview)
admin.site.register(NewsletterSubscriber, admin_class=NewsletterModelAdmin)
