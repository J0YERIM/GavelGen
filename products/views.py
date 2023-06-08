from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Tag, Comment, Heart, Report
from .forms import ProductForm, ProductUpdateForm, ReportForm
from django.http import Http404


def index(request):
    return render(request, 'index.html')


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True
        else:
            return False

    def handle_no_permission(self):
        raise Http404()


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True
        else:
            return False

    def handle_no_permission(self):
        raise Http404()


class ReportListView(ListView):
    model = Report
    template_name = 'products/report_list.html'
    context_object_name = 'report_list'


class ReportDetailView(DetailView):
    model = Report
    template_name = 'products/report_detail.html'
    context_object_name = 'report'


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'products/report_form.html'
    success_url = reverse_lazy('products:report_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'products/report_form.html'
    success_url = reverse_lazy('products:report_list')

    def test_func(self):
        report = self.get_object()
        if self.request.user == report.user:
            return True
        return False

    def handle_no_permission(self):
        raise Http404()


class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Report
    template_name = 'products/report_confirm_delete.html'
    success_url = reverse_lazy('products:report_list')
    context_object_name = 'report'

    def test_func(self):
        report = self.get_object()
        if self.request.user == report.user:
            return True
        return False

    def handle_no_permission(self):
        raise Http404()
