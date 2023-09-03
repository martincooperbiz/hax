#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/HaX.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/HaX.dmg" && rm "dist/HaX.dmg"
create-dmg \
  --volname "HaX" \
  --volicon "hax/static/images/icon.png" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "HaX.app" 175 120 \
  --hide-extension "HaX.app" \
  --app-drop-link 425 120 \
  "dist/HaX.dmg" \
  "dist/dmg/"
