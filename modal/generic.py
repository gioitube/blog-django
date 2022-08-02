from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .mixins import PassRequestMixin, DeleteMessageMixin, LoginAjaxMixin
from django.contrib.auth.views import LoginView


class BSModalLoginView(LoginAjaxMixin, SuccessMessageMixin, LoginView):
    pass


class BSModalFormView(PassRequestMixin, generic.FormView):
    pass


class BSModalCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    pass


class BSModalUpdateView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    pass


class BSModalReadView(generic.DetailView):
    pass


class BSModalDeleteView(DeleteMessageMixin, generic.DeleteView):
    pass
