from django.contrib.auth.forms import UserCreationForm
from django import forms 

class UserForm(UserCreationForm):

    class Meta:
        fields = ["username", "password1", "password2"]
    #end
    
    def save(self, commit):
        obj = super(UserForm, self).save(commit)
        obj.is_staff = True
        obj.save()
        return obj
    #end def
#end class