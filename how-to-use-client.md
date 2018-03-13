# Using Client

### 1. step 1: 
Sync code to local folder from: git@QE-PORT:QE-Auto/QE-PORTAL.git

### 2. 
copy top "qe_port" foler to any location. 

### 3. 
if using production server , please copy from "deploy/qe_port_client/" celery.py and settings.py from "qe_port/deploy" to overwrite those same file in "qe_port/qe_port" folder.  

### 4. 
at top "qe_port" folder (same path as "manage.py"). run the following command to start a celery client. 

for web:  
"celery -A qe_portal worker --concurrency=1 -l debug -Q web"  
for android:  
"celery -A qe_portal worker --concurrency=1 -l debug -Q android"  
for ios:  
"celery -A qe_portal worker --concurrency=1 -l debug -Q ios"  

### 5.
browser, open page: "http://qe-port:99/dashboard/scheduler_list" to run a suite. 