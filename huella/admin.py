# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.conf import settings # import the settings file
from django.contrib.auth.models import User, Group
import forms

class HuellaAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = 'Huella'

    # Text to put in each page's <h1>.
    site_header = 'Huella logística'

    # Text to put at the top of the admin index page.
    index_title = 'Software de administracion logística'

    # Path to a custom template that will be used by the admin site app index view.
#end def

class UserAdmin(admin.ModelAdmin):
    form = forms.UserForm

admin_site = HuellaAdminSite()
admin_site._registry = admin.site._registry
#admin_site.register(User, UserAdmin)
#admin_site.register(Group)