import os
from shutil import rmtree
from tempfile import mkdtemp
import unittest

from pelican import Pelican
from pelican.settings import read_settings
from pelican.tests.support import mute

import pelican_resume

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(CURRENT_DIR, "content")

class TestPelicanResume(unittest.TestCase):
    def setUp(self):
        self.temp_path = mkdtemp(prefix="pelican_resume.")
        self.settings = read_settings(path=None, override={
            "PATH": INPUT_PATH,
            "OUTPUT_PATH": self.temp_path,
            "PLUGINS": [pelican_resume]
        })
        self.pelican = Pelican(self.settings)
        mute(True)(self.pelican.run)()

    def tearDown(self):
        rmtree(self.temp_path)