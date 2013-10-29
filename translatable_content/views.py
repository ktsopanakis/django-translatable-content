from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.http import HttpResponseRedirect
from models import TranslationModel 
from django.conf import settings


def data(request,app, model, mid,field):
	languages = settings.LANGUAGES	
	if request.method == 'POST':
		for lan in languages:
			var =  unicode(request.POST[lan[0]])		
			word, created = TranslationModel.objects.get_or_create(app_name = app, model_name = model, modelfield_name = field, model_id = mid, language_code = lan[0] )
			word.translation_string = var
			word.save()	

	recs = []
	for lan in languages:
		rec ={}
		trans = TranslationModel.objects.filter(app_name = app, model_name = model, modelfield_name = field, model_id = mid, language_code = lan[0] )
		rec['language'] = lan
		if trans:
			rec['word'] = trans[0].translation_string
		else:
			rec['word'] = ''	
		recs.append(rec)	
	return render_to_response('translatable_content/translation_data.html', {'app':app, 'model':model, 'mid':mid, 'field':field, 'languages':languages,'recs':recs },context_instance=RequestContext(request))
