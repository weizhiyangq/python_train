import numpy as np

a = [[1,11,111],[2,22,222],[3,33,333]]
a_array = np.array(a)

np.save("npsave_train_bin.npy",a)
np.savetxt("npsave_train_txt.txt",a)

a_numpyload = np.load("npsave_train_bin.npy")
print(a_numpyload)
import pandas as pd
a_df = pd.DataFrame(a_numpyload)
print(a_df)

