from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    imageURL = models.URLField(blank=True)
    CATEGORIES = [
        ('ELECTRONICS', 'Electronics'),
        ('FASHION', 'Fashion'),
        ('HOME', 'Home'),
        ('TOYS', 'Toys'),
    ]
    category = models.CharField(max_length=64, choices=CATEGORIES, blank=True)
    active = models.BooleanField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    
    def __str__(self):
        return f"{self.bidder.username} - {self.price} on {self.listing.title}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    timestamp = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
    
    def __str__(self):
        return f"Comment by {self.commenter.username} on {self.listing.title}"