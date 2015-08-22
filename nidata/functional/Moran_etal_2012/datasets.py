# *- encoding: utf-8 -*-
"""
Utilities to download functional MRI datasets
"""
# Author: Alexandre Abraham, Philippe Gervais
# License: simplified BSD

import os

from sklearn.datasets.base import Bunch

from ...core.datasets import HttpDataset


class MyDataset(HttpDataset):
    """
    """
    def fetch(self, n_subjects=1, resume=True, force=False, verbose=1):
        # Before the fetcher, consruct urls to download.
        # openfmri dataset ID ds000109


        files = [('ds109', 'http://openfmri.s3.amazonaws.com/tarballs/ds109_raw.tgz', {'uncompress': True}),
                 ('models', 'http://openfmri.s3.amazonaws.com/tarballs/ds109_metadata.tgz', {'uncompress': True})]

        files = self.fetcher.fetch(files, resume=resume, force=force, verbose=verbose)
        print(files)

        # After the fetcher, I group them in a meaningful way for the user.

        # return the data
        return Bunch(files=files)
