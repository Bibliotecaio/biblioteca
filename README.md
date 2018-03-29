# Biblioteca

Library engine

## Standalone Installation

### Utils & Libs

#### Core

```
sudo apt update
sudo apt install nginx git-core software-properties-common libtiff5-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
sudo apt install supervisor rabbitmq-server wget curl
```

#### Postgres

```
sudo apt install postgresql-9.6
```

#### Python Environ

```
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt update
sudo apt-get install python3.6
sudo apt install virtualenv
sudo apt install python3.6-pip

```

#### Java Environ

```
sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt-get install oracle-java8-installer
```


#### JS Environ

```
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
sudo apt install nodejs
sudo npm install grunt -g
sudo npm install grunt-cli -g
sudo npm install bower -g
```

#### Ruby Environ

```
sudo apt install ruby
sudo gem install docsplit
```


#### Graphics Utils

```
sudo apt install graphicsmagick poppler-data poppler-utils ghostscript
```

#### Seaweed FS

```
wget -c https://github.com/chrislusf/seaweedfs/releases/download/0.75/linux_amd64.tar.gz
tar -xf linux_amd64.tar.gz
sudo mv weed /usr/local/bin/
```