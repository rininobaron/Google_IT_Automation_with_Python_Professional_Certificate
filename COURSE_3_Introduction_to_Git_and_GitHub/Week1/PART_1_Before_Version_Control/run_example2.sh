#! /usr/bin/env sh

echo "Differences between hello_world_prev.txt and hello_world_long.txt files"
sleep 2
diff -u hello_world_prev.txt hello_world_long.txt > hello_world.diff
cat hello_world.diff
sleep 5
echo "diff file created!"
sleep 2
clear
echo "Patch hello_world.txt using hello_world.diff"
patch hello_world.txt < hello_world.diff
sleep 1
cat hello_world.txt
sleep 5
