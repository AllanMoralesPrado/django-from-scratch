from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import GenericModelForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

class GenericModelFormView(FormView):
    template_name = "add_genericdata.html"
    form_class = GenericModelForm

    def get_success_url(self) -> str:
        return reverse("addG")

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)


def generic_form_view(request):
    if request.method == "POST":
        form = GenericModelForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse('addG'))
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos.")
    else:
        form = GenericModelForm()
        
    return render(request=request, template_name="add_genericdata.html", context={"form": form})