from unittest import TestCase
from nidata.diffusion import Sherbrooke3ShellDataset
from nidata.core._utils.testing import DownloadTestMixin, InstallTestMixin


class Sherbrooke3ShellDownloadTest(DownloadTestMixin, TestCase):
    dataset_class = Sherbrooke3ShellDataset


class Sherbrooke3ShellInstallTest(InstallTestMixin, TestCase):
    dataset_class = Sherbrooke3ShellDataset
