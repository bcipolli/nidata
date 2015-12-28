"""Read stanford hardi data and label map"""

from nidata.diffusion import StanfordHardiDataset
dset = StanfordHardiDataset().fetch()

# Hardi data
fraw, fbval, fbvec = dset['hardi']

from dipy.io.gradients import read_bvals_bvecs
bvals, bvecs = read_bvals_bvecs(fbval, fbvec)

import nibabel as nib
from dipy.core.gradients import gradient_table
gtab = gradient_table(bvals, bvecs)
img = nib.load(fraw)

# Labels data
import nibabel as nib
labels_file = dset['labels'][0]
labels_img = nib.load(labels_file)


# pve data
f_pve_csf, f_pve_gm, f_pve_wm = dset['pve']
img_pve_csf = nib.load(f_pve_csf)
img_pve_gm = nib.load(f_pve_gm)
img_pve_wm = nib.load(f_pve_wm)

# t1 data
f_t1 = dset['t1']
t1_img = nib.load(f_t1)
