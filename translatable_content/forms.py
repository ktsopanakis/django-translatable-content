from django import forms
from django.utils.translation import ugettext_lazy as _
import re
from widgets import TranslatableTextWidget


class TranslatableTextFormField(forms.Field):
   
    def __init__(self, *args, **kwargs):
        defaults = {'widget': TranslatableTextWidget}
        defaults.update(kwargs)
        super(TranslatableTextFormField, self).__init__(*args, **defaults)

    def clean(self, value):
        super(TranslatableTextFormField, self).clean(value)
        if value == '' and not self.required:
            return u''

        #if not re.match('#[0-9a-fA-F]{6}', value):
        #    raise forms.ValidationError(self.error_messages['invalid'])

        return value
        
        

#class TranslatableTextFormField(forms.Field):
#	
#	def __init__(self, *args, **kwargs):
#		self.translation = translation
#		
#		defaults = {'widget':TranslatableTextWidget}
#		defaults.update(kwargs)
#		super(TranslatableTextFormField, self).__init__(*args, **defaults)
#	
#	def clean(self, value):
#		super(TranslatableTextFormField, self).clean(value)
#		if value == '' and not self.required:
#			return u''
#		return value
#        
        
        
        
