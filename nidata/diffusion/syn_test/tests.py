from unittest import TestCase
from nidata.diffusion import SynTestDataset
from nidata.core._utils.testing import DownloadTestMixin, InstallTestMixin


class SynTestDatasetDownloadTest(DownloadTestMixin, TestCase):
    dataset_class = SynTestDataset


class SynTestDatasetInstallTest(InstallTestMixin, TestCase):
    dataset_class = SynTestDataset
