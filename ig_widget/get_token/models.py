from django.db import models
from jsonfield import JSONField

# Create your models here.
class IGUser(models.Model):
    user_id = models.BigIntegerField()
    access_token = models.CharField(max_length=200)
    media_data = JSONField(null=True)
    media_timestamp = models.DateTimeField(null=True)
