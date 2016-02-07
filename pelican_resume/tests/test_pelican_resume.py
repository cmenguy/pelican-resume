import os
from shutil import rmtree
from tempfile import mkdtemp
import unittest

from pelican import Pelican
from pelican.settings import read_settings

import pelican_resume

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(CURRENT_DIR, "content")

class TestPelicanResume(unittest.TestCase):
    def setUp(self):
        self.temp_path = mkdtemp(prefix="pelican_resume.")
        self.settings = read_settings(path=None, override={
            "PATH": INPUT_PATH,
            "OUTPUT_PATH": self.temp_path,
            "PLUGINS": [pelican_resume],
            "FEED_ALL_ATOM": None,
            "CATEGORY_FEED_ATOM": None,
            "TRANSLATION_FEED_ATOM": None,
            "AUTHOR_FEED_ATOM": None,
            "AUTHOR_FEED_RSS": None,
        })
        self.pelican = Pelican(self.settings)
        self.pelican.run()

    def tearDown(self):
        rmtree(self.temp_path)

    def test_resume_exists(self):
        pdf = os.path.join(self.temp_path, "pdfs", "resume.pdf")
        self.assertTrue(os.path.exists(pdf))
        self.assertTrue(os.stat(pdf).st_size > 0)

    def test_moderncv(self):
        self.assertTrue(os.path.exists(os.path.join(pelican_resume.CSS_DIR, "moderncv.css")))