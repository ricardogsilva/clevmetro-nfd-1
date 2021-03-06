#!/bin/bash
set -e

npm install
npm run compile
npm run lint
mvn clean install

sudo systemctl restart slapd
sudo systemctl restart apache2
sudo systemctl restart metroparksnfd.service
sudo systemctl restart uwsgi
