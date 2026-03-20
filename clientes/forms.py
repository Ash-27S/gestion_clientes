from django import forms
from .models import Customer, Order


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("El numero de telefono solo debe tener numeros.")
        return phone


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    
    def clean_total_amount(self):
        total_amount = self.cleaned_data.get('total_amount')
        if total_amount <= 0:
            raise forms.ValidationError("El monto total debe ser mayor a cero.")
        return total_amount
