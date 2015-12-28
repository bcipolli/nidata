from unittest import TestCase
from nidata.diffusion import ScilB0Dataset
from nidata.core._utils.testing import DownloadTestMixin, InstallTestMixin


class ScilB0DownloadDataset(DownloadTestMixin, TestCase):
    dataset_class = ScilB0Dataset

    def test_fetch_defaults(self):
        # should expect warnings. for now, too lazy..
        super(ScilB0DownloadDataset, self).test_fetch_defaults()


class ScilB0InstallDataset(InstallTestMixin, TestCase):
    dataset_class = ScilB0Dataset
