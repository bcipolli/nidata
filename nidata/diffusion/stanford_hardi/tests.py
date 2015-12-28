from unittest import TestCase
from nidata.diffusion import StanfordHardiDataset
from nidata.core._utils.testing import DownloadTestMixin, InstallTestMixin


class StanfordHardiDatasetDownloadTest(DownloadTestMixin, TestCase):
    dataset_class = StanfordHardiDataset


class StanfordHardiDatasetInstallTest(InstallTestMixin, TestCase):
    dataset_class = StanfordHardiDataset
