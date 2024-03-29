# Dockerfile
FROM httpd:2.4

RUN apt-get -y update && apt-get -y install wget unzip iputils-ping
RUN wget https://raw.githubusercontent.com/ynakaoku/lb-tester-cgi/main/index.cgi
# RUN wget https://github.com/meso-cacase/difff/archive/ver6.0-stable.zip
# RUN unzip ver6.0-stable
# RUN rm -f /usr/local/apache2/htdocs/index.html
# RUN mv difff-ver6.0-stable/* /usr/local/apache2/htdocs/
RUN chmod +x index.cgi
RUN mv index.cgi /usr/local/apache2/htdocs/

RUN apt-get -y update && apt-get -y install python3
RUN sed -ri 's/#LoadModule cgid_module/LoadModule cgid_module/g; \ 
             s/DirectoryIndex index.html/DirectoryIndex index.cgi/g; \ 
             s/Options Indexes FollowSymLinks/Options Indexes FollowSymLinks ExecCGI/g; \
             s/#AddHandler cgi-script .cgi/AddHandler cgi-script .pl .cgi/g' /usr/local/apache2/conf/httpd.conf
# RUN sed -ri "s|'http://difff.jp/'|'./'|g" /usr/local/apache2/htdocs/difff.pl
