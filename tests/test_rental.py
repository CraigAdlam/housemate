# test_rental.py module

import unittest
import sys
import io
import random

from src.housemate_app.my_property.property import Property
from src.housemate_app.my_property.rental import (
    Rental,
    RentalCondo,
    RentalTownHome,
    RentalDuplex,
    RentalBungalow,
    RentalTwoStory,
    RentalMansion,
    gen_rental,
    rental_recommendation
)


class TestRental(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        random.seed(355)

        # Initializing test instances
        self.r_condo_inst = RentalCondo()
        self.r_townhome_inst = RentalTownHome()
        self.r_duplex_inst = RentalDuplex()
        self.r_bungalow_inst = RentalBungalow()
        self.r_twostory = RentalTwoStory()
        self.r_mansion = RentalMansion()
        self.rental_known = Rental(1504, 4, 3, 3500, 314)
        self.rental2_known = Rental(799, 1, 2, 1800, 121)
        self.rental3_known = Rental(3114, 5, 5, 6000, 446)
        self.rental_gen_result = gen_rental(3, RentalBungalow)

        # Saving original stdout
        # Redirect stdout to a StringIO object
        self.original_stdout = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout

    @classmethod
    def tearDownClass(cls):
        pass

    def test_rental_condo(self):
        self.assertTrue(350 <= self.r_condo_inst.sqft <= 800)
        self.assertTrue(1 <= self.r_condo_inst.num_beds <= 2)
        self.assertTrue(1 == self.r_condo_inst.num_baths)
        self.assertTrue(1400 <= self.r_condo_inst.rent <= 1900)
        self.assertTrue(100 <= self.r_condo_inst.utilities <= 150)

    def test_rental_townhome(self):
        self.assertTrue(800 <= self.r_townhome_inst.sqft <= 1800)
        self.assertTrue(2 <= self.r_townhome_inst.num_beds <= 4)
        self.assertTrue(1 <= self.r_townhome_inst.num_baths <= 3)
        self.assertTrue(2200 <= self.r_townhome_inst.rent <= 3200)
        self.assertTrue(200 <= self.r_townhome_inst.utilities <= 250)

    def test_rental_duplex(self):
        self.assertTrue(1400 <= self.r_duplex_inst.sqft <= 2000)
        self.assertTrue(2 <= self.r_duplex_inst.num_beds <= 5)
        self.assertTrue(2 <= self.r_duplex_inst.num_baths <= 4)
        self.assertTrue(2800 <= self.r_duplex_inst.rent <= 4000)
        self.assertTrue(250 <= self.r_duplex_inst.utilities <= 300)

    def test_bungalow(self):
        self.assertTrue(1300 <= self.r_bungalow_inst.sqft <= 2400)
        self.assertTrue(4 <= self.r_bungalow_inst.num_beds <= 5)
        self.assertTrue(3 <= self.r_bungalow_inst.num_baths <= 4)
        self.assertTrue(3400 <= self.r_bungalow_inst.rent <= 4600)
        self.assertTrue(300 <= self.r_bungalow_inst.utilities <= 400)

    def test_twostory(self):
        self.assertTrue(2000 <= self.r_twostory.sqft <= 3300)
        self.assertTrue(4 <= self.r_twostory.num_beds <= 6)
        self.assertTrue(3 <= self.r_twostory.num_baths <= 5)
        self.assertTrue(4500 <= self.r_twostory.rent <= 6100)
        self.assertTrue(350 <= self.r_twostory.utilities <= 450)

    def test_mansion(self):
        self.assertTrue(8000 <= self.r_mansion.sqft <= 12000)
        self.assertTrue(8 <= self.r_mansion.num_beds <= 10)
        self.assertTrue(7 <= self.r_mansion.num_baths <= 8)
        self.assertTrue(10000 <= self.r_mansion.rent <= 13000)
        self.assertTrue(500 <= self.r_mansion.utilities <= 675)

    def test_calc_total_rent(self):
        self.assertEqual(self.rental_known.calc_total_rent(), 45768)
        self.assertEqual(self.rental2_known.calc_total_rent(), 23052)

    def test_display_rental(self):
        # Below code specifies that the output is a print statement!
        to_terminal = io.StringIO()
        sys.stdout = to_terminal
        self.rental3_known.display_rental()

        expected_print = (
            "Rental type: Rental\n"
            "Monthly rent: $6000\n"
            "Monthly utilities: $446\n"
            "Pet deposit required: False\n"
            "Annual total: $77352\n"
            "Square footage: 3114sqft.\n"
            "Number of bedrooms: 5\n"
            "Number of bathrooms: 5"
        )
        self.assertEqual(to_terminal.getvalue().strip(), expected_print)

    def test_gen_rental(self):
        self.assertEqual(len(self.rental_gen_result), 3)
        for instance in self.rental_gen_result:
            self.assertIsInstance(instance, RentalBungalow)
        self.assertEqual(self.rental_gen_result[0].rent, 3468)
        self.assertEqual(self.rental_gen_result[1].sqft, 1896)
        self.assertEqual(self.rental_gen_result[2].num_beds, 4)

    def test_rental_recommendation(self):
        # Instantiating rental_recommendation here, in efforts to suppress the print messages
        self.rental_recommendation_result = rental_recommendation(
            RentalCondo, 37000, 1)

        self.assertEqual(len(self.rental_recommendation_result), 15)
        for instance in self.rental_recommendation_result:
            self.assertIsInstance(instance, RentalCondo)
        self.assertEqual(self.rental_recommendation_result[10].rent, 1677)
        self.assertEqual(self.rental_recommendation_result[7].sqft, 844)
        self.assertEqual(self.rental_recommendation_result[2].num_baths, 1)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
