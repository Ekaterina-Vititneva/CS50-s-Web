from django import forms

class ListingForm(forms.Form):
    title = forms.CharField(label="Listing title", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="Description")
    bid = forms.DecimalField(label="Starting Bid", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    imageURL = forms.URLField(label="Image URL", required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(
        choices=[
            ('ELECTRONICS', 'Electronics'),
            ('FASHION', 'Fashion'),
            ('HOME', 'Home'),
            ('TOYS', 'Toys'),
        ],
        label="Category",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )