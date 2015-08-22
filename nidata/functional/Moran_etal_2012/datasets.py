# *- encoding: utf-8 -*-
"""
Utilities to download functional MRI datasets
"""
# Author: Shuying Yu
# License: simplified BSD

import os

from sklearn.datasets.base import Bunch

from ...core.datasets import HttpDataset
from ...core.fetchers import readmd5_sum_file


class MyDataset(HttpDataset):
    """
    """
    def fetch(self, n_subjects=1, resume=True, force=False, verbose=1):
        # Before the fetcher, construct urls to download.
        # openfmri dataset ID ds000109


        files = [('ds109', 'http://openfmri.s3.amazonaws.com/tarballs/ds109_raw.tgz', {'uncompress': True}),
                 ('models', 'http://openfmri.s3.amazonaws.com/tarballs/ds109_metadata.tgz', {'uncompress': True})]

        files = self.fetcher.fetch(files, resume=resume, force=force, verbose=verbose)

        #return Batch(files=files)

        #anat_files_names = ['highres001.nii.gz','highres001_brain.nii.gz',
        #                    'highres001_brain_mask.nii.gz']
        #behav_file_names = ['behavdata.txt']
        #func_file_names = ['bold.nii.gz']
        #model_file_names =['cond001,txt', 'cond002.txt', 'cond003.txt', 'cond004.txt']


        #behav_dirs = ['task001_run001','task001_run002']
        #func_dirs = ['task001_run001','task001_run002']
        #model_dirs = ['task001_run001','task001_run002']

        #n_subjects = 36

        #anat_files = [
        #    os.path.join('ds109','sub%03d' % i, 'anatomy', anat_file)
        #    for i in range(1, n_subjects+1)
        #    for anat_file in anat_files_names]

        #behav_files = [
        #    os.path.join('ds109','sub%03d' % i, 'behav', behav_dir, 'behavdata.txt')
        #    for i in range(1, n_subjects+1)
        #   for behav_dir in behav_dirs]

        #func_files = [
        #    os.path.join('ds109','sub%03d' % i, 'BOLD', func_dir, 'bold.nii.gz')
        #    for i in range(1, n_subjects+1)
        #    for func_dir in func_dirs]

        #vox_files = [
        #    os.path.join('ds109','sub%03d' % i, 'BOLD', func_dir, 'QA', 'voxsfnr.nii.gz')
        #    for i in range(1, n_subjects+1)
        #    for func_dir in func_dirs]

        #model_files = [
        #    os.path.join('ds109','sub%03d' % i, 'model001', 'onsets', model_dir, model_file_name)
        #    for i in range(1, n_subjects+1)
        #    for model_dir in model_dirs
        #    for model_file in model_files_names]


        # return the data
        #return Bunch(anat = anat_files, behav = behav_files, func = func_files, model = model_files, vox = vox_files)


