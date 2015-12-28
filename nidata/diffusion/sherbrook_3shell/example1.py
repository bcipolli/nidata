""" Load Sherbrooke 3-shell HARDI dataset

Returns
-------
img : obj,
    Nifti1Image
gtab : obj,
    GradientTable
"""

from nidata.diffusion import Sherbrooke3ShellDataset
fraw, fbval, fbvec = Sherbrooke3ShellDataset().fetch()

from dipy.io.gradients import read_bvals_bvecs
bvals, bvecs = read_bvals_bvecs(fbval, fbvec)

import nibabel as nib
from dipy.core.gradients import gradient_table
gtab = gradient_table(bvals, bvecs)
img = nib.load(fraw)
