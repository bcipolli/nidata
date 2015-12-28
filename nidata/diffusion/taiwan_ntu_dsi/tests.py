from unittest import TestCase
from nidata.diffusion import TaiwanNtuDsiDataset
from nidata.core._utils.testing import DownloadTestMixin, InstallTestMixin


class TaiwanNtuDsiDatasetDownloadTest(DownloadTestMixin, TestCase):
    dataset_class = TaiwanNtuDsiDataset


class TaiwanNtuDsiDatasetInstallTest(InstallTestMixin, TestCase):
    dataset_class = TaiwanNtuDsiDataset
