from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.views import generic
# from django.forms import inlineformset_factory

from apps.rooms.forms import RoomForm, BookingForm
from apps.rooms.models import Room, Booking


class RoomListView(generic.ListView):
    model = Room
    template_name = 'index.html'
    # context_object_name = "products"


class RoomCreateView(generic.CreateView):
    form_class = RoomForm
    model = Room
    success_url = 'index'
    template_name = 'room_create.html'


class RoomUpdateView(generic.UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'room.update.html'
    success_url = 'index'

    def form_valid(self, form):
        room = form.save(commit=False)
        room.save()
        return super().form_valid(form)


class RoomDetailView(generic.DetailView):
    model = Room
    template_name = 'room_detail.html'
    pk_url_kwarg = 'pk'


class RoomDeleteView(generic.DeleteView):
    model = Room
    pk_url_kwarg = 'pk'
    template_name = 'room_delete.html'
    success_url = 'index'


# class BookingListView(generic.ListView):
#     model = Booking
#     template_name = 'index.html'
    # context_object_name = "products"


class BookingCreateView(generic.CreateView):
    form_class = BookingForm
    model = Booking
    success_url = 'index'
    template_name = 'booking_create.html'


class BookingUpdateView(generic.UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking.update.html'
    success_url = 'index'

    def form_valid(self, form):
        room = form.save(commit=False)
        room.save()
        return super().form_valid(form)


class BookingDetailView(generic.DetailView):
    model = Booking
    template_name = 'booking_detail.html'
    pk_url_kwarg = 'pk'


class BookingDeleteView(generic.DeleteView):
    model = Booking
    pk_url_kwarg = 'pk'
    template_name = 'booking_delete.html'
    success_url = 'index'









    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['formset'] = inlineformset_factory(Room, Images, form=ImagesForm, extra=self.extra)(
    #             self.request.POST, self.request.FILES, instance=self.object
    #         )
    #     else:
    #         data['formset'] = inlineformset_factory(Room, Images, form=ImagesForm, extra=self.extra)()
    #     return data
    #
    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     formset = context['formset']
    #     print(formset)
    #     if formset.is_valid():
    #         self.object = formset.save()
    #         formset.instance = self.object
    #         formset.save()
    #     return super().form_valid(form)




