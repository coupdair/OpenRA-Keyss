#!/bin/bash

fi=tabs4keyb_scrin_air_F1-F4.png
fi=

w=64
list=
for t in build shield walk vehicle air
do
  for((s=1,e=4;e<13;s+=4,e+=4))
  do
    b=F$s-F$e
    fi=tabs4keyb_scrin_${t}_$b.png
    fb=`basename $fi .png`
    for((i=0;i<4;++i))
    do
      ((f=i+s))
      fo=`echo $fb | sed "s/$b//"`F$f.png
      ((x0=($w-1)*i))
      convert -crop ${w}x48+${x0} $fi $fo
      #clean (base on file size, black=empty image is less than 1kB)
      empty=`ls -lah $fo | sed 's/  / /g;s/  / /g;' | cut -d ' ' -f5 | grep K | wc -l`
      if((empty==0))
      then
        rm $fo
      else
        list=$list' '$fo
      fi
    done
  done
done

#exit

display $list
