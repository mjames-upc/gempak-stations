#!/usr/bin/python
import sys,os
import re

#
# UNCOMMENT TO DOWNLOAD LATEST FROM UCAR.EDU
#os.system('wget http://weather.rap.ucar.edu/surface/stations.txt')

# CONVERT AND FORMAT
def dm2dec(degStr):
  (degree, minute, dir) = re.split(',', degStr, maxsplit=3)
  if ( dir == "W" ) or ( dir == "S" ):
    sign = -1
  else:
    sign = 1
  return int(round(sign * (int(degree) + float(minute) / 60 ),2)*100)

fname=sys.argv
with open('stations.txt') as f:
  for line in f:
    if len(line) > 50 and line[0] != "!" and not line.startswith("CD") and line[2] == " ":
      stateID=line[0:2]
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
      ( latDegree, latMinute, latDirection ) = ( line[39:41], line[42:44], line[44] )
      ( lonDegree, lonMinute, lonDirection ) = ( line[47:50], line[52:53], line[53] ) 

      latDec = dm2dec(latDegree+','+latMinute+','+latDirection)
      lonDec = dm2dec(lonDegree+','+lonMinute+','+lonDirection)

      # left pad longitude for right-aligned column
      if len(str(lonDec)) < 6: 
        lonDec = ' ' + str(lonDec)

      # PRINT GEMPAK station table
      print stationID + '     ' + synopString + ' ' + stationName + '                 ' + stateID + ' ' + countryID + '  ' + str(latDec) + ' ' + str(lonDec) + ' ' + elevation + ' 0'
sys.exit(0)


