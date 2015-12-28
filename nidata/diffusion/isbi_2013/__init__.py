from ...core.datasets import HttpDataset


class Isbi2013Dataset(HttpDataset):
    # folder = op.join(dipy_home, 'taiwan_ntu_dsi')

    def fetch(self):
        """ Download a 2-shell software phantom dataset
        """
        url = 'https://dl.dropboxusercontent.com/u/2481924/isbi2013_merlet/'
        uraw = url + '2shells-1500-2500-N64-SNR-30.nii.gz'
        ubval = url + '2shells-1500-2500-N64.bval'
        ubvec = url + '2shells-1500-2500-N64.bvec'

        md5_list = ['42911a70f232321cf246315192d69c42',  # data
                    '90e8cf66e0f4d9737a3b3c0da24df5ea',  # bval
                    '4b7aa2757a1ccab140667b76e8075cb1']  # bvec
        url_list = [uraw, ubval, ubvec]
        fname_list = ['phantom64.nii.gz', 'phantom64.bval', 'phantom64.bvec']

        return self.fetcher.fetch(
            files=[(f, u, {'md5sum': m})
                   for f, u, m in zip(fname_list, url_list, md5_list)])


def fetch_isbi2013_2shell():
    return Isbi2013Dataset().fetch()
