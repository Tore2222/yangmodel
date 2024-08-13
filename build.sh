#!/bin/bash

./gencode -t common
cp -r output/common vht/.

pyinstaller -F imish_ncc_cmd.py
pyinstaller -F imish_ncc.py
pyinstaller -F test_translator.py
