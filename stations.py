#!/usr/bin/python
# Easy GEMPAK station table from NCAR master list.
#
# use: python stations.py stations.txt > output_filename
# ---
# M.James/Unidata	04/14	Created
#			05/15	Take input file from arg
#
#    input
#       AK ANCHORAGE INTL   PANC  ANC   70273  61 10N  150 01W   38   X     T  X  A    5 US
#    output
#       PANC     702730 ANCHORAGE INTL                   AK US  6117 -15002    38  0

import sys,os
import re

#
# UNCOMMENT to download latest.  file current as of 4/14 is included with git.
#os.system('wget http://weather.rap.ucar.edu/surface/stations.txt')

# CONVERT and format for coordinate decimal string
def dm2dec(degStr):
  # input string in the format 'degree,minute,direction' e.g '
  (degree, minute, dir) = re.split(',', degStr, maxsplit=3)
  sign=(-1 if re.match('[SW]', dir) else 1) #python <2.5 won't like this...
  return str(int(round(sign * (float(degree) + float(minute) / 60 ),2)*100))

fname=sys.argv
with open(fname[1]) as f:
  for line in f:
    if len(line) > 50 and line[0] != "!" and not line.startswith("CD") and line[2] == " ":
      stateID=line[0:2].replace("  ","--")
      countryID=line[81:83].replace("CO","CB")
      elevation=line[54:60]
      stationName=line[3:19]
      stationID=line[20:24]
      synopID=line[32:37]

      # right pad zero or missing string
      synopString=(str(int(synopID) * 10) if synopID.isdigit() else "999999")

      # CONVERT DegMin to Decimal
      ( latDegree, latMinute, latDirection ) = ( line[39:41], line[42:44], line[44] )
      ( lonDegree, lonMinute, lonDirection ) = ( line[47:50], line[51:53], line[53] ) 
      latDec = dm2dec(latDegree+','+latMinute+','+latDirection)
      lonDec = dm2dec(lonDegree+','+lonMinute+','+lonDirection)

      # PRINT GEMPAK station table
      print stationID + '     ' + synopString.rjust(6) + ' ' + stationName + '                 ' + stateID + ' ' + countryID + ' ' + str(latDec).rjust(5) + ' ' + str(lonDec).rjust(6) + ' ' + elevation + ' 0'

sys.exit(0)
