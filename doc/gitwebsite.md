/sbin/iptables -I INPUT -p tcp --dport 8080 -j ACCEPT  
  
https://github.com/  
https://gitlab.com/  
https://git.oschina.net/  
https://coding.net/  
https://code.csdn.net/  
  
#install pip  
su -  
wget https://bootstrap.pypa.io/get-pip.py  
python get-pip.py  
  
su -  
yum install gcc  
#Python.h: No such file or directory  
yum install python-devel  
pip install uwsgi  
pip install bottle  
  
#install nginx  
yum install pcre pcre-devel    
yum install zlib zlib-devel    
yum install openssl openssl-devel    
  
find -name nginx  
yum remove nginx  
cd /usr/local   
wget http://nginx.org/download/nginx-1.7.4.tar.gz  
tar -zxvf nginx-1.7.4.tar.gz  
cd  nginx-1.7.4  
./configure  
make  
make install  
whereis nginx   
  
