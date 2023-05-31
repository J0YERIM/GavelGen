from django.db import models
from users.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    starting_price = models.PositiveIntegerField()
    current_price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    participants = models.ManyToManyField(User, related_name='participated_products')
    tags = models.ManyToManyField('Tag', related_name='products')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content


class Heart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hearts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='hearts')

    def __str__(self):
        return f'사용자: {self.user}, 상품: {self.product}'


class Report(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='reports/')
    admin_check = models.BooleanField(default=False)
    admin_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')

    def __str__(self):
        return self.title
