#! /usr/bin/sh

echo "please enter address:"
read address
for x in `ls $address`
do
	if [ -f $x ]
	then
		echo `cat $x > write.txt`
	fi
done
