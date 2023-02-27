from django.forms import ModelForm
from .models import posts, materiales
from django import forms

"""  materiales = forms.ModelChoiceField(
               queryset = materiales.objects.all().order_by('id'), label = "Materiales",widget=forms.CheckboxSelectMultiple
        ) """
class createPost(ModelForm):

       

        class Meta:
                model = posts 
                fields = ['title','description','email_field','presupuesto_prom','contacto','img']

        def __init__(self, *args, **kwargs):
                super(createPost, self).__init__(*args,**kwargs)
                self.fields['img'].required = False

                self.fields['title'].widget.attrs.update({'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'})
                self.fields['description'].widget.attrs.update({'class':'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'})
                self.fields['img'].widget.attrs.update({'class':'block w-80 text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none ','id':'file_input','type':'file'})
                self.fields['email_field'].widget.attrs.update({'class':'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'})
                self.fields['presupuesto_prom'].widget.attrs.update({'class':'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'})
                self.fields['contacto'].widget.attrs.update({'class':'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'})