# uswgi安装  
参考 
https://www.zh30.com/centos6-simple-to-configure-nginx-uwsgi-python3-bottle-environment-tutorials.html  
http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html  

pip install bottle  
pip install uswgi  

cd /home/hi/mybottle
vi app.py
  from bottle import route,default_app
  @route('/')
  def abc():
          return 'hello'
  application=default_ap

uwsgi -s 127.0.0.1:5000 -w app --buffer-size 32768  

nginx.conf  
  location / {
              include uwsgi_params;
              uwsgi_pass 127.0.0.1:5000;
          }

http://localhost

