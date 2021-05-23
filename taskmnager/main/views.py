from django.shortcuts import render, redirect
from .models import Task
from product.models import Wedding
from .forms import TaskForm
from django.views.generic import ListView



def index(request):
    tasks = Task.objects.order_by('-id')[:100]
    form = TaskForm()
    context = {
        'form':form
    }
    return render(request, 'main/index.html', {'tasks': tasks})


def wedding(request):
    return render(request, 'main/wedding-dresses.html')


def sale(request):
    return render(request, 'main/sale.html')


def evening(request):
    return render(request, 'main/evening-dresses.html')


def shoes(request):
    return render(request, 'main/shoes.html')


def veil(request):
    return render(request, 'main/veil.html')


def accessories(request):
    return render(request, 'main/accessories.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def about(request):
    return render(request, 'main/about.html')


def search(request):
    return render(request, 'main/search.html')


def delivery(request):
    return render(request, 'main/delivery.html')


def refund(request):
    return render(request, 'main/refund.html')


def bank(request):
    return render(request, 'main/bank.html')


def ourBride1(request):
    return render(request, 'main/ourBride1.html')


def ourBride2(request):
    return render(request, 'main/ourBride2.html')


def ourBride3(request):
    return render(request, 'main/ourBride3.html')


def ourBride4(request):
    return render(request, 'main/ourBride4.html')


def ourBride5(request):
    return render(request, 'main/ourBride5.html')


def ourBride6(request):
    return render(request, 'main/ourBride6.html')


def ourBride7(request):
    return render(request, 'main/ourBride7.html')


def ourBride8(request):
    return render(request, 'main/ourBride8.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


class Search(ListView):
    paginate_by = 3

    def get_ordering(self):
        return Wedding.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_queryset(*args, **kwargs)
        context["q"] = f'{self.request.GET.get("q")}&'
        return context