from django import forms


class PriceFilter(forms.Form):
    min_price = forms.IntegerField(label="Цена от ", required=False)
    max_price = forms.IntegerField(label="Цена до ", required=False)

