""" Load Taiwan NTU dataset

Returns
-------
img : obj,
    Nifti1Image
gtab : obj,
    GradientTable
"""

from nidata.diffusion import TaiwanNtuDsiDataset
fraw, fbval, fbvec, lic = TaiwanNtuDsiDataset().fetch()

import numpy as np
from dipy.io.gradients import read_bvals_bvecs
bvals, bvecs = read_bvals_bvecs(fbval, fbvec)
bvecs[1:] = bvecs[1:] / np.sqrt(np.sum(bvecs[1:] * bvecs[1:], axis=1))[:, None]

import nibabel as nib
from dipy.core.gradients import gradient_table
gtab = gradient_table(bvals, bvecs)
img = nib.load(fraw)
