from django.forms import ModelForm
from .models import posts, materiales
from django import forms

"""  materiales = forms.ModelChoiceField(
               queryset = materiales.objects.all().order_by('id'), label = "Materiales",widget=forms.CheckboxSelectMultiple
        ) """
class createPost(ModelForm):

       

        class Meta:
                model = posts 
                fields = ['title','description','img']

        def __init__(self, *args, **kwargs):
                super(createPost, self).__init__(*args,**kwargs)
                self.fields['img'].required = False

                self.fields['title'].widget.attrs.update({'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'})
                self.fields['description'].widget.attrs.update({'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'})
                self.fields['img'].widget.attrs.update({'class':'block w-80 text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none ','id':'file_input','type':'file'})

