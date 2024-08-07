from django import forms

class ListingForm(forms.Form):
    title = forms.CharField(label="Listing title", max_length=100)
    description = forms.CharField(widget=forms.Textarea, label="Description")
    starting_bid = forms.DecimalField(label="Starting Bid")
    imageURL = forms.URLField(label="Image URL", required=False)
    category = forms.ChoiceField(
        choices=[
            ('ELECTRONICS', 'Electronics'),
            ('FASHION', 'Fashion'),
            ('HOME', 'Home'),
            ('TOYS', 'Toys'),
        ],
        label="Category",
        required=False
    )