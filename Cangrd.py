import glob
import rioxarray as rio
import pandas as pd
import numpy as np
import xarray as xr

#not used for the moment even though I believe that will be needed
#df = pd.read_csv(r"CANGRD_points_LL.txt", sep = ' ', header=None)

list_files = sorted(set(glob.glob(r"t?????[0-2].grd" ) + glob.glob(r"t????0[0-9].grd" )))

times = pd.date_range("1900/01/01",freq='M', periods= len(list_files))

datarrays = [rio.open_rasterio(rst, masked=True,band_as_variable=True).assign_coords(time = t).expand_dims(dim='time').squeeze() for rst,t in zip(list_files, times)]
ds = xr.concat(datarrays,dim='time').rename({'band_1' : 'tas', 'y': 'lat', 'x' : 'lon'})