from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe



class TranslatableTextWidget(forms.Textarea):

	def render(self, name, value, attrs=None):
		rendered = super(TranslatableTextWidget, self).render(name, value, attrs)
		
		if value == None:
	   		return rendered
	   		
		else:
			return rendered + mark_safe(u"""<a id=%(name)s class="transtext" href="#"><img src="/static/translatable_content/images/transicon.png" style="width: 48px;margin-left: 16px;"></a> """ % {'name': name, 'value':value} )

	
	class Media:
#		css = {
#			'translate.css',
#		
#		)
		js = ('http://code.jquery.com/jquery-1.9.1.js','http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js','/static/translatable_content/translate.js')



class TranslatableStringWidget(forms.TextInput):

	def render(self, name, value, attrs=None):
		rendered = super(TranslatableStringWidget, self).render(name, value, attrs)
		
		if value == None:
	   		return rendered
	   		
		else:
			return rendered + mark_safe(u"""<a id=%(name)s class="transstr" href="#"><img src="/static/translatable_content/images/transicon.png" style="width: 48px;margin-left: 16px;"></a> """ % {'name': name, 'value':value} )

	
	class Media:
		js = ('http://code.jquery.com/jquery-1.9.1.js','http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js','/static/translatable_content/translate.js')

