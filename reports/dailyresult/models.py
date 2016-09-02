from __future__ import unicode_literals
from profiles.models import Profile
from django.db import models


class ReportField(models.Model):
    calls = models.IntegerField()
    meetings = models.IntegerField()
    contracts = models.IntegerField()
    prepayment = models.IntegerField()
    standart_shop = models.IntegerField()
    user = models.ForeignKey(Profile)

    def __unicode__(self):
        return self.user.username
