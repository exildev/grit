from huella.admin import admin_site
from django.contrib import admin
from models import Norma, Item, Formato
from forms import NormaForm, ItemForm, FormatoForm


class ItemStack(admin.StackedInline):
	model = Item

class AdminNorma(admin.ModelAdmin):
	form = NormaForm
	model = Norma
	inlines = [ItemStack]
#end class

class AdminItem(admin.ModelAdmin):
	form = ItemForm
	model = Item
#end class

class AdminFormato(admin.ModelAdmin):
	form = FormatoForm
	model = Formato
#end class


admin_site.register(Norma, AdminNorma)
#admin_site.register(Item, AdminItem)
admin_site.register(Formato, AdminFormato)