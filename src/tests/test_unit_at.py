import unittest
from oxrse_unit_conv.units import at, mol


class TestAtoms(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(at.si_unit.matches(mol))

    def test_basic_conversion(self):
        self.assertEqual(at.to_si((6.022 * (10 ** 23))), 1)
        self.assertAlmostEqual(mol.to_unit(1, at), (6.022 * (10 ** 23)), delta=70000000)


if __name__ == '__main__':
    unittest.main()
