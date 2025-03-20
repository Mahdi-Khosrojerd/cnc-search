from django.db import models
import random, re, string

# Create your models here.

class InformationModel(models.Model):
    sku = models.CharField(max_length=10, primary_key=True)
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=50)
    auther = models.CharField(max_length=55)
    controler = models.CharField(max_length=10)
    controler_model = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='media/%y/%m/%d', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_sku_code(self):
        while True:
            code = 'kpx-'
            code += ''.join(random.choices(string.digits, k=6))
            if not InformationModel.objects.filter(sku=code).exists():
                return code

    def persian_slugify(self, value):
        value = re.sub(r'[^\w\s-]', '', value).strip().lower()
        value = re.sub(r'[-\s]+', '-', value)
        return value
    
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku_code()
        if not self.slug:
            slugify = self.persian_slugify(self.title)
            sku_code = self.sku
            sku_code = str(sku_code)
            slugify += '-' + sku_code
            self.slug = slugify
        super().save(*args, **kwargs)