#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]; then
	cp -f ./dist/deadline_mac ~/
	echo "alias deadline=\"~/deadline_mac\"" >> ~/.zshrc
	sleep 1
	echo "Finished! Restart your terminal."
else
	echo "Error! Program will work only on school 42 MAC OS."
fi