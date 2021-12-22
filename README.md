# MRS-Labs

## MRS Introduction
For more information about MapReduce cluster you can refer to this [Link](https://cloud.orange-business.com/en/offers/infrastructure-iaas/public-cloud/features/map-reduce-service/)

## MRS version
This guide is validated with MRS version 3.1.0-LTS and anaconda3 (Anaconda3-2020.07-Linux-x86_64.sh [Link](https://docs.anaconda.com/anaconda/install/hashes/lin-3-64/)). Since MRS has python 2.7 and 3.8 installed, we choose the version of Anaconda which has also python 3.8 installed 
## Steps
1. Install MRS Client
3. Install Anaconda
4. Integrate with Spark2x

### Install MRS Client

Most of the details are described in [Link](https://docs.prod-cloud-ocb.orange-business.com/usermanual/mrs/admin_guide_000171.html)

![image](https://user-images.githubusercontent.com/11695917/147064871-4c1bfe47-4ee0-41a0-91fc-83617e27fca5.png)

It is recommanded to install the VM which runs notebook in the same VPC of the MRS cluster. In this way MRS Manager can easily transfer MRS client to the target VM.

### Install Anaconda

You can use wget to download a choosen version of anaconda for the VM. For example:

wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh

It is advised to install in another place than the default one, for example /opt/anaconda3

Once done click yes to initiate Anaconda3, the initiation process will be written in  ~/.bashrc

The problem is that if it is written in ~/.bashrc, everytime login it will automatically start Anaconda3, so you can copy paste is to ~/.bashrc.anaconda

```
cp ~/.bashrc ~/.bashrc.anaconda
```

Then do:

```
vi ~/.bashrc to remove the conda initialize part
```

![image](https://user-images.githubusercontent.com/11695917/147119509-584e235d-e79a-4b4c-8947-7eaab7a5e1d8.png)

Finally do source ~/.bashrc.anaconda to load the environment

Then do: 

```
jupyter notebook --generate-config --allow-root to generate the conf file.
```

![image](https://user-images.githubusercontent.com/11695917/147119667-e67269e3-1c65-46b6-81f2-d82ac28df63d.png)

```
vi /root/.jupyter/jupyter_notebook_config.py to modify the ip to the host ip:
```

![image](https://user-images.githubusercontent.com/11695917/147119752-661b368c-0729-49c5-a920-2972e2852db8.png)

Change port if already in use:

![image](https://user-images.githubusercontent.com/11695917/147119800-ecc2e156-476c-4e9d-9691-c9bec5ea2ff7.png)

Save the file

### Integrate with Spark2x

Once done for installing MRS client and anaconda, then you can launch jupyter notebook by the following commands:

```
source /opt/hadoopclient/bigdata_env
kinit developuser
source ~/.bashrc.anaconda
export PYSPARK_DRIVER_PYTHON="ipython"
export PYSPARK_DRIVER_PYTHON_OPTS="notebook --allow-root"
```

![image](https://user-images.githubusercontent.com/11695917/147119981-1118dd7e-0aac-44ec-b2e7-ede3211ad1a4.png)

Finally start the notebook:

```
pyspark --master yarn --deploy-mode client &
```

