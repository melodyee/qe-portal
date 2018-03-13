# Development Environment Setup

## Step 1:
/etc/hosts

192.168.187.16 QE-PORT

## Step 2:
http://QE-PORT, Register 

## Step 3:
ssh-keygen
cat ~/.ssh/.id_rsa.pub
copy to ssh - profile

## Step 4:
go to http://192.168.187.16/QE-Auto/QE-PORTAL 

copy ssh: (xxx):QE-Auto/QE-PORTAL.git 

cd local folder:

git clone (xxx):QE-Auto/QE-PORTAL.git 

## Step 5:
sudo apt install python-pip

## Step 6:
pip install django

## Step 7:
sudo apt install python-celery-common (linux)

pip install celery

sudo pip install django-bootstrap3

sudo pip install django-simple-history

## Step 8:

sudo python -m pip install django-markdownx
