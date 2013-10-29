# hello, django.contrib.staticfiles!



from django.db import models

class TranslationModel(models.Model):
	app_name = models.CharField( max_length=250)
	model_name = models.CharField( max_length=250)
	modelfield_name = models.CharField( max_length=250)
	model_id = models.IntegerField()
	language_code = models.CharField( max_length=5)
	translation_string = models.CharField(max_length=250, blank=True, null =True)
	translation_text = models.TextField(blank=True, null =True)


