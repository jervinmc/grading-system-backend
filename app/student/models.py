from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Student(models.Model):
    firstname=models.CharField(_('firstname'),max_length=255,blank=True,null=True)
    lastname=models.CharField(_('lastname'),max_length=255,blank=True,null=True)
    middlename=models.CharField(_('middlename'),max_length=255,blank=True,null=True)
    section=models.CharField(_('section'),max_length=255,blank=True,null=True)
    address=models.CharField(_('address'),max_length=255,blank=True,null=True)
    kinder_level=models.CharField(_('kinder_level'),max_length=255,blank=True,null=True)
    date_from=models.DateTimeField(_('date_from'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
