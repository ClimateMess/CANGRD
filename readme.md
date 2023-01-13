A failed attempt at handling the data found at https://crd-data-donnees-rdc.ec.gc.ca/CDAS/products/EC_data/CANGRD/

I am not too sure how to handle the irregular grid and how to load properly all the data into a xarray dataset. 
I thought I had done it until I realized that my grid was only the pixel index of the grd file. 

![download](https://user-images.githubusercontent.com/12923598/212220787-aaf043a1-56fa-48f8-9196-56b930751911.png)


Notes from the documentation : 
The station values of temperature anomalies or the normalized precipitation anomalies are interpolated to the evenly spaced (50 km) grid boxes using the Gandin’s Optimal Interpolation (OI) (Gandin, 1965; Alaka et al. 1972; Bretherton et al. 1976). Values for grid boxes over large bodies of water such as Hudson Bay are excluded. The spatial representativeness of the climate network in Canada and the uncertainty associated to the interpolation were assessed in previous studies (Milewska et al. 2005; Milewska and Hogg 2001). 

The CANGRD grid is in polar stereographic projection with a 50 km spatial resolution. The grid is a 125 (columns) by 95 (rows) matrix, where the SW corner (0,0) is at 40.0451°N latitude and 129.8530°W longitude. The projection is true at 60.0°N and centered on 110.0°W. The file ‘CANGRD_points_LL.txt’ lists the latitudes and longitudes for each grid point.

The filenames are six digit numbers in the format: ‘YYYYDD.grd’, where ‘YYYY’ represents a year and ‘DD’ represents the following: 

-01 to 12 – month Jan to Dec;

-13 - annual;

-14 - winter (December of previous year to February of current year);

-15 - spring (March to May);

-16 - summer (June to August);

-17 - autumn (September to November).

