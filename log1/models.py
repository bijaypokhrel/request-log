from django.db import models

# Create your models here.


class RequestLog(models.Model):
    created_at = models.DateTimeField()
    response_at = models.DateTimeField()
    sec_response_time = models.IntegerField()
    url = models.TextField()
    request_headers = models.TextField()
    request_textfield = models.TextField()

    response_code = models.TextField()
    response_headers = models.TextField()
    response = models.TextField()

    def __str__(self):
        return self.url
