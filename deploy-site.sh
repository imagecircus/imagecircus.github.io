#!/bin/sh
cd output
git add -A .
git commit -a -m 'Updating site'
git push origin gh-pages