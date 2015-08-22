import sys
sys.path.append('/Users/bcipolli/code/_git_libs/nidata')

from nidata.functional.my_dataset.datasets import MyDataset

dset = MyDataset()
output_bunch = dset.fetch()
print(output_bunch)

print(MyDataset().fetch())
