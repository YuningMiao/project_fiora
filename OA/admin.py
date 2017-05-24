# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from OA import models
# Register your models here.
admin.site.register(models.generic)
admin.site.register(models.consultencyService)
admin.site.register(models.customerService)
admin.site.register(models.userinfo)
admin.site.site_header = "OfferComes Assessment System" 
