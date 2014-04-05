from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)
    password = models.CharField('password', max_length=128)

class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'