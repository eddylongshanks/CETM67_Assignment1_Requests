""" Provider objects for building data sets """

class EnquiryProvider:
    """ Stores a dictionary list of form values to be retrieved later """

    def __init__(self):
        self.data = {}

    def add(self, data_to_add):
        """ Add a dictionary object to the existing list """

        if not isinstance(data_to_add, dict):
            raise TypeError("Object must be a Dictionary")

        self.data.update(data_to_add)

    def get_list(self):
        """ Return the list as a dictionary object """

        return self.data
    
    def get_list_with_string_values(self):
        """ Return the list as a dictionary object with string values"""
        working_list = self.data.items()

        list_with_string_values =  {str(key): str(value) for key, value in working_list}

        return list_with_string_values

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return "EnquiryProvider()"
