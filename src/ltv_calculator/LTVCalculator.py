""" LTV Calculator v1.0 """

class LTVCalculator():
    """ Calculates the LTV value when given Loan Amount and Property Value """

    def __init__(self, loan_amount, property_value, max_ltv):
        self.max_ltv = max_ltv
        self.loan_amount = loan_amount
        self.property_value = property_value

    def get_value(self):
        """ Calculate ratio of loan to value, then cap at 1.0 (≡100%) """

        try:
            ltv_result = min(float(self.loan_amount) / float(self.property_value), 1.0)
        except Exception as ex:
            raise ValueError("Invalid values were provided, you must provide numbers") from ex

        ltv_percentage = ltv_result * 100

        ltv_formatted = float(f'{ltv_percentage:.1f}')

        return ltv_formatted

    def is_acceptable(self):
        """ Return boolean dependent on acceptability within specified MAX_LTV value """

        ltv_value = self.get_value()

        try:
            max_acceptable_ltv = float(self.max_ltv)

            # Apply floor and ceiling values (0 and 100)
            max_ltv = min(100, max(0, max_acceptable_ltv))
        except Exception as ex:
            raise ValueError("MAX_LTV setting contains an invalid value, must be a number between 1 and 100") from ex

        if ltv_value <= max_ltv:
            return True

        return False

    def __str__(self):
        return f'LTV: { self.get_value() }'

    def __repr__(self):
        return "LTVCalculator()"
