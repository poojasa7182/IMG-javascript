import unittest
import assn3
from unittest import TestCase
import requests
from bs4 import BeautifulSoup

class test_users(unittest.TestCase):

    username = "ritvik.jain.52206"
    URL= "https://m.facebook.com/"+username+"/about/"
    # login(username)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    r = requests.get(URL,cookies= {'googletrans': '/es/en'},headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.findAll('div',attrs={'class':'_55wo _2xfb _1kk1'})

    def test_scrap(self):

        self.assertEqual(assn3.scrap('radhikagarg1601'),"Done")
        self.assertEqual(assn3.scrap('utkarsh.parkhi.1'),"Done")

        with self.assertRaises(Exception):
            assn3.scrap("pooja")

        self.assertEqual(assn3.scrap('radhikagarg1601'),"Already Scrapped")
        self.assertEqual(assn3.scrap('utkarsh.parkhi.1'),"Already Scrapped")

    def test_work(self):
        work = ['IMG, IIT RoorkeeProject Leader२० जानेवारी, २०१९ - आतापर्यंत', 'Geek GazetteHead of Web Cell२५ डिसेंबर, २०१८ - आतापर्यंतWeb Developer', 'PAGprogrammer']
        self.assertEqual(assn3.find_work(self.soup,self.table),work)

    def test_city(self):
        city = "Roorkee"
        self.assertEqual(assn3.find_city(self.soup,self.table),city)

    def test_name(self):
        name = "Ritvik Jain"
        self.assertEqual(assn3.find_name(self.soup),name)

    def test_show(self):
        obj = assn3.Person(name="Pooja")
        res = obj.show()
        self.assertEqual(res,"My name is Pooja and my current city is Roorkee")

        obj = assn3.Person(name="Pooja",city="Nanded")
        res = obj.show()
        self.assertEqual(res,"My name is Pooja and my current city is Nanded")

        obj = assn3.Person(name="Pooja",city="Nanded",work=["IMG"])
        res = obj.show()
        self.assertEqual(res,"My name is Pooja and my current city is Nanded")
        
if __name__ == '__main__':
    unittest.main()