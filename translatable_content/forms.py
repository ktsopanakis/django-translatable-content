from django import forms
from django.utils.translation import ugettext_lazy as _
import re
from widgets import TranslatableTextWidget,TranslatableStringWidget


class TranslatableTextFormField(forms.Field):
   
    def __init__(self, *args, **kwargs):
        defaults = {'widget': TranslatableTextWidget}
        defaults.update(kwargs)
        super(TranslatableTextFormField, self).__init__(*args, **defaults)

    def clean(self, value):
        super(TranslatableTextFormField, self).clean(value)
        if value == '' and not self.required:
            return u''
        return value
        
        
class TranslatableStringFormField(forms.Field):
   
    def __init__(self, *args, **kwargs):
        defaults = {'widget': TranslatableStringWidget}
        defaults.update(kwargs)
        super(TranslatableStringFormField, self).__init__(*args, **defaults)

    def clean(self, value):
        super(TranslatableStringFormField, self).clean(value)
        if value == '' and not self.required:
            return u''
        return value    
