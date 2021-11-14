#! /usr/bin/sh
echo "enter address:"
read address
if [ -f $address ]
then
	echo "file exists."
else
	`mkdir $address`
fi
