saveanomaly(char *path, Mat &mat)
{
        int n, ncid, dims[2], vid;

        CV_Assert(mat.channels() == 1);
        if(mat.depth() != CV_32F)
                mat.convertTo(mat, CV_32F);

        n = nc_create(path, NC_NOCLOBBER|NC_NETCDF4, &ncid);
        if (n != NC_NOERR)
                ncfatal(n);
        n = nc_def_dim(ncid, "scan_lines_along_track", mat.rows, &dims[0]);
        if (n != NC_NOERR)
                ncfatal(n);
        n = nc_def_dim(ncid, "pixels_across_track", mat.cols, &dims[1]);
        if (n != NC_NOERR)
                ncfatal(n);
        n = nc_def_var (ncid, "anomaly", NC_FLOAT, nelem(dims), dims, &vid);
        if (n != NC_NOERR)
                ncfatal(n);
        n = nc_put_var_float(ncid, vid, (float*)mat.data);
        if (n != NC_NOERR)
                ncfatal(n);
        n = nc_close(ncid);
        if(n != NC_NOERR)
                ncfatal(n);
        n = nc_def_var (ncid, "latitude", NC_FLOAT, nelem(dims), dims, &vid);
        if (n != NC_NOERR)
                ncfatal(n);
        n = nc_def_var (ncid, "longitude", NC_FLOAT, nelem(dims), dims, &vid);
        if (n != NC_NOERR)
                ncfatal(n);