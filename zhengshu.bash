#!/bin/bash
for i  in `find . -name *nginx*`;do unzip $i;done
for i in `find . -name "*.crt" |awk -F'.' '{print $3"."$4}' `;do cp /usr/local/nginx/kis/jd.com.conf ${i}.conf && sed -i "s/jd.com/$i/g" ${i}.conf;done
#find . -type f |xargs sed -i 's///g;s///g'
