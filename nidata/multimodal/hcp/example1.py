from nidata.multimodal import HcpDataset
print(HcpDataset().fetch(n_subjects=1, data_types=['anat']))
