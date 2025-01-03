from django.db import models

class BotUsers(models.Model):
    telegram_id = models.BigIntegerField(verbose_name="Telegram ID", unique=True)
    telegram_username = models.CharField(verbose_name="Telegram username", max_length=255, null=True, blank=True)
    full_name = models.CharField(verbose_name="Full name", max_length=255, null=True, blank=True)

    def __str__(self):
        if self.full_name:
            return self.full_name
        elif self.telegram_username:
            return self.telegram_username
        return str(self.telegram_id)

    class Meta:
        verbose_name = "Bot user"
        verbose_name_plural = "Bot users"
        ordering = ['telegram_id']