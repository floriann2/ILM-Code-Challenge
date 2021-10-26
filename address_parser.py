import collections


class AddressParser():
    """
    Parse a collection of strings and integers
    Form a dictionary for accepted values
    """

    def __init__(self):
        self.address = {}

        # To preserve the insertion order, 
        # we can use the following:
        # self.address = collections.OrderedDict({})

    def get_unit_number(self, unit):
        if (type(unit) is not int):
            raise TypeError('Incorrect argument type')
        self.address['unit'] = unit 

        return True
    
    def get_street_number(self, number):
        if (type(number) is not int):
            raise TypeError('Incorrect argument type')
        self.address['number'] = number

        return True

    def get_street_name(self, street):
        if (type(street) is not str):
            raise TypeError('Incorrect argument type')
        self.address['street'] = street

        return True

    def get_city_name(self, city):
        if (type(city) is not str):
            raise TypeError('Incorrect argument type')
        self.address['city'] = city

        return True

    def get_province_name(self, province):
        if (type(province) is not str):
            raise TypeError('Incorrect argument type')
        self.address['province'] = province

        return True

    def get_postal_code(self, postal_code):
        if (type(postal_code) is not str):
            raise TypeError('Incorrect argument type')
        self.address['postal_code'] = postal_code

        return True

    def get_address(self):
        if (not self.address.get('number')):
            return 'Please provide street number'
        elif (not self.address.get('street')):
            return 'Please provide street'
        elif (not self.address.get('city')):
            return 'Please provide city'
        elif (not self.address.get('province')):
            return 'Please provide province'
        
        return self.address


if __name__ == '__main__':
    address_parser = AddressParser()
    address_parser.get_unit_number(4)
    address_parser.get_street_number(567)
    address_parser.get_street_name('W8th Ave')
    address_parser.get_city_name('Vancouver')
    address_parser.get_province_name('BC')
    address_parser.get_postal_code('D4E5F6')
    address = address_parser.get_address()
    print ("ADDRESS: {}".format(address))
