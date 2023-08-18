from django import forms
from .models import User, Branch

Gender=[('male','Male'),
         ('female','Female')]
Account_Type = [ ('savings', 'Savings'),
    ('current', 'Current'),]

Materials = [
    ("cheque", "Cheque Book"),
    ("debit", "Debit Card"),
    ("credit", "Credit Card"),
]

class UserForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=Gender, widget=forms.RadioSelect())
    phone = forms.IntegerField()
    email= forms.EmailField()
    address=forms.CharField(max_length=200)
    account_type = forms.CharField(label='Account_type', widget=forms.Select(choices=Account_Type))
    materials_provided = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Materials,
    )


    class Meta:
        model = User
        fields = ('name', 'dob','age','gender','phone','email','address','district','branch',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.college.branch_set.order_by('name')