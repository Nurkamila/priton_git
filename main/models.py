from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Person(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
