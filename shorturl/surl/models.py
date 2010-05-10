from django.db import models
import datetime

# Create your models here.

class URL(models.Model):
  full_url = models.CharField(max_length=500)
  pub_date = models.DateTimeField('date published')
  short_url = models.CharField(max_length=6)

  def __unicode__(self):
    return self.short_url + ' -> ' + self.full_url

  def was_published_today(self):
    return self.pub_date.date() == datetime.date.today()
  was_published_today.short_description = 'Published today?'
