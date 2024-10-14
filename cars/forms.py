from django import forms
from cars.models import Brand, Car


class CarForm(forms.Form):      # hardeest way - not used
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    model = forms.CharField(max_length=200)
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save() # DB save
        return car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data['value'] # value = self.cleaned_data.get('value')
        if value < 20000:
            #raise forms.ValidationError('Invalid value')
            self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000,00')
        return value
    def clean_factory_year(self):
        year = self.cleaned_data['factory_year']
        if year < 1975:
            self.add_error('factory_year', 'Ano de fabricação deve ser maior que 1975')
        return year 