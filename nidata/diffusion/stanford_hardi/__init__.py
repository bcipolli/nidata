from ...core.datasets import HttpDataset


def fetch_stanford_labels():
    return StanfordHardiDataset().fetch(subset=('label',))


def fetch_stanford_t1():
    pass


class StanfordHardiDataset(HttpDataset):

    def fetch(self, subset=('t1', 'pve', 'labels', 'hardi')):
        """
        label: Reduced freesurfer aparc image from stanford web site.
        hardi: HARDI dataset with 160 gradient directions


        """
        rv = dict()  # return value
        subset = [sub.lower() for sub in subset]
        if 'labels' in subset:
            files = []
            baseurl = 'https://stacks.stanford.edu/file/druid:yx282xq2090/'
            files.append(("aparc-reduced.nii.gz",
                          baseurl + "aparc-reduced.nii.gz",
                          {'md5sum': '742de90090d06e687ce486f680f6d71a'}),)
            files.append(("label-info.txt",
                          baseurl + "label_info.txt",
                          {'md5sum': '39db9f0f5e173d7a2c2e51b07d5d711b'}),)
            rv['labels'] = self.fetcher.fetch(files)

        if 'hardi' in subset:
            url = 'https://stacks.stanford.edu/file/druid:yx282xq2090/'
            uraw = url + 'dwi.nii.gz'
            ubval = url + 'dwi.bvals'
            ubvec = url + 'dwi.bvecs'

            md5_list = ['0b18513b46132b4d1051ed3364f2acbc',  # data
                        '4e08ee9e2b1d2ec3fddb68c70ae23c36',  # bval
                        '4c63a586f29afc6a48a5809524a76cb4']  # bvec
            url_list = [uraw, ubval, ubvec]
            fname_list = ['HARDI150.nii.gz', 'HARDI150.bval', 'HARDI150.bvec']

            files = [(f, u, {'md5sum': m})
                     for f, u, m in zip(fname_list, url_list, md5_list)]
            rv['hardi'] = self.fetcher.fetch(files)

        if 'pve' in subset:
            url = 'https://stacks.stanford.edu/file/druid:yx282xq2090/'
            url_pve_csf = url + 'pve_csf.nii.gz'
            url_pve_gm = url + 'pve_gm.nii.gz'
            url_pve_wm = url + 'pve_wm.nii.gz'

            file_csf_md5 = '2c498e4fed32bca7f726e28aa86e9c18'
            file_gm_md5 = '1654b20aeb35fc2734a0d7928b713874'
            file_wm_md5 = '2e244983cf92aaf9f9d37bc7716b37d5'

            files = (("pve_csf.nii.gz", url_pve_csf, {'md5sum': file_csf_md5}),
                     ("pve_gm.nii.gz", url_pve_gm, {'md5sum': file_gm_md5}),
                     ("pve_wm.nii.gz", url_pve_wm, {'md5sum': file_wm_md5}))
            rv['pve'] = self.fetcher.fetch(files)

        if 't1' in subset:
            url = 'https://stacks.stanford.edu/file/druid:yx282xq2090/'
            url_t1 = url + 't1.nii.gz'
            file_md5 = 'a6a140da6a947d4131b2368752951b0a'
            files = (("t1.nii.gz", url_t1, {'md5sum': file_md5}),)
            rv['t1'] = self.fetcher.fetch(files)[0]

        return rv
