from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe



class TranslatableTextWidget(forms.TextInput):

    def render(self, name, value, attrs=None):
        rendered = super(TranslatableTextWidget, self).render(name, value, attrs)
        return rendered + mark_safe(
            u"""<div id="translate_text_%(name)s" class="translate_text"></div>
            <a id=%(name)s class="trans" href="#">link here for translating the value: %(value)s</a> 
            """ % {'name': name, 'value':value, 'attrs':attrs}
        )

    class Media:
#        css = {
#        	'translate.css',
#        
#        )
        js = ('http://code.jquery.com/jquery-1.9.1.js','http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js','/static/content_translation/translate.js')


