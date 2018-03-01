from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def basic_validator(self, postdata):
        errors = {}
        if len(postdata['first_name']) < 2:
            errors["first_name"] = 'First name is not long enough.'
        if len(postdata['last_name']) < 2:
            errors["last_name"] = 'Last name if not long enough.'
        if len(postdata['email']) < 1:
            errors["email"] = "Email cannot be blank!"
        elif not EMAIL_REGEX.match(postdata['email']):
            errors["email"] = "Invalid Email Address!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()