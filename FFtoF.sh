#!/bin/bash

fi=tabs4keyb_scrin_air_F1-F4.png
fi=

w=64
list=
for((s=1,e=4;e<13;s+=4,e+=4))
do
  b=F$s-F$e
  fi=tabs4keyb_scrin_air_$b.png
  fb=`basename $fi .png`
  for((i=0;i<4;++i))
  do
    ((f=i+s))
    fo=`echo $fb | sed "s/$b//"`F$f.png
    ((x0=($w-1)*i))
    convert -crop ${w}x48+${x0} $fi $fo
    list=$list' '$fo
  done
done

display $list
