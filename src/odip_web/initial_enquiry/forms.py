""" form classes for the enquiry creator """

from django.core.validators import RegexValidator
from django import forms
from django.utils import timezone
from django.conf import settings


class CustomerDetailsForm(forms.Form):
    """ Page 1 of the Initial Enquiry journey """

    # Custom Regex validation for telephone number
    phone_regex = RegexValidator(regex=r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$',
        message="Provide a valid UK Phone Number.")

    first_name = forms.CharField(max_length=40, label="First Name")
    last_name = forms.CharField(max_length=40, label="Last Name")
    building = forms.CharField(max_length=50, required=False, label="Building and Street")
    street = forms.CharField(max_length=50, required=False, label="Street")
    town = forms.CharField(max_length=50, required=False, label="Town")
    county = forms.CharField(max_length=50, required=False, label="County")
    postcode = forms.CharField(max_length=10, required=False, label="Postcode")
    telephone_number = forms.CharField(validators=[phone_regex], max_length=17, label="Telephone Number", widget=forms.TextInput(attrs={'type': 'tel'}))
    email_address = forms.EmailField(max_length=254, required=False, label="Email Address", widget=forms.TextInput(attrs={'type': 'email'}))

    MORNING = 'M'
    EARLY_AFTERNOON = 'EA'
    LATE_AFTERNOON = 'LA'
    SATURDAY = 'S'
    PREFERRED_TIME_TO_CONTACT_CHOICES = [
        (MORNING, '9am - 12pm (Mon-Fri)'),
        (EARLY_AFTERNOON, '12pm - 3pm (Mon-Fri)'),
        (LATE_AFTERNOON, '3pm - 5pm (Mon-Fri)'),
        (SATURDAY, '9am - 2pm (Sat)'),
    ]
    preferred_time_to_contact = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=PREFERRED_TIME_TO_CONTACT_CHOICES,
        label="Preferred Time to Call"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Override default "required" validation message to mention the field name
        for field in self.fields.values():
            field.error_messages = {'required' : f'{field.label} is required'}


class PropertyDetailsForm(forms.Form):
    """ Page 2 of the Initial Enquiry journey """

    ltv_value = forms.FloatField(max_value=100, min_value=0, label="LTV")
    annual_income = forms.IntegerField(label="Annual Income", widget=forms.TextInput(attrs={'type': 'number'}))    
    loan_amount = forms.IntegerField(label="Loan Amount", widget=forms.TextInput(attrs={'type': 'number'}))
    property_value = forms.IntegerField(label="Property Value", widget=forms.TextInput(attrs={'type': 'number'}))

    NEW_HOUSE = 'NH'
    REMORTGAGE = 'RM'
    MORTGAGE_TYPE_CHOICES = [
        (NEW_HOUSE, 'New House'),
        (REMORTGAGE, 'Remortgage'),
    ]
    mortgage_type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=MORTGAGE_TYPE_CHOICES,
        label="Mortgage Type"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Override default "required" validation message to mention the field name
        for field in self.fields.values():
            field.error_messages = {'required' : f'{field.label} is required'}

    def clean_ltv_value(self):
        """ Validates LTV against MAX_LTV """
        max_ltv = 80
        ltv = self.cleaned_data['ltv_value']

        if ltv > max_ltv:
            raise forms.ValidationError("LTV is too high, consider reducing your Loan Amount")
        return ltv


class EnquiryForm(forms.Form):
    """ Final full enquiry model """

    # class Meta:
    #     model = Enquiry
    #     fields = ['first_name', 'last_name', 'building', 'street', 'town', 'county', 'postcode', 'telephone_number', 'email', 'preferred_time_to_contact',
    #               'annual_income', 'loan_amount', 'property_value', 'mortgage_type' ]

    date_created = forms.DateField(initial=timezone.now, label="Date Created")
    has_been_contacted = forms.BooleanField(initial=False, label="Has been Contacted?")

