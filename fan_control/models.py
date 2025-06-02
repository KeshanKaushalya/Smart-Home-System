from django.db import models
from django.contrib.auth.models import User

class FanSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    speed = models.IntegerField(default=155)
    is_on = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Fan Settings"
