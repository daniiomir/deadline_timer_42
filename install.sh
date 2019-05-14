#!/bin/bash

cp -f ./dist/deadline ~/
echo "alias deadline=\"~/deadline\"" >> ~/.zshrc
sleep 1
echo "Finished! Restart your terminal."