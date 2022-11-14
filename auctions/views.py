from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing


def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    watchlistTrue = request.user in listingData.watchlist.all()
    return render(request, "auctions/listing.html", {
        "listing": listingData,
        "watchlistTrue": watchlistTrue
    })


def removeFromWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse(listing, args=(id,)))


def addToWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse(listing, args=(id,)))


def index(request):
    listings = Listing.objects.filter(activeListing=True)
    return render(request, "auctions/index.html", {
        "listings": listings,
        "categorys": Category.objects.all()
    })


def categoryFilter(request):
    if request.method == "POST":
        if request.POST["category"] == "fb":
            return HttpResponseRedirect(reverse(index))
        else:
            catFilter = request.POST["category"]
            category = Category.objects.get(categoryName=catFilter)
            listings = Listing.objects.filter(
                activeListing=True, category=category)
            return render(request, "auctions/index.html", {
                "listings": listings,
                "categorys": Category.objects.all()
            })


def createListing(request):
    if request.method == "GET":
        return render(request, "auctions/create.html", {
            # Sending the categories to the view
            "categorys": Category.objects.all()
        })
    else:
        # get data from the form
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.POST["image"]
        price = request.POST["price"]

        # As category is an object, we need to get all it's values from the category input
        category = request.POST["category"]
        categoryData = Category.objects.get(categoryName=category)

        # Getting the current user
        user = request.user

        # Adding to db
        newListing = Listing(
            title=title,
            description=description,
            image=image,
            price=float(price),
            category=categoryData,
            owner=user
        )
        newListing.save()
        # redirect to index
        return HttpResponseRedirect(reverse(index))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
