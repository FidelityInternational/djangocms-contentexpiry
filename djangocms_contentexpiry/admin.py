from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.core.urlresolvers import reverse

from rangefilter.filter import DateRangeFilter

from .models import ContentExpiry


class ExpiryChangeList(ChangeList):

    def url_for_result(self, result):
        app_label = result.content._meta.app_label
        model_name = result.content.__class__.__name__.lower()
        url_name = 'admin:{app}_{model}_change'.format(
            app=app_label, model=model_name)
        return reverse(url_name, args=(str(result.content.id)))


class ContentExpiryAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'content_type', 'activation_date', 'expiry_date',
        'modified_by', 'version_status')
    list_filter = (
        ('activation_date', DateRangeFilter),
        ('expiry_date', DateRangeFilter),
        'content_type',
        'modified_by',
    )

    def title(self, obj):
        return str(obj.content)

    def version_status(self, obj):
        return obj.content.versions.get().get_state_display()

    def get_changelist(self, request, **kwargs):
        return ExpiryChangeList


admin.site.register(ContentExpiry, ContentExpiryAdmin)
