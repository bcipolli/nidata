from ...core.datasets import HttpDataset


class SynTestDataset(HttpDataset):

    def fetch(self):
        """ Download t1 and b0 volumes from the same session
        """
        url = 'https://dl.dropboxusercontent.com/u/5918983/'
        t1 = url + 't1.nii.gz'
        b0 = url + 'b0.nii.gz'

        md5_list = ['701bda02bb769655c7d4a9b1df2b73a6',  # t1
                    'e4b741f0c77b6039e67abb2885c97a78']  # b0
        url_list = [t1, b0]
        fname_list = ['t1.nii.gz', 'b0.nii.gz']

        return self.fetcher.fetch(
            files=[(f, u, {'md5sum': m})
                   for f, u, m in zip(fname_list, url_list, md5_list)])


def fetch_syn_data():
    return SynTestDataset().fetch()
