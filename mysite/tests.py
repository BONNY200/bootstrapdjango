from django.test import TestCase
from django.contrib.staticfiles import finders
from pathlib import Path


class HomePageTests(TestCase):
    def test_homepage_renders(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'href="/static/css/style.css"')
        self.assertContains(response, '/static/images/menu/1.jpg')

    def test_homepage_assets_exist(self):
        for asset in ('css/style.css', 'js/main.js', 'images/menu/1.jpg'):
            with self.subTest(asset=asset):
                self.assertIsNotNone(finders.find(asset))

    def test_fontawesome_webfonts_resolve(self):
        stylesheet = Path(finders.find('css/all.min.css')).read_text(encoding='utf-8')
        self.assertIn('../images/webfonts/fa-solid-900.woff2', stylesheet)
        self.assertIsNotNone(finders.find('images/webfonts/fa-solid-900.woff2'))
