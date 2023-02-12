from django.forms import ModelForm
from .models import posts


class createPost(ModelForm):
        class Meta:
                model = posts 
                fields = ['title','description','img']

        def __init__(self, *args, **kwargs):
                super(createPost, self).__init__(*args,**kwargs)
                self.fields['img'].required = False