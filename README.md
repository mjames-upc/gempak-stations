# GEMPAK Station Decoder

This Python script downloads and decodes the [NCAR / RAL list of METAR stations](http://weather.rap.ucar.edu/surface/stations.txt) into a GEMPAK station table.  

## Use

    python stations.py > sfstns.tbl

## Result

    more sfstns.tbl
    PADK     704540 ADAK NAS                         AK US  5188 -17615     4  0
    PAKH     999999 AKHIOK                           AK US  5693 -15402    14  0
    PAFM     999999 AMBLER                           AK US  6709 -15702    88  0
    PAKP     999999 ANAKTUVUK PASS                   AK US  6813 -15107   642  0
    PANC     702730 ANCHORAGE INTL                   AK US  6117 -15002    38  0
    PAFC     999999 ANCHORAGE/WFO                    AK US  6117 -15003    48  0
    ...   

