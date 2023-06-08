from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product, Tag, Comment, Heart, Report
from .forms import ProductForm, ProductUpdateForm, ReportForm, CommentForm
from django.http import Http404


def index(request):
    return render(request, 'index.html')


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_likes_this'] = self.object.hearts.filter(user=self.request.user).exists()
        context['liked_users'] = self.object.hearts.all()
        context['comment_form'] = CommentForm()
        return context


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
    context_object_name = 'product'

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


def toggle_heart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('products:product_detail', args=(product.id,)))

    heart, created = Heart.objects.get_or_create(user=request.user, product=product)
    if not created:
        heart.delete()

    return HttpResponseRedirect(reverse('products:product_detail', args=(product.id,)))


def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
    return redirect('products:product_detail', pk=product.pk)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'products/comment_form.html'
    context_object_name = 'comment'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False

    def get_success_url(self):
        return reverse('products:product_detail', args=[self.object.product.id])


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'products/comment_confirm_delete.html'
    context_object_name = 'comment'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False

    def get_success_url(self):
        return reverse('products:product_detail', args=[self.object.product.id])
