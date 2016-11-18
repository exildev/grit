from django import forms
import models
from django.template.loader import render_to_string

class TextWidget(forms.Widget):

    def __init__(self):
        super(TextWidget, self).__init__()
    # end def

    def render(self, name, value, attrs=None):
        return render_to_string("riesgo/text.html", {'name': name, 'value': value or ''})
    # end def

    #class Media:
    #    js = ('epc/js/chart.js',)
    # end class

# end class

