from django.db import models


class QouteCategory(models.Model):
    name            = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Qoute(models.Model):
    qoute           = models.TextField()
    author          = models.CharField(max_length=50)
    qoute_category  = models.ForeignKey('QouteCategory', on_delete = models.CASCADE)


    def __str__(self):
        # return self.qoute
        if len(self.qoute) > 50:
            return self.qoute[:50] + '...'

        return self.qoute       # it just looks nice to have 50 character in first look

    class Meta:
        ordering = ['-id']      # makes the last added qoutes appears in first
