from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d")

    class Meta:
        ordering= ('name',)

    def __str__(self):
        return self.name
