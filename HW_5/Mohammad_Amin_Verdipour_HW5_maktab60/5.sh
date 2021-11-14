#! /usr/bin/sh

echo "enter address:"
read address
file=0
folder=0
add=1
for x in `ls $address`
do
	if [ -f $x ]
	then
		file=`expr $file + $add`
	elif [ -d $x ]
	then
		folder=`expr $folder + $add`
	fi
done
echo "Number of files:"$file
echo "Number of folders:"$folder


