import unittest

import address_parser


class TestAddressParser(unittest.TestCase):

    def setUp(self):
        self.address_parser = address_parser.AddressParser()

    def test_unit_number(self):
        unit_number_1 = self.address_parser.get_unit_number('4-567')
        self.assertTrue(unit_number_1)

        unit_number_2 = self.address_parser.get_unit_number('4')
        self.assertFalse(unit_number_2)
 
    def test_street_number(self):
        street_number = self.address_parser.get_street_number('567')
        self.assertTrue(street_number)

        with self.assertRaises(TypeError):
            self.address_parser.get_street_number(None)

    def test_street_name(self):
        street_name = self.address_parser.get_street_name('W8th', 'Ave')
        self.assertTrue(street_name)
        
        with self.assertRaises(TypeError):
            self.address_parser.get_street_name(None)

    def test_city_name(self):
        city = self.address_parser.get_city_name('Vancouver')
        self.assertTrue(city)

        with self.assertRaises(TypeError):
            self.address_parser.get_city_name('')

    def test_province_name(self):
        province = self.address_parser.get_province_name('BC')
        self.assertTrue(province)

        with self.assertRaises(TypeError):
            self.address_parser.get_province_name()

    def test_postal_code(self):
        postal_code = self.address_parser.get_postal_code('D4E5F6')
        self.assertTrue(postal_code)

        with self.assertRaises(TypeError):
            self.address_parser.get_postal_code()

    def test_parse_address(self):
        address = '123_Main_St_Vancouver_BC_A1B2C3'
        address_format = type({})
        new_address = self.address_parser.parse_address(address)
        self.addTypeEqualityFunc(address_format, new_address)


if __name__ == "__main__":
    unittest.main()
