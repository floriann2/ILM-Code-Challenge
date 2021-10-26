import unittest

import address_parser


class TestAddressParser(unittest.TestCase):

    def setUp(self):
        self.address_parser = address_parser.AddressParser()

    def test_unit_number(self):
        unit_number = self.address_parser.get_unit_number(4)
        self.assertTrue(unit_number)

        with self.assertRaises(TypeError):
            self.address_parser.get_unit_number('test')
 
    def test_street_number(self):
        street_number = self.address_parser.get_street_number(567)
        self.assertTrue(street_number)

        with self.assertRaises(TypeError):
            self.address_parser.get_street_number('567')

    def test_street_name(self):
        street_name = self.address_parser.get_street_name('W8th Ave')
        self.assertTrue(street_name)
        
        with self.assertRaises(TypeError):
            self.address_parser.get_street_name(1)

    def test_city_name(self):
        city = self.address_parser.get_city_name('Vancouver')
        self.assertTrue(city)

        with self.assertRaises(TypeError):
            self.address_parser.get_city_name(1)

    def test_province_name(self):
        province = self.address_parser.get_province_name('BC')
        self.assertTrue(province)

        with self.assertRaises(TypeError):
            self.address_parser.get_province_name(3)

    def test_postal_code(self):
        postal_code = self.address_parser.get_postal_code('D4E5F6')
        self.assertTrue(postal_code)

        with self.assertRaises(TypeError):
            self.address_parser.get_postal_code(4)

    def test_get_address(self):
        test = {}
        test_type = type(test)
        address = self.address_parser.get_address()

        self.addTypeEqualityFunc(test_type, address)

if __name__ == "__main__":
    unittest.main()
