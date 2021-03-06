#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
|module_summary| object_data.py
===============================

Custom Data used in QGraphicsItems

"""

#                   (     int, const QVariant)
#I.E. object.setData(OBJ_TYPE, OBJ_TYPE_LINE);
#I.E. object.setData(OBJ_LAYER, "OUTLINE");
#I.E. object.setData(OBJ_COLOR, 123);
#I.E. object.setData(OBJ_LTYPE, OBJ_LTYPE_CONT);

# Keys
# enum OBJ_KEYS {
OBJ_TYPE   = 0  # value type - int: See OBJ_TYPE_VALUES
OBJ_NAME   = 1  # value type - str: See OBJ_NAME_VALUES
OBJ_LAYER  = 2  # value type - str: "USER", "DEFINED", "STRINGS", etc...
OBJ_COLOR  = 3  # value type - int: 0-255 //TODO: Use color chart in formats/format-dxf.h for this
OBJ_LTYPE  = 4  # value type - int: See OBJ_LTYPE_VALUES
OBJ_LWT    = 5  # value type - int: 0-27
OBJ_RUBBER = 6  # value type - int: See OBJ_RUBBER_VALUES
# };

# Values
# enum OBJ_TYPE_VALUES {
OBJ_TYPE_NULL         =      0  #: :NOTE: Allow this enum to evaluate false
OBJ_TYPE_BASE         = 100000  #: :NOTE: Values >= 65536 ensure compatibility with qgraphicsitem_cast()
OBJ_TYPE_ARC          = 100001  #:
OBJ_TYPE_BLOCK        = 100002  #:
OBJ_TYPE_CIRCLE       = 100003  #:
OBJ_TYPE_DIMALIGNED   = 100004  #:
OBJ_TYPE_DIMANGULAR   = 100005  #:
OBJ_TYPE_DIMARCLENGTH = 100006  #:
OBJ_TYPE_DIMDIAMETER  = 100007  #:
OBJ_TYPE_DIMLEADER    = 100008  #:
OBJ_TYPE_DIMLINEAR    = 100009  #:
OBJ_TYPE_DIMORDINATE  = 100010  #:
OBJ_TYPE_DIMRADIUS    = 100011  #:
OBJ_TYPE_ELLIPSE      = 100012  #:
OBJ_TYPE_ELLIPSEARC   = 100013  #:
OBJ_TYPE_RUBBER       = 100014  #:
OBJ_TYPE_GRID         = 100015  #:
OBJ_TYPE_HATCH        = 100016  #:
OBJ_TYPE_IMAGE        = 100017  #:
OBJ_TYPE_INFINITELINE = 100018  #:
OBJ_TYPE_LINE         = 100019  #:
OBJ_TYPE_PATH         = 100020  #:
OBJ_TYPE_POINT        = 100021  #:
OBJ_TYPE_POLYGON      = 100022  #:
OBJ_TYPE_POLYLINE     = 100023  #:
OBJ_TYPE_RAY          = 100024  #:
OBJ_TYPE_RECTANGLE    = 100025  #:
OBJ_TYPE_SLOT         = 100026  #:
OBJ_TYPE_SPLINE       = 100027  #:
OBJ_TYPE_TEXTMULTI    = 100028  #:
OBJ_TYPE_TEXTSINGLE   = 100029  #:
# };

# OBJ_NAME_VALUES # const char* const
OBJ_NAME_NULL         = "Unknown"               #:
OBJ_NAME_BASE         = "Base"                  #:
OBJ_NAME_ARC          = "Arc"                   #:
OBJ_NAME_BLOCK        = "Block"                 #:
OBJ_NAME_CIRCLE       = "Circle"                #:
OBJ_NAME_DIMALIGNED   = "Aligned Dimension"     #:
OBJ_NAME_DIMANGULAR   = "Angular Dimension"     #:
OBJ_NAME_DIMARCLENGTH = "Arc Length Dimension"  #:
OBJ_NAME_DIMDIAMETER  = "Diameter Dimension"    #:
OBJ_NAME_DIMLEADER    = "Leader Dimension"      #:
OBJ_NAME_DIMLINEAR    = "Linear Dimension"      #:
OBJ_NAME_DIMORDINATE  = "Ordinate Dimension"    #:
OBJ_NAME_DIMRADIUS    = "Radius Dimension"      #:
OBJ_NAME_ELLIPSE      = "Ellipse"               #:
OBJ_NAME_ELLIPSEARC   = "Elliptical Arc"        #:
OBJ_NAME_RUBBER       = "Rubber"                #:
OBJ_NAME_GRID         = "Grid"                  #:
OBJ_NAME_HATCH        = "Hatch"                 #:
OBJ_NAME_IMAGE        = "Image"                 #:
OBJ_NAME_INFINITELINE = "Infinite Line"         #:
OBJ_NAME_LINE         = "Line"                  #:
OBJ_NAME_PATH         = "Path"                  #:
OBJ_NAME_POINT        = "Point"                 #:
OBJ_NAME_POLYGON      = "Polygon"               #:
OBJ_NAME_POLYLINE     = "Polyline"              #:
OBJ_NAME_RAY          = "Ray"                   #:
OBJ_NAME_RECTANGLE    = "Rectangle"             #:
OBJ_NAME_SLOT         = "Slot"                  #:
OBJ_NAME_SPLINE       = "Spline"                #:
OBJ_NAME_TEXTMULTI    = "Multi Line Text"       #:
OBJ_NAME_TEXTSINGLE   = "Single Line Text"      #:

# enum OBJ_LTYPE_VALUES {
# CAD Linetypes
OBJ_LTYPE_CONT     = 0   #:
OBJ_LTYPE_CENTER   = 1   #:
OBJ_LTYPE_DOT      = 2   #:
OBJ_LTYPE_HIDDEN   = 3   #:
OBJ_LTYPE_PHANTOM  = 4   #:
OBJ_LTYPE_ZIGZAG   = 5   #:
# Embroidery Stitchtypes
OBJ_LTYPE_RUNNING  = 6   #: __________
OBJ_LTYPE_SATIN    = 7   #: vvvvvvvvvv
OBJ_LTYPE_FISHBONE = 8   #: >>>>>>>>>>
# };

# enum OBJ_LWT_VALUES {
OBJ_LWT_BYLAYER    = -2  #:
OBJ_LWT_BYBLOCK    = -1  #:
OBJ_LWT_DEFAULT    =  0  #:
OBJ_LWT_01         =  1  #:
OBJ_LWT_02         =  2  #:
OBJ_LWT_03         =  3  #:
OBJ_LWT_04         =  4  #:
OBJ_LWT_05         =  5  #:
OBJ_LWT_06         =  6  #:
OBJ_LWT_07         =  7  #:
OBJ_LWT_08         =  8  #:
OBJ_LWT_09         =  9  #:
OBJ_LWT_10         = 10  #:
OBJ_LWT_11         = 11  #:
OBJ_LWT_12         = 12  #:
OBJ_LWT_13         = 13  #:
OBJ_LWT_14         = 14  #:
OBJ_LWT_15         = 15  #:
OBJ_LWT_16         = 16  #:
OBJ_LWT_17         = 17  #:
OBJ_LWT_18         = 18  #:
OBJ_LWT_19         = 19  #:
OBJ_LWT_20         = 20  #:
OBJ_LWT_21         = 21  #:
OBJ_LWT_22         = 22  #:
OBJ_LWT_23         = 23  #:
OBJ_LWT_24         = 24  #:
# };

# enum OBJ_SNAP_VALUES {
OBJ_SNAP_NULL            =  0  #: :NOTE: Allow this enum to evaluate false
OBJ_SNAP_ENDPOINT        =  1  #:
OBJ_SNAP_MIDPOINT        =  2  #:
OBJ_SNAP_CENTER          =  3  #:
OBJ_SNAP_NODE            =  4  #:
OBJ_SNAP_QUADRANT        =  5  #:
OBJ_SNAP_INTERSECTION    =  6  #:
OBJ_SNAP_EXTENSION       =  7  #:
OBJ_SNAP_INSERTION       =  8  #:
OBJ_SNAP_PERPENDICULAR   =  9  #:
OBJ_SNAP_TANGENT         = 10  #:
OBJ_SNAP_NEAREST         = 11  #:
OBJ_SNAP_APPINTERSECTION = 12  #:
OBJ_SNAP_PARALLEL        = 13  #:
# };

# enum OBJ_RUBBER_VALUES {
OBJ_RUBBER_OFF = 0  #: :NOTE: Allow this enum to evaluate false
OBJ_RUBBER_ON  = 1  #: :NOTE: Allow this enum to evaluate true

OBJ_RUBBER_CIRCLE_1P_RAD = 2
OBJ_RUBBER_CIRCLE_1P_DIA = 3
OBJ_RUBBER_CIRCLE_2P = 4
OBJ_RUBBER_CIRCLE_3P = 5
OBJ_RUBBER_CIRCLE_TTR = 6
OBJ_RUBBER_CIRCLE_TTT = 7

OBJ_RUBBER_DIMLEADER_LINE = 8

OBJ_RUBBER_ELLIPSE_LINE = 9
OBJ_RUBBER_ELLIPSE_MAJORDIAMETER_MINORRADIUS = 10
OBJ_RUBBER_ELLIPSE_MAJORRADIUS_MINORRADIUS = 11
OBJ_RUBBER_ELLIPSE_ROTATION = 12

OBJ_RUBBER_GRIP = 13

OBJ_RUBBER_LINE = 14

OBJ_RUBBER_POLYGON = 15
OBJ_RUBBER_POLYGON_INSCRIBE = 16
OBJ_RUBBER_POLYGON_CIRCUMSCRIBE = 17

OBJ_RUBBER_POLYLINE = 18

OBJ_RUBBER_IMAGE = 19

OBJ_RUBBER_RECTANGLE = 20

OBJ_RUBBER_TEXTSINGLE = 21
# };

# enum SPARE_RUBBER_VALUES {
SPARE_RUBBER_OFF = 0  #: :NOTE: Allow this enum to evaluate false
SPARE_RUBBER_PATH = 1
SPARE_RUBBER_POLYGON = 2
SPARE_RUBBER_POLYLINE = 3
# };

# enum PREVIEW_CLONE_VALUES {
PREVIEW_CLONE_NULL = 0  #: :NOTE: Allow this enum to evaluate false
PREVIEW_CLONE_SELECTED = 1
PREVIEW_CLONE_RUBBER = 2
# };

# enum PREVIEW_MODE_VALUES {
PREVIEW_MODE_NULL = 0  #: :NOTE: Allow this enum to evaluate false
PREVIEW_MODE_MOVE = 1
PREVIEW_MODE_ROTATE = 2
PREVIEW_MODE_SCALE = 3
# };


# const char* const
ENABLE_SNAP   = "ENABLE_SNAP"                    #:
ENABLE_GRID   = "ENABLE_GRID"                    #:
ENABLE_RULER  = "ENABLE_RULER"                   #:
ENABLE_ORTHO  = "ENABLE_ORTHO"                   #:
ENABLE_POLAR  = "ENABLE_POLAR"                   #:
ENABLE_QSNAP  = "ENABLE_QSNAP"                   #:
ENABLE_QTRACK = "ENABLE_QTRACK"                  #:
ENABLE_LWT    = "ENABLE_LWT"                     #:
ENABLE_REAL   = "ENABLE_REAL"                    #:

SCENE_QSNAP_POINT = "SCENE_QSNAP_POINT"          #:
SCENE_MOUSE_POINT = "SCENE_MOUSE_POINT"          #:
VIEW_MOUSE_POINT  = "VIEW_MOUSE_POINT"           #:
RUBBER_ROOM = "RUBBER_ROOM"                      #:

VIEW_COLOR_BACKGROUND = "VIEW_COLOR_BACKGROUND"  #:
VIEW_COLOR_CROSSHAIR  = "VIEW_COLOR_CROSSHAIR"   #:
VIEW_COLOR_GRID       = "VIEW_COLOR_GRID"        #:

