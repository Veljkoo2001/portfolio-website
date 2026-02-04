from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Ime',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Vaše ime'
        })
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'vaš@email.com'
        })
    )
    
    message = forms.CharField(
        label='Poruka',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Vaša poruka...'
        })
    )
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError("Poruka mora imati najmanje 10 karaktera.")
        return message