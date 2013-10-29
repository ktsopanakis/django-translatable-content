from django.db import models
from forms import TranslatableTextFormField, TranslatableStringFormField


class TranslatableTextField(models.Field):
    """
    TranslatableTextField
    """

    __metaclass__ = models.SubfieldBase
    _south_introspects = True

    description = "A translatable text object"

    def to_python(self, value):
        return value

    def get_prep_value(self, value):
        if not (value and value.strip()) and self.null:
            return None
        return value

#    def value_to_string(self, value):
#        if value:
#            return value.strip() or None

    def formfield(self, *args, **kwargs):
        defaults = {'form_class': TranslatableTextFormField}
        defaults.update(kwargs)
        return super(TranslatableTextField, self).formfield(*args, **defaults)

    def db_type(self, connection):	
        return 'longtext'




class TranslatableStringField(models.Field):
    """
    TranslatableStringField
    """

    __metaclass__ = models.SubfieldBase
    _south_introspects = True

    description = "A translatable string object"

    def to_python(self, value):
        # assert value[0] == "#"
        # assert re.match('#[0-9a-fA-F]{6}', value)
        return value

    def get_prep_value(self, value):
        if not (value and value.strip()) and self.null:
            return None
        return value

    def value_to_string(self, value):
        if value:
            return value.strip() or None

    def formfield(self, *args, **kwargs):
        defaults = {'form_class': TranslatableStringFormField}
        defaults.update(kwargs)
        return super(TranslatableStringField, self).formfield(*args, **defaults)

    def db_type(self, connection):	
        return 'char(%s)' % self.max_length
        

        
