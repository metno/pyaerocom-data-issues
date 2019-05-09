# Checking of modellevel data files

## Working example (aerocom3_GISS-MATRIX_GLOFIR0p5_ec550aer_ModelLevel_2008_daily.nc)

### Output ncdump -h 
```
netcdf aerocom3_GISS-MATRIX_GLOFIR0p5_ec550aer_ModelLevel_2008_daily {
dimensions:
	time = 2 ;
	bnds = 2 ;
	lev = 40 ;
	lat = 90 ;
	lon = 144 ;
variables:
	double time(time) ;
		time:_FillValue = NaN ;
		time:bounds = "time_bnds" ;
		time:axis = "T" ;
		time:long_name = "time" ;
		time:standard_name = "time" ;
		time:units = "days since 1850-01-01" ;
		time:calendar = "365_day" ;
	double time_bnds(time, bnds) ;
		time_bnds:_FillValue = NaN ;
		time_bnds:units = "days since 1850-01-01" ;
		time_bnds:calendar = "365_day" ;
	double lev(lev) ;
		lev:_FillValue = NaN ;
		lev:bounds = "lev_bnds" ;
		lev:units = "1" ;
		lev:axis = "Z" ;
		lev:positive = "down" ;
		lev:long_name = "hybrid sigma pressure coordinate" ;
		lev:standard_name = "atmosphere_hybrid_sigma_pressure_coordinate" ;
		lev:formula = "p(n,k,j,i) = a(k)*p0 + b(k)*ps(n,j,i)" ;
		lev:formula_terms = "p0: p0 a: a b: b ps: ps" ;
	double lev_bnds(lev, bnds) ;
		lev_bnds:_FillValue = NaN ;
		lev_bnds:formula = "p(n,k,j,i) = a(k)*p0 + b(k)*ps(n,j,i)" ;
		lev_bnds:standard_name = "atmosphere_hybrid_sigma_pressure_coordinate" ;
		lev_bnds:units = "1" ;
		lev_bnds:formula_terms = "p0: p0 a: a_bnds b: b_bnds ps: ps" ;
	float p0 ;
		p0:_FillValue = NaNf ;
		p0:long_name = "reference pressure for hybrid sigma coordinate" ;
		p0:units = "Pa" ;
	double a(lev) ;
		a:_FillValue = NaN ;
		a:long_name = "hybrid sigma coordinate A coefficient for layer" ;
	double b(lev) ;
		b:_FillValue = NaN ;
		b:long_name = "hybrid sigma coordinate B coefficient for layer" ;
	float ps(time, lat, lon) ;
		ps:_FillValue = NaNf ;
		ps:standard_name = "surface_air_pressure" ;
		ps:long_name = "Surface Pressure" ;
		ps:units = "Pa" ;
		ps:cell_methods = "time: mean" ;
	double a_bnds(lev, bnds) ;
		a_bnds:_FillValue = NaN ;
		a_bnds:long_name = "hybrid sigma coordinate A coefficient for layer bounds" ;
	double b_bnds(lev, bnds) ;
		b_bnds:_FillValue = NaN ;
		b_bnds:long_name = "hybrid sigma coordinate B coefficient for layer bounds" ;
	double lat(lat) ;
		lat:_FillValue = NaN ;
		lat:bounds = "lat_bnds" ;
		lat:units = "degrees_north" ;
		lat:axis = "Y" ;
		lat:long_name = "latitude" ;
		lat:standard_name = "latitude" ;
	double lat_bnds(lat, bnds) ;
		lat_bnds:_FillValue = NaN ;
	double lon(lon) ;
		lon:_FillValue = NaN ;
		lon:bounds = "lon_bnds" ;
		lon:units = "degrees_east" ;
		lon:axis = "X" ;
		lon:long_name = "longitude" ;
		lon:standard_name = "longitude" ;
	double lon_bnds(lon, bnds) ;
		lon_bnds:_FillValue = NaN ;
	float ec550aer(time, lev, lat, lon) ;
		ec550aer:_FillValue = 1.e+20f ;
		ec550aer:standard_name = "volume_extinction_coeffcient_in_air_due_to_ambient_aerosol_particles" ;
		ec550aer:long_name = "Aerosol Extinction @550nm" ;
		ec550aer:units = "m-1" ;
		ec550aer:original_name = "ec550aer" ;
		ec550aer:cell_methods = "time: mean" ;
		ec550aer:history = "2017-03-09T23:41:42Z altered by CMOR: replaced missing value flag (-1e+30) with standard missing value (1e+20)." ;
		ec550aer:associated_files = "gridspecFile: gridspec_REALM_fx_GISS-MATRIX-GLOFIR0p5_r0i0p0.nc" ;

// global attributes:
		:institution = "NASA/GISS (Goddard Institute for Space Studies) New York, NY" ;
		:institute_id = "NASA-GISS" ;
		:experiment_id = "GLOFIR0p5" ;
		:source = "GISS-MATRIX-GLOFIR0p5-MATRIXEQSAM_AEROBB2s Atmosphere: GISS-E2; Ocean: R" ;
		:model_id = "GISS-MATRIX-GLOFIR0p5" ;
		:forcing = "N/A" ;
		:parent_experiment_id = "N/A" ;
		:parent_experiment_rip = "N/A" ;
		:branch_time = 0. ;
		:contact = "Kenneth Lo (cdkkl@giss.nasa.gov)" ;
		:references = "http://data.giss.nasa.gov/modelE/ar5" ;
		:initialization_method = 1 ;
		:physics_version = 1 ;
		:tracking_id = "10b022b3-0597-490f-8d97-24c074853a57" ;
		:product = "output" ;
		:experiment = "GLOFIR0p5" ;
		:frequency = "day" ;
		:creation_date = "2017-03-09T23:41:42Z" ;
		:history = "2017-03-09T23:41:42Z CMOR rewrote data to comply with CF standards and AEROCOM-ACC requirements." ;
		:Conventions = "CF-1.3" ;
		:project_id = "AEROCOM-ACC" ;
		:table_id = "Table 3D-D (July 2009) 6053da228d695447dc6f66720d2bf9f8" ;
		:title = "GISS-MATRIX-GLOFIR0p5 model output prepared for AEROCOM-ACC GLOFIR0p5" ;
		:parent_experiment = "N/A" ;
		:modeling_realm = "REALM" ;
		:realization = 1 ;
		:cmor_version = "2.5.7" ;
}
```
