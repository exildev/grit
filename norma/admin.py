<<<<<<< HEAD
from exile_ui.admin import admin_site
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
admin_site.register(Item, AdminItem)
admin_site.register(Formato, AdminFormato)
=======
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
>>>>>>> d4a43d94c0aa6b0b9855c268cd630ce06cd3af9c
