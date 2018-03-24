FROM python:3.6-stretch
RUN apt update && apt install git-core software-properties-common libtiff5-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk wget curl pdftk -y
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt install nodejs -y && npm install grunt grunt-cli bower -g
RUN apt install ruby -y && gem install docsplit
RUN apt install graphicsmagick poppler-data poppler-utils ghostscript -y
RUN wget -c https://github.com/chrislusf/seaweedfs/releases/download/0.75/linux_amd64.tar.gz &&  tar -xf linux_amd64.tar.gz && mv weed /usr/local/bin/
WORKDIR /code
ADD ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
ADD ./Makefile /code/Makefile
ADD ./client /code/client
RUN make install_npm_packages && make install_bower_packages && make compile 
ADD . /code
RUN python manage.py collectstatic --no-input
