import numpy as np
import scipy.io

mat = scipy.io.loadmat('TrainingSamplesDCT_8')
FG = mat["TrainsampleDCT_FG"]
BG = mat["TrainsampleDCT_BG"]
total = FG.shape[0] + BG.shape[0]
prior_c  = FG.shape[0] / total
prior_g = BG.shape[0] / total
# Question A:
print("Prior probability of Cheetah is:", prior_c)
print("Prior probability of grass is:", prior_g)

# Question B:
