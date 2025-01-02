#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 16 ros2 launch mypkg coordinate_listen.launch.py > /tmp/mypkg.log

wng () {
         echo warnig${1}
	 res=1
}

res=0

cat /tmp/mypkg.log |
grep '(x,y,z): 1.000000,1.000000,1.000000'
[ "$?" = 0 ] || wng "1.000000,1.000000,1.000000"
cat /tmp/mypkg.log |
grep '(x,y,z): 10.000000,2.000000,1.000000'
[ "$?" = 0 ] || wng "(x,y,z): 10.000000,2.000000,1.000000"
cat /tmp/mypkg.log |
grep '(x,y,z): 10.000000,10.000000,2.000000'
[ "$?" = 0 ] || wng "(x,y,z): 10.000000,10.000000,2.000000"
cat /tmp/mypkg.log |
grep '(x,y,z): 10.000000,10.000000,10.000000'
[ "$?" = 0 ] || wng "(x,y,z): 10.000000,10.000000,10.000000"


exit $res
