import os
import os.path as op
import warnings

from ...core.datasets import HttpDataset


class ScilB0Dataset(HttpDataset):
    # folder = op.join(dipy_home, 'sherbrooke_3shell')
    def fetch(self):
        """ Download b=0 datasets from multiple MR systems (GE, Philips, Siemens) and
            different magnetic fields (1.5T and 3T)

            output is flattened, images are put in all relevant groups:
            1.5T, 3T, GE, Philips, Siemens, Stanford
        """
        zipname = 'datasets_multi-site_all_companies'
        url = 'http://scil.dinf.usherbrooke.ca/wp-content/data/'
        uraw = url + zipname + '.zip'

        out_dir = self.fetcher.fetch(
            ((zipname, uraw, dict(uncompress=True)),))[0]

        # Now gather all info into a dict.
        out_files = dict()
        try:
            for mag_type in next(os.walk(out_dir))[1]:
                mag_dir = op.join(out_dir, mag_type)
                mfrs = next(os.walk(mag_dir))[1]

                if len(mfrs) == 0:
                    out_files[mag_type] = (out_files.get(mag_type, []) +
                                           [op.join(mag_dir, 'b0.nii.gz')])
                else:
                    for mfr in mfrs:
                        out_file = op.join(mag_dir, mfr, 'b0.nii.gz')
                        out_files[mag_type] = (out_files.get(mag_type, []) +
                                               [out_file])
                        out_files[mfr] = (out_files.get(mfr, []) + [out_file])
        except StopIteration:  # some unexpected structure
            warnings.warn("Zip file had unexpected structure, unable to "
                          "automatically categorize files. "
                          "Files are at %s." % out_dir)
        return out_files


def fetch_scil_b0():
    ScilB0Dataset().fetch()
