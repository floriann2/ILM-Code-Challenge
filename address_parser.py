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
        if '-' in unit:
            value = unit.split('-')
            self.address['unit'] = int(value[0])

            return True
        else:
            # No optional unit number provided
            return False
    
    def get_street_number(self, number):
        if not number:
            raise TypeError('No street number provided')
        if '-' in number:
            value = number.split('-')
            self.address['number'] = int(value[1])
        else:
            self.address['number'] = number

        return True

    def get_street_name(self, specific, generic):
        if not specific or not generic:
            raise TypeError('No street name provided')
        street = (specific + ' ' + generic)
        self.address['street'] = street

        return True

    def get_city_name(self, city):
        if not city:
            raise TypeError('No city provided')
        self.address['city'] = city

        return True

    def get_province_name(self, province):
        if not province:
            raise TypeError('No province provided')
        self.address['province'] = province

        return True

    def get_postal_code(self, postal_code):
        if not postal_code:
            raise TypeError('No postal code provided')
        self.address['postal_code'] = postal_code

        return True

    def parse_address(self, address):
        split_address = address.split('_')
        self.get_unit_number(split_address[0])
        self.get_street_number(split_address[0])
        self.get_street_name(split_address[1], split_address[2])
        self.get_city_name(split_address[3])
        self.get_province_name(split_address[4])
        self.get_postal_code(split_address[5])
        print ("Address: {}".format(self.address))

        return self.address


if __name__ == '__main__':
    address_parser = AddressParser()
    # address = '123_Main_St_Vancouver_BC_A1B2C3'
    address = '4-567_W8th_Ave_Vancouver_BC_D4E5F6'
    address_parser.parse_address(address)
