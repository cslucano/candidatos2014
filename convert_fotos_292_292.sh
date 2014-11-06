#!/bin/bash
for f in fotos/*; do
  DST=${f/fotos\//}
  DST=`echo $DST | sed 's/\([0-9]*\)\_.*\.\(.*\)/\1.\2/'`
  DST=`echo 'fotos_292_292/'$DST`
  convert -resize 292x292 $f $DST 
done
