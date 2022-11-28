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


class Grades(models.Model):
    user_id = models.IntegerField(_('user_id'),default=0)
    subject_id = models.IntegerField(_('subject_id'),default=0)
    score = models.IntegerField(_('score'),default=0)
    grade_type=models.CharField(_('grade_type'),max_length=255,blank=True,null=True)
    description=models.CharField(_('description'),max_length=255,blank=True,null=True)
    date_submitted=models.DateTimeField(_('date_submitted'), null=False,blank=False,default=timezone.now)
    class Meta:
        ordering = ["-id"]
