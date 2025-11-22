from django import forms

class BookSearchForm(forms.Form):
    """
    Form for searching books safely.
    Validates input to prevent unsafe queries.
    """
    query = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Search books'})
    )
