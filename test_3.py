import unittest
import assn3
from unittest import TestCase

class test_users(unittest.TestCase):

    def test_scrap1(self):
        self.assertEqual(assn3.scrap('radhikagarg1601'),"Done")
        self.assertEqual(assn3.scrap('utkarsh.parkhi.1'),"Done")
        self.assertEqual(assn3.scrap('rishi.ranjan.54966'),"Done")
        self.assertEqual(assn3.scrap('ritvik.jain.52206'),"Done")
        self.assertEqual(assn3.scrap('anshul.d.sharma.7'),"Done")

    def test_scrap2(self):
        self.assertEqual(assn3.scrap('radhikagarg1601'),"Already Scrapped")
        self.assertEqual(assn3.scrap('utkarsh.parkhi.1'),"Already Scrapped")
        self.assertEqual(assn3.scrap('rishi.ranjan.54966'),"Already Scrapped")
        self.assertEqual(assn3.scrap('ritvik.jain.52206'),"Already Scrapped")
        self.assertEqual(assn3.scrap('anshul.d.sharma.7'),"Already Scrapped")

    def test_invalidUsernames(self):
        with self.assertRaises(Exception):
            assn3.scrap("pooja")


if __name__ == '__main__':
    unittest.main()