from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Media, Hashtag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['is_active']
        fields = '__all__'
        widgets = {
            'user_account': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }

from django.core.validators import validate_image_file_extension
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True
forms.ImageField
class MultipleFileField(forms.FileField):
    default_validators = [validate_image_file_extension]
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        exclude = ['is_active', 'alt', 'user_post']
        fields = '__all__'
        # widgets = {
        #     'user_media': MultipleFileInput #forms.ClearableFileInput()
        # }
        field_classes = {
            'user_media': MultipleFileField
        }

class HashtagForm(forms.ModelForm):
    tag = forms.SlugField(required=False)

    class Meta:
        model = Hashtag
        fields = ['tag']
        widgets ={
            'tag': forms.TextInput(attrs={'class': 'form-control'})
        }

    def is_valid(self) -> bool:
        data = self.data['tag']
        result = super().is_valid()
        if Hashtag.objects.filter(tag = data).exists():
            result = True
            self.cleaned_data['tag'] = data
        return result


# MediaFormSet = forms.inlineformset_factory(Post, Media, form=MediaForm, extra=2, can_delete=True, fk_name='user_post')
# HashtagFormSet = forms.inlineformset_factory(Post, Hashtag, form=HashtagForm, extra=1, can_delete=True,)

# MediaFormSet = forms.formset_factory(MediaForm, extra=2)
