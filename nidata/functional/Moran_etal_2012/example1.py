import sys
sys.path.append('C:/Users/Shuying/nidata')

#from nidata.functional.Moran_etal_2012.datasets import MyDataset

import sys
sys.path.append('C:/Users/Shuying/nidata_path')

from nidata.functional.moran_etal_2012.datasets import MoranEtal2012Dataset

# dset = MoranEtal2012Dataset()
#output_bunch = dset.fetch()

#Filenames to be used
dataset = {

    # Structural data of the brain (without skull)
    'anat_brain': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/anatomy/highres001_brain.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/anatomy/highres001_brain.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/anatomy/highres001_brain.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/anatomy/highres001_brain.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/anatomy/highres001_brain.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/anatomy/highres001_brain.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/anatomy/highres001_brain.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/anatomy/highres001_brain.nii.gz'
    ],

    # Behavioral responses for false belief condition
    'behavior_belief': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/behav/task001_run001/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/behav/task001_run001/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/behav/task001_run001/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/behav/task001_run001/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/behav/task001_run001/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/behav/task001_run001/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/behav/task001_run001/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/behav/task001_run001/behavdata.txt'
    ],

    # Behavioral responses for false photo condition
    'behavior_photo': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/behav/task001_run002/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/behav/task001_run002/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/behav/task001_run002/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/behav/task001_run002/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/behav/task001_run002/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/behav/task001_run002/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/behav/task001_run002/behavdata.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/behav/task001_run002/behavdata.txt'
    ],

    # Functional data for false belief conditions
    'func_belief': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/BOLD/task001_run001/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/BOLD/task001_run001/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/BOLD/task001_run001/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/BOLD/task001_run001/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/BOLD/task001_run001/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/BOLD/task001_run001/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/BOLD/task001_run001/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/BOLD/task001_run001/bold.nii.gz'
    ],

    # Functional data for false photo conditions
    'func_photo': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/BOLD/task001_run002/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/BOLD/task001_run002/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/BOLD/task001_run002/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/BOLD/task001_run002/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/BOLD/task001_run002/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/BOLD/task001_run002/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/BOLD/task001_run002/bold.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/BOLD/task001_run002/bold.nii.gz'
    ],

    # Vox data for the false belief conditions.
    'vox_belief': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/BOLD/task001_run001/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/BOLD/task001_run001/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/BOLD/task001_run001/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/BOLD/task001_run001/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/BOLD/task001_run001/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/BOLD/task001_run001/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/BOLD/task001_run001/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/BOLD/task001_run001/QA/voxsfnr.nii.gz'
    ],

    # Vox data for the false photo conditions.
    'vox_photo': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/BOLD/task001_run002/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/BOLD/task001_run002/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/BOLD/task001_run002/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/BOLD/task001_run002/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/BOLD/task001_run002/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/BOLD/task001_run002/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/BOLD/task001_run002/QA/voxsfnr.nii.gz',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/BOLD/task001_run002/QA/voxsfnr.nii.gz'
    ],

    #Part 1; contains start time, duration, and weighting of 10 sec story
    'false_belief_story_1': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/model/model001/onsets/task001_run001/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/model/model001/onsets/task001_run001/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/model/model001/onsets/task001_run001/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/model/model001/onsets/task001_run001/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/model/model001/onsets/task001_run001/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/model/model001/onsets/task001_run001/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/model/model001/onsets/task001_run001/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/model/model001/onsets/task001_run001/cond001.txt'
    ],

    #Part 2; contains start time, duration, and weighting of 10 sec story
    'false_belief_story_2': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/model/model001/onsets/task001_run002/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/model/model001/onsets/task001_run002/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/model/model001/onsets/task001_run002/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/model/model001/onsets/task001_run002/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/model/model001/onsets/task001_run002/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/model/model001/onsets/task001_run002/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/model/model001/onsets/task001_run002/cond001.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/model/model001/onsets/task001_run002/cond001.txt'
    ],

    # Part 1: 1st belief condition with 6 sec question
    'false_belief_question_1': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/model/model001/onsets/task001_run001/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/model/model001/onsets/task001_run001/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/model/model001/onsets/task001_run001/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/model/model001/onsets/task001_run001/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/model/model001/onsets/task001_run001/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/model/model001/onsets/task001_run001/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/model/model001/onsets/task001_run001/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/model/model001/onsets/task001_run001/cond002.txt'
    ],

    # Part 2: 2nd belief condition with 6 sec question
    'false_belief_question_2': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/model/model001/onsets/task001_run002/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/model/model001/onsets/task001_run002/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/model/model001/onsets/task001_run002/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/model/model001/onsets/task001_run002/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/model/model001/onsets/task001_run002/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/model/model001/onsets/task001_run002/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/model/model001/onsets/task001_run002/cond002.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/model/model001/onsets/task001_run002/cond002.txt'
    ],

    #Part 1; contains start time, duration, and weighting of 10 sec story
    'false_photo_story_1': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/model/model001/onsets/task001_run001/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/model/model001/onsets/task001_run001/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/model/model001/onsets/task001_run001/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/model/model001/onsets/task001_run001/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/model/model001/onsets/task001_run001/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/model/model001/onsets/task001_run001/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/model/model001/onsets/task001_run001/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/model/model001/onsets/task001_run001/cond003.txt'
    ],

    # Part 2; contains start time, duration, and weighting of 10 sec story
    'false_photo_story_2': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/model/model001/onsets/task001_run002/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/model/model001/onsets/task001_run002/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/model/model001/onsets/task001_run002/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/model/model001/onsets/task001_run002/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/model/model001/onsets/task001_run002/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/model/model001/onsets/task001_run002/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/model/model001/onsets/task001_run002/cond003.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/model/model001/onsets/task001_run002/cond003.txt'
    ],

    # Part 1: 1st photo condition with 6 sec question
    'false_photo_question_1': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/model/model001/onsets/task001_run001/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/model/model001/onsets/task001_run001/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/model/model001/onsets/task001_run001/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/model/model001/onsets/task001_run001/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/model/model001/onsets/task001_run001/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/model/model001/onsets/task001_run001/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/model/model001/onsets/task001_run001/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/model/model001/onsets/task001_run001/cond004.txt'
    ],

    # Part 2: 2nd photo condition with 6 sec question
    'false_photo_question_2': [
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub001/model/model001/onsets/task001_run002/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub002/model/model001/onsets/task001_run002/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub003/model/model001/onsets/task001_run002/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub005/model/model001/onsets/task001_run002/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub007/model/model001/onsets/task001_run002/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub008/model/model001/onsets/task001_run002/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub009/model/model001/onsets/task001_run002/cond004.txt',
        'C:/Users/Shuying/nidata_path/Moran_etal_2012/ds109/sub010/model/model001/onsets/task001_run002/cond004.txt'
    ]

}


