#!/bin/bash

rm allnews.zip
cd package/
zip -r ../allnews.zip .
cd ..
zip allnews.zip *.py *.html *.css