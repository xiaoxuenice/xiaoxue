uname -a
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm
yum -y --enablerepo=elrepo-kernel  install kernel-ml 
awk -F\' '$1=="menuentry " {print i++ " : " $2}' /etc/grub2.cfg
grub2-set-default 0
#reboot
