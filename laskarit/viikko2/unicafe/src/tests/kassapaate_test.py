import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_rahaa_tonni(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    def test_ei_edullisia(self):
        self.assertEqual(self.kassa.edulliset, 0)
    def test_ei_maukkaita(self):
        self.assertEqual(self.kassa.maukkaat, 0)


    def test_cash_edullinen_raha(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, (100000+240))
    
    def test_cash_edullinen_kpl(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_cash_edullinen_ei_kpl(self):
        self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_cash_edullinen_ei_raha(self):
        self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_cash_edullinen_ei_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(230), 230)



    def test_cash_maukkaat_raha(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, (100000+400))
    
    def test_cash_maukkaat_kpl(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_cash_maukkaat_ei_kpl(self):
        self.kassa.syo_maukkaasti_kateisella(380)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_cash_edullinen_ei_raha(self):
        self.kassa.syo_maukkaasti_kateisella(380)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_cash_edullinen_ei_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(380), 380)


#----------------KORTTI-----------------------


    def test_kortti_edullinen_raha_kassa_muutu(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, (100000))
    
    def test_kortti_edullinen_kpl(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_kortti_edullinen_palautus(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)

    def test_kortti_edullinen_maksutus(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")

    def test_kortti_edullinen_ei_kpl(self):
        card = Maksukortti(230)
        self.kassa.syo_edullisesti_kortilla(card)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_kortti_edullinen_ei_palautus(self):
        card = Maksukortti(230)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(card), False)

    def test_kortti_edullinen_ei_muuta_saldoa(self):
        card = Maksukortti(230)
        self.kassa.syo_edullisesti_kortilla(card)
        self.assertEqual(str(card), "Kortilla on rahaa 2.30 euroa")

    


    def test_kortti_maukas_raha_kassa_muutu(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, (100000))
    
    def test_kortti_maukas_kpl(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_kortti_maukkaasti_palautus(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)

    def test_kortti_maukaasti_maksutus(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_kortti_maukas_ei_kpl(self):
        card = Maksukortti(230)
        self.kassa.syo_maukkaasti_kortilla(card)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_kortti_maukas_ei_palautus(self):
        card = Maksukortti(230)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(card), False)

    def test_kortti_maukas_ei_muuta_saldoa(self):
        card = Maksukortti(230)
        self.kassa.syo_maukkaasti_kortilla(card)
        self.assertEqual(str(card), "Kortilla on rahaa 2.30 euroa")

    

    def test_lataa_rahaa_saldo_muuttuu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 11.00 euroa")
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)

    def test_lataa_nega(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)