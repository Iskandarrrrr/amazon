from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150,
                             unique=True,
                             verbose_name='Name of category')

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=150,
                             unique=True,
                             verbose_name='Name of product')
    content = models.TextField(verbose_name='Description')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='Images')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated date')
    publish = models.BooleanField(default=True, verbose_name='Publish')
    views = models.IntegerField(default=0, verbose_name='Quantity views')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    video = models.CharField(max_length=500, verbose_name='Video', default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return 'https://img.freepik.com/premium-vector/no-photo-available-vector-icon-default-image-symbol-picture-coming-soon-web-site-mobile-app_87543-18055.jpg'


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
