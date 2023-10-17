#!/bin/sh

# heavily inspired by https://github.com/4ms/4ms-kicad-lib/blob/master/PCM/make_archive.sh

PRJECT_ROOT=`pwd`
PCM_ROOT="$PRJECT_ROOT/PCM"
TRANSLATION_PATH="$PRJECT_ROOT/kicad_amf_plugin/language"
ACHIEVE_PATH="$PRJECT_ROOT/PCM/archive"
PLUGIN_PATH="$ACHIEVE_PATH/plugins"
RESOURCE_PATH="$ACHIEVE_PATH/resources"


VERSION=$1

echo "Clean up old files"
rm -f $PCM_ROOT/*.zip
rm -rf $PLUGIN_PATH


echo "Update translation : $TRANSLATION_PATH"

pushd $TRANSLATION_PATH
python3 geni18n.py
popd

echo "Create folder structure for ZIP"
mkdir -p $PLUGIN_PATH
mkdir -p $RESOURCE_PATH

echo "Copy plugin to destination"

for i in __init__.py __main__.py kicad_amf_plugin
    do cp -r $i $PLUGIN_PATH
done

echo "Write version to achieve"
echo $VERSION > $PLUGIN_PATH/VERSION

echo "Copy resource to destination"
cp $PCM_ROOT/icon.png $RESOURCE_PATH
META_DATA_PATH=$ACHIEVE_PATH/metadata.json
cp $PCM_ROOT/metadata.template.json $META_DATA_PATH

echo "Modify archive metadata.json"
sed -i "s/VERSION_HERE/$VERSION/g" $META_DATA_PATH
sed -i "s/\"kicad_version\": \"6.0\",/\"kicad_version\": \"6.0\"/g" $META_DATA_PATH
sed -i "/SHA256_HERE/d" $META_DATA_PATH
sed -i "/DOWNLOAD_SIZE_HERE/d" $META_DATA_PATH
sed -i "/DOWNLOAD_URL_HERE/d" $META_DATA_PATH
sed -i "/INSTALL_SIZE_HERE/d" $META_DATA_PATH

echo "Zip PCM archive"
zip -r $PCM_ROOT/KiCAD-PCM-$VERSION.zip ACHIEVE_PATH/*

echo "Gather data for repo rebuild"
echo VERSION=$VERSION >> $GITHUB_ENV
echo DOWNLOAD_SHA256=$(shasum --algorithm 256 PCM/KiCAD-PCM-$VERSION.zip | xargs | cut -d' ' -f1) >> $GITHUB_ENV
echo DOWNLOAD_SIZE=$(ls -l PCM/KiCAD-PCM-$VERSION.zip | xargs | cut -d' ' -f5) >> $GITHUB_ENV
echo DOWNLOAD_URL="https:\/\/github.com\/Bouni\/kicad-jlcpcb-tools\/releases\/download\/$VERSION\/KiCAD-PCM-$VERSION.zip" >> $GITHUB_ENV
echo INSTALL_SIZE=$(unzip -l PCM/KiCAD-PCM-$VERSION.zip | tail -1 | xargs | cut -d' ' -f1) >> $GITHUB_ENV
