from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing, name="create"),
    path("categoryFilter", views.categoryFilter, name="categoryFilter"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("removeFromWatchlist/<int:id>", views.removeFromWatchlist,
         name="removeFromWatchlist"),
    path("addToWatchlist/<int:id>", views.addToWatchlist,
         name="addToWatchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("comment", views.listing, name="comment")
]
