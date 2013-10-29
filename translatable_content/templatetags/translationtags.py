# coding: utf-8
from portal.models import *
from django.db.models import get_model
from django import template
from datetime import date, timedelta
from django.template.loader import get_template
from django.template import Context
from translatable_content.models import TranslationModel
from django.utils.translation import get_language

register = template.Library()

@register.filter(name='translation')
def translation(obj, field):
    
    model_name = obj.__class__.__name__.lower()
    app_name = obj._meta.app_label
    lan = get_language()
    if lan >2:
    	lan =lan[0:2]
    
    #mm = TranslationModel.objects.get(app_name = app_name, model_name = model_name,modelfield_name = field, model_id = obj.id,language_code = lan)
    try:
    	if obj._meta.get_field(field).get_internal_type() == 'TranslatableStringField':
    		mm = TranslationModel.objects.get(app_name = app_name, model_name = model_name,modelfield_name = field, model_id = obj.id,language_code = lan).translation_string
    	else:
    		mm = TranslationModel.objects.get(app_name = app_name, model_name = model_name,modelfield_name = field, model_id = obj.id,language_code = lan).translation_text
    	if mm == '' or mm == None:
    		mm = obj.__dict__[field]			
    except:
    	mm = obj.__dict__[field]
    return mm
    
   
