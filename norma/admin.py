from exileui.admin import exileui
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


exileui.register(Norma, AdminNorma)
exileui.register(Item, AdminItem)
exileui.register(Formato, AdminFormato)
