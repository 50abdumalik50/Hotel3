from django.shortcuts import render

from django.views import generic

from apps.restaurants.forms import RestaurantForm, HoursForm, RestaurantMenuForm
from apps.restaurants.models import Restaurant, Hour, Restaurant_Menu


class RestaurantListView(generic.ListView):
    model = Restaurant
    template_name = 'restaurant.html'
    # context_object_name = "products"


class HoursListView(generic.ListView):
    model = Hour
    template_name = 'restaurant.hours.html'
    success_url = 'restaurant'


class RestaurantMenuListView(generic.ListView):
    model = Restaurant_Menu
    template_name = 'restaurant_menu'
    success_url = 'restaurant'


class RestaurantMenuDetailView(generic.DetailView):
    model = Restaurant_Menu
    template_name = 'restaurant_menu.detail.html'
    pk_url_kwarg = 'pk'




# class RestaurantCreateView(generic.CreateView):
#     form_class = RestaurantForm
#     model = Restaurant
#     success_url = 'index'
#     template_name = 'restaurant_create.html'
#
#
# class RestaurantUpdateView(generic.UpdateView):
#     model = Restaurant
#     form_class = RestaurantForm
#     template_name = 'restaurant.update.html'
#     success_url = 'index'
#
#     def form_valid(self, form):
#         room = form.save(commit=False)
#         room.save()
#         return super().form_valid(form)
#
#
# class RestaurantDetailView(generic.DetailView):
#     model = Restaurant
#     template_name = 'restaurant_detail.html'
#     pk_url_kwarg = 'pk'
#
#
# class RestaurantDeleteView(generic.DeleteView):
#     model = Restaurant
#     pk_url_kwarg = 'pk'
#     template_name = 'restaurant_delete.html'
#     success_url = 'index'
