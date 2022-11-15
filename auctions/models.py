from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName


class Listing(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=280, default="")
    image = models.CharField(max_length=2090, default="")
    price = models.FloatField(default=0)
    activeListing = models.BooleanField(default=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(
        User, blank=True, null=True, related_name="watchlist")
    latestBidder = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="latestBidder")

    def __str__(self):
        return self.title


class Bid(models.Model):
    bid = models.FloatField(default=0)
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listinBid")
    bidder = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="userBid")

    def __str__(self):
        return f"{self.bid} by {self.bidder} on {self.listing}"


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="userComment")
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingComment")
    comment = models.CharField(max_length=280, default="")

    def __str__(self):
        return f"{self.author}: {self.comment}"
