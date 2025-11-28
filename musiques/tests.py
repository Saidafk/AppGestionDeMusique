from django.test import TestCase
from django.urls import reverse, NoReverseMatch
from musiques.models import Morceau, Artiste
from rest_framework.test import APITestCase

class MorceauTestCase(TestCase):
    def setUp(self):
        artiste1 = Artiste.objects.create(nom='artiste1')
        artiste2 = Artiste.objects.create(nom='artiste2')
        Morceau.objects.create(titre='musique1', artiste=artiste1)
        Morceau.objects.create(titre='musique2', artiste=artiste2)
    
    def test_morceau_url_name(self):
        try:
            reverse('musiques:morceau-detail', args=[1])
        except NoReverseMatch:
            assert False

    def test_morceau_url(self):
        morceau = Morceau.objects.get(titre='musique1')
        url = reverse('musiques:morceau-detail', args=[morceau.pk])
        response = self.client.get(url)
        assert response.status_code == 200

    def test_morceau_without_titre(self):
        artiste = Artiste.objects.create(nom='artiste test')
        with self.assertRaises(Exception):
            Morceau.objects.create(titre=None, artiste=artiste)

    def test_morceau_without_artiste(self):
        with self.assertRaises(Exception):
            Morceau.objects.create(titre='musique sans artiste', artiste=None)

class MorceauAPITest(APITestCase):
    def test_list_api(self):
        url = reverse('musiques:morceau-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



