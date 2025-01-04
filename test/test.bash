#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kouta Sakai
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
echo $ROS_DISTRO
timeout 12 ros2 launch mypkg coordinate_listen.launch.py > /tmp/mypkg.log

wng () {
         echo warnig${1}
	 res=1
}

res=0

cat /tmp/mypkg.log |
grep '43.062100,141.354400'
[ "$?" = 0 ] || wng "札幌"
cat /tmp/mypkg.log |
grep '38.268200,140.869400'
[ "$?" = 0 ] || wng "仙台"
cat /tmp/mypkg.log |
grep '35.689500,139.691700'
[ "$?" = 0 ] || wng "東京"
cat /tmp/mypkg.log |
grep '35.443700,139.638000'
[ "$?" = 0 ] || wng "横浜"
cat /tmp/mypkg.log |
grep '35.181500,136.906600'
[ "$?" = 0 ] || wng "名古屋"
cat /tmp/mypkg.log |
grep '34.693700,135.502300'
[ "$?" = 0 ] || wng "大阪"
cat /tmp/mypkg.log |
grep '35.011600,135.768100'
[ "$?" = 0 ] || wng "京都"
cat /tmp/mypkg.log |
grep '34.690100,135.195600'
[ "$?" = 0 ] || wng "神戸"
cat /tmp/mypkg.log |
grep '34.385300,132.455300'
[ "$?" = 0 ] || wng "広島"
cat /tmp/mypkg.log |
grep '33.590400,130.401700'
[ "$?" = 0 ] || wng "福岡"


exit $res
