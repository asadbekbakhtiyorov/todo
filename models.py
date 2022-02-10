from django.db import models
from django.contrib.auth.models import User


from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    Ch=(
        ('new','new'),
        ('done','done')
    )
    title = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=10,choices=Ch)
    date = models.DateTimeField(default=timezone.now)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    def str(self):
        return self.title