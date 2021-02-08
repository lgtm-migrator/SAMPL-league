#!/usr/bin/env bash

echo "settiing up EPEL repo"
sudo wget -r --no-parent -A 'epel-release-*.rpm' https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/
sudo rpm -Uvh dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-*.rpm --force
sudo yum-config-manager --enable epel*

echo "installing certbot"
sudo yum install -y certbot

echo "running certbot"
sudo certbot certonly --debug --non-interactive --email mhenry5@uci.edu --agree-tos --standalone --domains app.samplchallenges.org --keep-until-expiring --pre-hook \"sudo service nginx stop\" --post-hook \"sudo service nginx start\"

echo "linking cert"
sudo ln -sf /etc/letsencrypt/live/app.samplchallenges.org /etc/letsencrypt/live/ebcert