# Print the dataset {key: value}
# print(dataset)

import glob
import numpy as np
import os
import matplotlib.pyplot as plt
import tempfile

import nibabel
from nilearn.image import index_img
from nilearn.plotting import plot_anat, plot_stat_map

"""
# Load structural data
for i in range(0,3):
    print("Loading structural data...")
    try:
        struct_img = nibabel.load(dataset['anat_brain'][i])
    except Exception as e:
        print('Unexpected exception: %s' % e)
    else:
        print("Structural image size: %s" % str(struct_img.shape))
        plot_anat(struct_img, title='Structural Image')
# plt.show()

# Load functional data for false belief
for i in range(0,3):
    print("Loading functional data for False Belief Story...")
    try:
        func_belief_img = nibabel.load(dataset['func_belief'][i])
    except Exception as e:
        print('Unexpected exception: %s' % e)
    else:
        print(func_belief_img.get_data().shape)
        plot_stat_map(index_img(func_belief_img, i))
# plt.show()

# Load functional data for false photo
for i in range(0,3):
    print("Loading functional data for False Photo Story...")
    try:
        func_photo_img = nibabel.load(dataset['func_photo'][i])
    except Exception as e:
        print('Unexpected exception: %s' % e)
    else:
        print(func_photo_img.get_data().shape)
        plot_stat_map(index_img(func_photo_img, i))
plt.show()
"""

# Linear Regression Analysis
from scipy import stats
import numpy as np

import pandas
age = pandas.read_csv('C:/Users/Shuying/nidata_path/Moran_etal_2012/demographics.txt', sep=' ', error_bad_lines=False, header=None)
#print(age[3].as_matrix()) # Print ages from demographics (43 out of 48 salvaged)

from numpy import arange,array,ones,linalg, loadtxt, zeros, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
import pylab
import matplotlib.pyplot as plt

# Define variables.
# X is age and Y is voxel activation (but as random numbers for now...)
xi = age[3].as_matrix()
A = array([ xi, ones(len(age[3].as_matrix()))])
# linearly generated sequence
y = np.random.random_sample((len(age[3].as_matrix()),))
title('Voxel Activation = f(Age)',fontsize='25')
xlabel('Age in Years', fontsize='20')
ylabel('Voxel Activation', fontsize='20')


slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
print 'r-value:', r_value
print  'p-value:', p_value
print 'standard deviation:', std_err


line = slope*xi+intercept
pylab.plot(xi,line,'r-',linewidth=2.0, label='First Order Model')
pylab.plot(xi,y,'o', label='Data')
pylab.legend(loc='upper right', fontsize='15')
#pylab.legend(loc='upper left')
show()

"""
w = linalg.lstsq(A.T,y)[0] # obtaining the parameters

# plotting the line
line = w[0]*xi+w[1] # regression line
plot(xi,line,'r-',xi,y,'o')
show()
"""

# print(MyDataset().fetch())
