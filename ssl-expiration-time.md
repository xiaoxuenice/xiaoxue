#!/bin/bash
#在同一目录下 将文件(.crt)结尾的证书文件放置。
rm -f daoqishijian.txt
for i in `ls | egrep "*.crt"`;do
 if [[ $i ==  "zhengshudaoqishijian.sh" ]];then
    break
 fi
  n=`openssl x509 -in $i -noout -dates|grep notAfter | awk -F " " '{print $4}'`
  y=`openssl x509 -in $i -noout -dates|grep notAfter | awk -F " " '{print $1}' |awk -F "=" '{print $2}'`
  ri=`openssl x509 -in $i -noout -dates|grep notAfter | awk -F " " '{print $2}'`
  echo "${i} 		 ${n}-${y}-${ri}" >> daoqishijian.txt
  
done
sed -i 's/Jan/1/g;s/Feb/2/g;s/Mar/3/g;s/Apr/4/g;s/May/5/g;s/Jun/6/g;s/Jul/7/g;s/Aug/8/g;s/Sep/9/g;s/Oct/10/g;s/Nov/11/g;s/Dec/12/g;s/STAR\.//g;s/\_chained.crt//g;s/\.crt//g;s/\_/\./g' daoqishijian.txt
cat daoqishijian.txt
