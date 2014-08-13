from django.db import models

# Create your models here.
class Team(models.Model):
    the_fk = models.ForeignKey('auth.User', related_name='fk_related')
    the_m2m = models.ManyToManyField('auth.User', related_name='m2m_related')
