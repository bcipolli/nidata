from ...core.datasets import HttpDataset


class TaiwanNtuDsiDataset(HttpDataset):
    # folder = op.join(dipy_home, 'taiwan_ntu_dsi')

    def fetch(self):
        """ Download a DSI dataset with 203 gradient directions
        """
        uraw = 'http://dl.dropbox.com/u/2481924/taiwan_ntu_dsi.nii.gz'
        ubval = 'http://dl.dropbox.com/u/2481924/tawian_ntu_dsi.bval'
        ubvec = 'http://dl.dropbox.com/u/2481924/taiwan_ntu_dsi.bvec'
        ureadme = 'http://dl.dropbox.com/u/2481924/license_taiwan_ntu_dsi.txt'

        md5_list = ['950408c0980a7154cb188666a885a91f',  # data
                    '602e5cb5fad2e7163e8025011d8a6755',  # bval
                    'a95eb1be44748c20214dc7aa654f9e6b',  # bvec
                    '7fa1d5e272533e832cc7453eeba23f44']  # license
        url_list = [uraw, ubval, ubvec, ureadme]
        fname_list = ['DSI203.nii.gz', 'DSI203.bval',
                      'DSI203.bvec', 'DSI203_license.txt']

        return self.fetcher.fetch(
            files=[(f, u, {'md5sum': m})
                   for f, u, m in zip(fname_list, url_list, md5_list)])


def fetch_taiwan_ntu_dsi():
    return TaiwanNtuDsiDataset().fetch()
