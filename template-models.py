from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


price = models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
package_name=models.CharField(_('package_name'),max_length=255,blank=True,null=True)
date_from=models.DateTimeField(_('date_from'), null=False,blank=False,default=timezone.now)