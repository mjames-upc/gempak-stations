#!/usr/bin/python
# Easy GEMPAK station table from NCAR master list.
# ---
# M.James/Unidata	04/14	Created
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
  if re.match('[SW]', dir):
    sign = -1
  else:
    sign = 1
  return str(int(round(sign * (float(degree) + float(minute) / 60 ),2)*100))

fname=sys.argv
with open('stations.txt') as f:
  for line in f:
    if len(line) > 50 and line[0] != "!" and not line.startswith("CD") and line[2] == " ":
      stateID=line[0:2]
      if stateID=="  ": stateID="--"
      countryID=line[81:83]
      elevation=line[54:60]
      stationName=line[3:19]
      stationID=line[20:24]
      synopID=line[32:37]

      # right pad zero or missing string
      if synopID.isdigit():
        synopString=str(int(synopID) * 10)
      else:
        synopString="999999"

      # CONVERT DegMin to Decimal
      #print line[39:41] + ':' + line[42:44] + ':' + line[44]
      #print line[47:50] + ':' + line[51:53] + ':' + line[53]
      ( latDegree, latMinute, latDirection ) = ( line[39:41], line[42:44], line[44] )
      ( lonDegree, lonMinute, lonDirection ) = ( line[47:50], line[51:53], line[53] ) 

      latDec = dm2dec(latDegree+','+latMinute+','+latDirection)
      lonDec = dm2dec(lonDegree+','+lonMinute+','+lonDirection)

      # PRINT GEMPAK station table
      print stationID + '     ' + synopString.rjust(6) + ' ' + stationName + '                 ' + stateID + ' ' + countryID + ' ' + str(latDec).rjust(5) + ' ' + str(lonDec).rjust(6) + ' ' + elevation + ' 0'

sys.exit(0)


