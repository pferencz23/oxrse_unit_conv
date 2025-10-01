import unittest
from oxrse_unit_conv.units import fahrenheit, kelvin 


class TestFahrenheit(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(fahrenheit.si_unit.matches(kelvin))

    def test_basic_conversion(self):
        self.assertEqual(fahrenheit.to_si(-459.67), 0)
        self.assertAlmostEqual(fahrenheit.to_unit(10, kelvin), 260.928, 3)



if __name__ == '__main__':
    unittest.main()