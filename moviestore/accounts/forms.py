from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe
from django.forms.utils import ErrorList
# Create your views here.

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))
    
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text=None
            self.fields[fieldname].widget.attrs.update(
                {'class':'form-control'}
            )