# coding: utf-8
import arcpy
import numpy
import pandas
inNetCDFFile = "E:/PAPER WRITING/TROPOMI & OMI NO2/OMI DATA (xem Disk D)/NC FILEs_Boundary_Vietnam/OMI Tro NO2_Ave_2010.nc"
variable = "OMNO2d_003_ColumnAmountNO2TropCloudScreened"
XDimension = "lon"
YDimension = "lat"
outRasterLayer = "py_2010"
bandDimmension = ""
dimensionValues = ""
valueSelectionMethod = ""
cellRegistration = ""
arcpy.MakeNetCDFRasterLayer_md(inNetCDFFile, variable, XDimension, YDimension,
                               outRasterLayer, bandDimmension, dimensionValues, 
                               valueSelectionMethod, cellRegistration)
# <Result 'py_2010'>
