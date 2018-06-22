from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Name',
        }
    ))

    phone = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Phone Number',
        }
    ))

    from_email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Email Address',
        }
    ))

    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Subject',
        }
    ))

    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your message',
        }
    ))
