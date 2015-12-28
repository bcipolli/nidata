""" Load t1 and b0 volumes from the same session

Returns
-------
t1 : obj,
    Nifti1Image
b0 : obj,
    Nifti1Image
"""

from nidata.diffusion import SynTestDataset
t1_name, b0_name = SynTestDataset().fetch()

import nibabel as nib
t1 = nib.load(t1_name)
b0 = nib.load(b0_name)
