django-translatable-content
===========================

Created by DotByDot (www.dotbydot.gr)

Beta Version - Not to be used for production till it goes version 1.0

Follow the steps below:
0. Install the package 

1. Open your settings.py:
	
	a. add into the INSTALLED_APPS section the following line:
	'translatable_content',
	before the application that you will use it 
	
	b. define the LANGUAGES tuple that you want your strings and textareas to be translated into.
	example:
	LANGUAGES = (
		('en', 'English'),
		('el', 'Greek'),
	)

and run python manage.py syncdb.
2. Add to your urls.py the following:
	(r'^translatable_content/', include('translatable_content.urls')),

3. Now you can use the custom modelfields below into your Models:
	
	from translatable_content.fields import TranslatableTextField, TranslatableStringField
	
	a. my_textfield = TranslatableTextField(blank=True, null=True)
	b. my_charfield = TranslatableStringField(blank=True, null=True,max_length=250)

4. Using the fields into the template
	a. Add {% load translationtags %} on top of the html file
	b. Use this custom filter so that you can print the value of your field in the correct language
	{{ obj|translation:"my_textfield" }}
	The above shall return the my_textfield field value of object translated into the current language
