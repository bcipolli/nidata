from unittest import TestCase
from nidata.diffusion import Isbi2013Dataset
from nidata.core._utils.testing import DownloadTestMixin, InstallTestMixin


class Isbi2013DownloadDatasetTest(DownloadTestMixin, TestCase):
    dataset_class = Isbi2013Dataset


class Isbi2013InstallDataset(InstallTestMixin, TestCase):
    dataset_class = Isbi2013Dataset
