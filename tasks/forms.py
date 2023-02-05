from django.forms import ModelForm
from .models import posts


class createPost(ModelForm):
        class Meta:
                model = posts 
                fields = '__all__'