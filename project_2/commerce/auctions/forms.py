from django import forms

class ListingForm(forms.Form):
    title = forms.CharField(label="Listing title", max_length=100)