
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView
from django.conf import settings
from django.http import JsonResponse
from .forms import CustomerDetailsForm, PropertyDetailsForm, EnquiryForm
from .helpers.providers import EnquiryProvider
from requests import post
import json

ODIP_API_ENDPOINT = "http://ec2-18-168-225-13.eu-west-2.compute.amazonaws.com/send-enquiry"
LTVCALCULATOR_API_ENDPOINT = "https://eposdjjkpd.execute-api.eu-west-2.amazonaws.com/dev/ltv-calculator-v1"

def customer_details(request):
    """ Customer Details form, first page of Enquiry """

    # Set initial response code for testing purposes
    response_code = 200

    if request.method == "POST":
        form = CustomerDetailsForm(request.POST, use_required_attribute=False)

        if form.is_valid():
            # Save to the session to be retreived later
            request.session["customer_details"] = form.cleaned_data
            return redirect("property_details")
        response_code = 400
    else:
        form = CustomerDetailsForm(use_required_attribute=False)

    context = {
        "form": form
    }
    return render(request, "customer_details.html", context, status=response_code)


def property_details(request):
    """ Property Details form, second page of Enquiry """

    # Set initial response code for testing purposes
    response_code = 400

    # Session check to verify journey integrity
    if not "customer_details" in request.session:
        return redirect("customer_details")

    if request.method =="POST":
        form = PropertyDetailsForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            property_details_data = form.cleaned_data
            customer_details_data = request.session["customer_details"]

            # Consolidate data from other pages to prep for db entry
            enquiry_data = EnquiryProvider()
            enquiry_data.add(property_details_data)
            enquiry_data.add(customer_details_data)

            # Convert all values to string before sending to API
            string_data = enquiry_data.get_list_with_string_values()

            # Post the data to the API
            response = post(ODIP_API_ENDPOINT, json = string_data)

            print(response.text)

            return redirect("thank_you")

    else:
        # Generate a new form page and set response code
        form = PropertyDetailsForm(use_required_attribute=False)
        response_code = 200

    context = {
        "form": form
    }
    return render(request, "property_details.html", context, status=response_code)


def calculate_ltv(request):

    loan_amount = int(request.GET.get('loanamount', None))
    property_value = int(request.GET.get('propertyvalue', None))

    property_data = {
        "loan_amount": loan_amount,
        "property_value": property_value
    }

    # Send data to the LTV Calculator API
    response = post(LTVCALCULATOR_API_ENDPOINT, json = property_data)

    # Map the response data to usable values
    ltv_data = response.json()
    ltv_value = ltv_data['body']['ltv_percentage']
    ltv_acceptable = ltv_data['body']['is_acceptable']

    # Check if the value is within specified acceptance criteria
    if ltv_acceptable:
        ltv_css = "ltv_acceptable"
        visibility_css = "hidden"
    else:
        ltv_css = "ltv_unacceptable"
        visibility_css = "visible"

    data = {
        'ltv': ltv_value,
        'ltv_css': ltv_css,
        'visibility_css': visibility_css,
    }
    return JsonResponse(data)

def thank_you(request):
    """ Page displayed on submission complete """

    # Session check to verify journey integrity
    if not "customer_details" in request.session:
        return redirect("customer_details")

    # Clean the session
    del request.session["customer_details"]

    return render(request, "thank_you.html")


def error_404(request, exception):
    """ Custom 404 error handler """
    return render(request, 'error/404.html', status=404)

def error_500(request):
    """ Custom 500 error handler """
    return render(request, 'error/500.html', status=500)
