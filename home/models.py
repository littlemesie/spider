# models.py
from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=64)