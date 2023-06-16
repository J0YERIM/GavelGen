from django.db import models
from users.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    starting_price = models.PositiveIntegerField()
    current_price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    participants = models.ManyToManyField(User, through='Participants', related_name='participated_products', related_query_name='participated_product')
    tags = models.ManyToManyField('Tag', related_name='products', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.current_price = self.starting_price
        super().save(*args, **kwargs)

    def participate_in_auction(self, price, user):
        if price is not None and price > self.current_price:
            self.current_price = price
            participant, created = Participants.objects.get_or_create(user=user, product=self,
                                                                      defaults={'current_price': price})
            if not created:
                participant.current_price = price
                participant.save()
            self.save()
            return True
        else:
            return False

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
        return f"Comment by {self.user.username} on {self.product.title}"


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
    image = models.ImageField(upload_to='products/', blank=True)
    admin_check = models.BooleanField(default=False)
    admin_response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')

    def __str__(self):
        return self.title


class Participants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participated_in_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='participants_records')
    current_price = models.PositiveIntegerField()

    def __str__(self):
        return f"User: {self.user}, Product: {self.product}, Current Price: {self.current_price}"






