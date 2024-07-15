from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
<<<<<<< HEAD
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
=======
from django.views import View
from django.views.generic import CreateView, ListView
>>>>>>> c67331d (Feat: Reescrevendo NewCarView como CreateView e testando.)

from cars.forms import CarModelForm
from cars.models import Car


class CarsListView(ListView):
  model = Car
  template_name = 'cars.html'
  context_object_name = 'cars'

  def get_queryset(self):
      cars = super().get_queryset().order_by('model')
      search = self.request.GET.get('search')

      if search:
        cars = cars.filter(model__icontains=search)
      return cars

<<<<<<< HEAD

=======
>>>>>>> c67331d (Feat: Reescrevendo NewCarView como CreateView e testando.)
class NewCarCreateView(CreateView):
  model = Car
  form = CarModelForm
  template_name = 'new_car.html'
  success_url = '/cars/'
  fields = '__all__'
<<<<<<< HEAD


class CarDetailView(DetailView):
  model = Car
  template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
  model = Car
  form_class = CarModelForm
  template_name = 'car_update.html'

  def get_success_url(self):
    return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarDeleteView(DeleteView):
  model = Car
  template_name = 'car_delete.html'
  success_url = '/cars/'
=======
>>>>>>> c67331d (Feat: Reescrevendo NewCarView como CreateView e testando.)
