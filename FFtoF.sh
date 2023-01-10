#!/bin/bash

fi=tabs4keyb_scrin_air_F1-F4.png

w=64
for((i=1;i<5;++i))
do
  fb=`basename $fi .png`
  fo=`echo $fb | sed "s/F.-F.//"`F$i.png
  ((x0=($w-1) *(i-1)))
  convert -crop ${w}x48+${x0} $fi $fo
  list=$list' '$fo
done

display $list
