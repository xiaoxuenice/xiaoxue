#!/bin/bash
for i  in `find . -name *nginx*`;do unzip $i;done
for i in `find . -name "*.crt" |awk -F'.' '{print $3"."$4}' `;do cp /usr/local/nginx/kis/188ball.net.conf ${i}.conf && sed -i "s/188ball\.net/$i/g" ${i}.conf;done
#find . -type f |xargs sed -i 's///g;s///g'