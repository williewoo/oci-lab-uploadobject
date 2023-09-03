# oci-lab-uploadobject
A lab to show how to setup a python flask to upload files to OCI object storage bucket using Tags, Dynamic Group and Policy

![img](drawio/Overview_Diagram.png)

This is a demo to show a life usecase to allow endusers upload files to OCI Object Storage Bucket
One of the security requirement is do not allow hardcode any user name, creditdetial, key inside any configuration 

This demo show how to use OCI policy and Dynamic Group to allow the virtual machine access the object storage
To avoid hardcoding, a Tag is used

Highlights:
A virtual machine running python and assigned a Tag
A Dynamic Group include the Tagged resources (Virtual Mahcine)
A policy to allow Dynamic Group access Object Storage Bucket


Create a compute instance
Remember to add NSG

python --version
sudo pip3 install virtualenv
sudo pip3 install flask
sudo yum install python36-oci-sdk

pip3 show virtualenv
python /usr/local/lib/python3.6/site-packages/virtualenv venv
source venv/bin/activate

sudo firewall-cmd --zone=public --permanent --add-port=5000/tcp
sudo systemctl reload firewalld
sudo firewall-cmd --list-all

git clone https://github.com/williewoo/oci-lab-uploadobject.git