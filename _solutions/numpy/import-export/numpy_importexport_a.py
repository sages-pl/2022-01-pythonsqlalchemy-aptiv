
species = np.loadtxt(DATA, max_rows=1, delimiter=',', dtype=str, usecols=(2,3,4))
features = np.loadtxt(DATA, skiprows=1, delimiter=',', usecols=(0,1,2,3))
labels = np.loadtxt(DATA, skiprows=1, delimiter=',', usecols=4, dtype=int)
