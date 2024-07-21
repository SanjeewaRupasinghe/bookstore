from django import forms

class ReviewForm(forms.Form):
    body=forms.CharField(widget=forms.Textarea(attrs={'class':'mt-5 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}))
    image=forms.ImageField(required=False)