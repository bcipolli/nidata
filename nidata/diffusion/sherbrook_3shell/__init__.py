from ...core.datasets import HttpDataset


class Sherbrooke3ShellDataset(HttpDataset):
    # folder = op.join(dipy_home, 'sherbrooke_3shell')
    def fetch(self):
        """ Download a 3shell HARDI dataset with 192 gradient directions
        """
        url = 'https://dl.dropboxusercontent.com/u/2481924/sherbrooke_data/'
        uraw = url + '3shells-1000-2000-3500-N193.nii.gz'
        ubval = url + '3shells-1000-2000-3500-N193.bval'
        ubvec = url + '3shells-1000-2000-3500-N193.bvec'

        # zip
        md5_list = ['0b735e8f16695a37bfbd66aab136eb66',  # data
                    'e9b9bb56252503ea49d31fb30a0ac637',  # bval
                    '0c83f7e8b917cd677ad58a078658ebb7']  # bvec
        url_list = [uraw, ubval, ubvec]
        fname_list = ['HARDI193.nii.gz', 'HARDI193.bval', 'HARDI193.bvec']

        return self.fetcher.fetch(
            files=[(f, u, {'md5sum': m})
                   for f, u, m in zip(fname_list, url_list, md5_list)])


def fetch_sherbrooke_3shell():
    return Sherbrooke3ShellDataset().fetch()
