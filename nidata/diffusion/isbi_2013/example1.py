""" Load ISBI 2013 2-shell synthetic dataset

Returns
-------
img : obj,
    Nifti1Image
gtab : obj,
    GradientTable
"""

from nidata.diffusion import Isbi2013Dataset
fraw, fbval, fbvec = Isbi2013Dataset().fetch()

from dipy.io.gradients import read_bvals_bvecs
bvals, bvecs = read_bvals_bvecs(fbval, fbvec)

import nibabel as nib
from dipy.core.gradients import gradient_table
gtab = gradient_table(bvals, bvecs)
img = nib.load(fraw)
