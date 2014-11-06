#!/bin/bash
for f in fotos/*; do
  DST=${f/fotos\//}
  DST=`echo $DST | sed 's/\([0-9]*\)\_.*\.\(.*\)/\1.\2/'`
  DST=`echo 'fotos_80_80/'$DST`
  convert -resize 80x80 $f $DST 
done
