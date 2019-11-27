#%%

import numpy as np
import glob

seqinfo = "E:\OBJECT_DECTECT\deep_sort\detections"
#for seqinfo in seq:
for filename in glob.glob(seqinfo +"/*.npy"):
    load=np.load(filename)
    np.savetxt(filename[39:48]+'txt',load)

#%%
