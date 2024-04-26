from django.db import models
class Post(models.Model):
    STATUS_CHOICES = (
        ('publish', 'Publish'),
        ('draft', 'Draft'),
        ('thrash', 'Thrash'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title