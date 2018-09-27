from django import forms

from .models import Category, Style, Country


class DrinkForm(forms.Form):

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),
                                                required=False)
    styles = forms.ModelMultipleChoiceField(queryset=Style.objects.all(),
                                            required=False)
    countries = forms.ModelMultipleChoiceField(queryset=Country.objects.all(),
                                               required=False)
    organic = forms.BooleanField(required=False,
                                 help_text='Uncheked means indifferent.')
    length = forms.IntegerField(label='Number of drinks to show',
                                max_value=1000, min_value=1,
                                initial=10)


class FuzzyDrinkForm(forms.Form):

    q = forms.CharField(
        label='Search text', max_length=100, required=False,
        help_text='Ex: "Öl", "Öl Vin", "IPA", "vodka"... Leave empty to search all.'
    )
    length = forms.IntegerField(label='Number of drinks to show',
                                max_value=1000, min_value=1,
                                initial=10)
