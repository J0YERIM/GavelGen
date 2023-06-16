from django import forms
from .models import Product, Report, Comment, Tag


class ProductForm(forms.ModelForm):
    tags = forms.CharField(label='Tags', max_length=100)

    class Meta:
        model = Product
        fields = ['title', 'content', 'starting_price', 'image']

    def save(self, commit=True):
        instance = super().save(commit=True)  # change commit to True here
        tags = self.cleaned_data.get('tags')
        if tags:
            tags = [tag.strip() for tag in tags.split(',')]
            for tag in tags:
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                instance.tags.add(tag_obj)
        if not commit:
            instance.save()
        return instance


class ProductUpdateForm(forms.ModelForm):
    tags = forms.CharField(label='Tags', max_length=100, required=False)

    class Meta:
        model = Product
        fields = ['title', 'content', 'image', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].initial = ', '.join(tag.name for tag in self.instance.tags.all())

    def save(self, commit=True):
        instance = super().save(commit=True)
        tags = self.cleaned_data.get('tags')
        instance.tags.clear()
        if tags:
            tags = [tag.strip() for tag in tags.split(',')]
            for tag in tags:
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                instance.tags.add(tag_obj)
        if not commit:
            instance.save()
        return instance


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'content', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

