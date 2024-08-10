from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import User, Listing, Bid, Comment

from .forms import ListingForm, BidForm


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


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

def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = Listing(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                bid=form.cleaned_data['bid'],
                imageURL=form.cleaned_data['imageURL'],
                category=form.cleaned_data['category'],
                created_by=request.user, 
                last_modifed_by=request.user
            )
            listing.save()
            return redirect("index")
    else:
        form = ListingForm()
    
    return render(request, "auctions/create_listing.html", {"form": form})

def listing(request, title):
    listing = get_object_or_404(Listing, title=title)
    user = request.user

    if request.method == "POST":
        if 'add_to_watchlist' in request.POST or 'remove_from_watchlist' in request.POST:
            # Handle watchlist modification
            if 'add_to_watchlist' in request.POST:
                if listing not in user.watchlist.all():
                    user.watchlist.add(listing)
            elif 'remove_from_watchlist' in request.POST:
                if listing in user.watchlist.all():
                    user.watchlist.remove(listing)
            return redirect('listing', title=listing.title)

        elif 'bid' in request.POST:
            # Handle bid submission
            form = BidForm(request.POST)
            if form.is_valid():
                bid_amount = form.cleaned_data['bid']
                if bid_amount > listing.bid:
                    listing.bid = bid_amount
                    listing.last_modified_by = request.user
                    listing.save()

                    new_bid = Bid(
                        price=bid_amount,
                        bidder=request.user,
                        listing=listing,
                    )
                    new_bid.save()

                    messages.success(request, "Your bid was placed successfully!")
                    return redirect('listing', title=listing.title)
                else:
                    messages.error(request, "Your bid must be higher than the current bid.", extra_tags='danger')
            else:
                messages.error(request, "Please enter a valid bid.", extra_tags='danger')

    else:
        form = BidForm()

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "form": form,
    })



def categories(request):
    return render(request, "auctions/categories.html", {
        "listings": Listing.objects.all()
    })

def watchlist(request):
    user = request.user
    return render(request, "auctions/watchlist.html", {
        "listings": user.watchlist.all()
    })

def add_comment(request):
    return render(request, "auctions/listing.html")