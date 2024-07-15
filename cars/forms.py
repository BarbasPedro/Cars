from django import forms

from cars.models import Car


class CarModelForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = '__all__'

  def clean_value(self):
    value = self.cleaned_data.get('value')
    if value is not None and value < 20000:
      self.add_error('value', 'Valor mínimo do carro deve ser R$20.000,00')
    return value

  def clean_factory_year(self):
    year = self.cleaned_data.get('factory_year')
    if year is not None and year < 1975:
      self.add_error('factory_year', 'Não é possível cadastrar modelos fabricados antes de 1975')
    return year
