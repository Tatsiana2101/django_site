from django.shortcuts import render
from .models import Evening, Sale, Shoes, Veil, Accessories, EveningDress, Wedding
from django.views.generic import DetailView
from .forms import PriceFilter


def eveningDress(request):
    ev = EveningDress.objects.all()
    return render(request, 'product/wed_1.html', {'ev': ev})


def wed_1(request):
    wedding = Wedding.objects.all()
    form = PriceFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            wedding = wedding.filter(price__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"]:
            wedding = wedding.filter(price__lte=form.cleaned_data["max_price"])
    return render(request, 'product/wed_1.html', {'wedding': wedding, "form": form})


def sale_2(request):
    sale = Sale.objects.all()
    form = PriceFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            sale = sale.filter(price__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"]:
            sale = sale.filter(price__lte=form.cleaned_data["max_price"])
    return render(request, 'product/sale_2.html', {'sale': sale, "form": form})


def even_3(request):
    evening = EveningDress.objects.all()
    form = PriceFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            evening = evening.filter(price__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"]:
            evening = evening.filter(price__lte=form.cleaned_data["max_price"])
    return render(request, 'product/even_3.html', {'evening': evening, "form": form})


def shoes_4(request):
    shoes = Shoes.objects.all()
    form = PriceFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            shoes = shoes.filter(price__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"]:
            shoes = shoes.filter(price__lte=form.cleaned_data["max_price"])
    return render(request, 'product/shoes_4.html', {'shoes': shoes, "form": form})


def veil_5(request):
    veil = Veil.objects.all()
    form = PriceFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            veil = veil.filter(price__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"]:
            veil = veil.filter(price__lte=form.cleaned_data["max_price"])
    return render(request, 'product/veil_5.html', {'veil': veil, "form": form})


def access_6(request):
    accessories = Accessories.objects.all()
    form = PriceFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            accessories = accessories.filter(price__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"]:
            accessories = accessories.filter(price__lte=form.cleaned_data["max_price"])
    return render(request, 'product/access_6.html', {'accessories': accessories, "form": form})


class OwnPages1(DetailView):
    model = Wedding
    template_name = 'product/ownPage.html'
    context_object_name = 'positions'


class OwnPages2(DetailView):
    model = Sale
    template_name = 'product/saleOwnPage.html'
    context_object_name = 'sale'


class OwnPages3(DetailView):
    model = Evening
    template_name = 'product/ownPage3.html'
    context_object_name = 'evening'


class OwnPages4(DetailView):
    model = Shoes
    template_name = 'product/ownPage4.html'
    context_object_name = 'shoes'


class OwnPages5(DetailView):
    model = Veil
    template_name = 'product/ownPage5.html'
    context_object_name = 'veil'


class OwnPages6(DetailView):
    model = Accessories
    template_name = 'product/ownPage6.html'
    context_object_name = 'accessories'


def type_filter(request, pk):
    shoes = Shoes.objects.all()
    if pk == 1:
        now = 0 + pk
        shoes = shoes.filter(type=now)

    elif pk == 2:
        now = 0 + pk
        shoes = shoes.filter(type=now)

    elif pk == 3:
        now = 0 + pk
        shoes = shoes.filter(type=now)

    elif pk == 4:
        now = 0 + pk
        shoes = shoes.filter(type=now)
    form = PriceFilter()
    return render(request, 'product/shoes_4.html', {'shoes': shoes, 'form': form})


def type_filter5(request, pk):
    veil = Veil.objects.all()
    if pk == 1:
        now = 0 + pk
        veil = veil.filter(type=now)

    elif pk == 2:
        now = 0 + pk
        veil = veil.filter(type=now)

    return render(request, 'product/veil_5.html', {'veil': veil})


def type_filter6(request, pk):
    accessories = Accessories.objects.all()
    if pk == 1:
        now = 0 + pk
        accessories = accessories.filter(type=now)

    elif pk == 2:
        now = 0 + pk
        accessories = accessories.filter(type=now)

    return render(request, 'product/access_6.html', {'accessories': accessories})


def type_filter3(request, pk):
    evening = EveningDress.objects.all()
    if pk == 1:
        now = 0 + pk
        evening = evening.filter(type=now)

    elif pk == 2:
        now = 0 + pk
        evening = evening.filter(type=now)

    elif pk == 3:
        now = 0 + pk
        evening = evening.filter(type=now)

    elif pk == 4:
        now = 0 + pk
        evening = evening.filter(type=now)

    return render(request, 'product/even_3.html', {'evening': evening})


def type_filter1(request, pk):
    wedding = Wedding.objects.all()
    if pk == 1:
        now = 0 + pk
        wedding = wedding.filter(type=now)

    elif pk == 2:
        now = 0 + pk
        wedding = wedding.filter(type=now)

    elif pk == 3:
        now = 0 + pk
        wedding = wedding.filter(type=now)

    elif pk == 4:
        now = 0 + pk
        wedding = wedding.filter(type=now)

    return render(request, 'product/wed_1.html', {'wedding': wedding})

