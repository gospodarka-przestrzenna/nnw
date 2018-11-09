NNW
========

NORTH by NORTHWEST (as Hitchcock movie)

The script computes road direction according to North and writes it into specified column in Shapefile.

It is computed using road start and end points.

As an input file the Shapefile is used. Ouput appears in "output" subdirectory.

Usage example: 
 ``python2 ./nnw.py -f ./someshp.shp -a columnanme``

Required libraries:
	shapefile (pyshp)



