from django.db import models


class Carmodel(models.Model):
    title = models.CharField(max_length=50)
    birth_date = models.TextField(blank=True)
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Cars(models.Model):
    title = models.CharField(max_length=50, verbose_name='cars')
    color = models.TextField(blank=True)
    ot_kuchi = models.TextField(blank=True)
    year = models.TextField(blank=True)
    price = models.TextField(blank=True)
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    carmodel = models.ForeignKey(Carmodel, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_bool = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Cars"
        verbose_name_plural = "Cars"
        ordering = ['created_ed']