#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "Maciej Kaminski Politechnika Wroclawska"
__version__ = "1.0.1"

import shapefile as shp
import cmath,math
import argparse
import pdb

parser = argparse.ArgumentParser(description=\
"Program writes angle beetween North and road orientation to specified column in Shapefile")

column_group=parser.add_argument_group("column names")
column_group.add_argument("-a,--angle_column_name",dest='angle_column_name',default="angle")

files_group=parser.add_argument_group("input files")
files_group.add_argument("-f,--lines_filename",dest='filename',default='edges.shp')

args=parser.parse_args()

def main():
    with shp.Reader(args.filename) as reader:
        try:
            reader.fields
        except:
            print "No such file "+args.filename
            return

        # index of column
        try:
            column_index=[k[0].upper() for k in reader.fields].index(args.angle_column_name.upper())
            column_index-=1
        except Exception as e:
            print "No such column: "+args.angle_column_name
            print "Column must exist"
            return

        if reader.shapeType!=shp.POLYLINE:
            print "File must contain POLYLINE geometry"
            return

        with shp.Writer("output/"+args.filename) as writer:
            writer.fields=reader.fields[1:]

            for shaperecord in reader.iterShapeRecords():
                writer.shape(shaperecord.shape)
                vstart=complex(*shaperecord.shape.points[0])
                vend=complex(*shaperecord.shape.points[-1])
                vv=vend-vstart

                alpha=math.pi/2-cmath.phase(vv)
                if alpha<0:
                    alpha+=cmath.pi*2
                # to degrees
                degree=alpha/(cmath.pi*2)*360
                record = shaperecord.record
                record[column_index]=round(degree,1)
                writer.record(*record)

if __name__ == "__main__":
    main()
