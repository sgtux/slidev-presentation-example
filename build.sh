#!/bin/bash
BASE_SITE_PATH=owasp-top-10
rm -rf build
mkdir build

list=(Intro A01 A02 A03 A04 A05 A06 A07 A08 A09 A10)

for i in "${list[@]}";
do
    cd $i
    echo "Building $i..."
    yarn
    yarn build --base /$BASE_SITE_PATH/$i/ > /dev/null

    if [ $? != 0 ]; then
        echo "Failed."
        exit
    fi
    mv dist ../build/$i
    cd ..
    echo "Done."
done

sed -i 's/#IMAGE_PATH_TO_USE#/..\/images\//g' build/*/assets/*.js
cp -R images build
cp index.html build
