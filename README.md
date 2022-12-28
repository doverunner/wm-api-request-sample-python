# pallycon-wm-api-request-sample

This sample is to get specification for PallyCon Watermark APIs for python
<br><br>

## Prerequisites

### Language

This works on `PYTHON` version :

- 3.7.x

<br>

### Virtual Environments

_**Virtual Environments**(a.k.a. `Envs`) must be established_ and do all the tasks in this Envs.

In this project we use `Anaconda 4.8.2` as Envs.


**how to install virtual environments?**  
If you are not familiar with Envs, see the list below and choose one out of this.  
Installation guide is here : [How to create virtual environments with venv and conda in Python
](https://lynn-kwong.medium.com/how-to-create-virtual-environments-with-venv-and-conda-in-python-31814c0a8ec2)


> list of virtual environments
> - Anaconda
> - miniconda
> - venv




<br>

### Libraries

For Anaconda users, create a virtual environment using `environment.yml` file and command.

`environment.yml` file :
```text
name: wm_api_request_sample {{or, set environment name}}
channels:
  - defaults
dependencies:
  - ca-certificates=2021.5.25
  - certifi=2021.5.30
  - openssl=1.1.1k
  - pip=21.1.2
  - pycrypto=2.6.1
  - python=3.7.10
  - pytz=2021.1
  - setuptools=52.0.0
  - sqlite=3.35.4
  - vc=14.2
  - vs2015_runtime=14.27.29016
  - wheel=0.36.2
  - wincertstore=0.2
prefix: {{set anaconda env directory}}
``` 

command :
```shell script
conda env create -f environment.yml
```
<br>

For other environments users, install packages using `requirements.txt`.
```text
certifi==2021.5.30
pycrypto==2.6.1
pytz==2021.1
wincertstore==0.2
```

<br><br>



## Quick Start

How to generate playback URL using the python script


### Step 1:

Open the sample.py file in an editor



### Step 2:

In the json_str enter the following:

```text

json_str = {
    "domain”:”sdfsdf.cloudfront.net",            //<<cloudfront url
    "output_path": “output”_video,               //<< S3 output folder path
    "cid": "BBB",                                //<< Content ID
    "streaming_format": "dash",                  //<<streaming format dash, hls
    "forensic_mark": “Watermark_Demo”,           //<< forensic watermark string
    "wmt_type": "aes",                           //<<watermark type aes
    "Prefix_folder": "wm-contents"               //<<wm-contents folder name
}
```


### Step 3:

After updating the json_str have the following code to generate watermark session URL

```text
generate(UrlInfo.SESSION_WATERMARK_URL_GENERATE,
         site_id=‘YZXX',
         site_key=‘32MYdSKheT3brD5y3njqFlMlCKyxRh1a',
         access_key=‘a2yx45EmY5djchcg71CTY8ay7upZ',
         json_req='{"region": "RG004"}')
```

### Step 4:

If python command line is being used then execute the command   
“Python sample.py”  
Or in anaconda execute the sample.py  script



### Step 5:

The output generated in step 4 would have a  url info for example:
```text
result {
    "description": "SESSION_WATERMARK_URL_GENERATE",

    "pallycon-apidata": "eyJkYXRhIjogImx6SlJTbGtKMVN6Rjg4cm5tdm\UtyK1pTdUl4a3pEMW52K2psUEE9IiwgInRpMDIyLTEyLTI2VDE1OjIxOjE1WiIsICJoYXNoIjogIkwzK0pCK1VzMWsrM1BDaWtMYzNETmQ4ekpScmk0ZVNwbTlVU21iSTFlMDQ9In0=",

    "url": "https://watermark.pallycon.com/api/v2/session/watermarkUrl/MOXX?pallycon-apidata=eyJkYXRmx6SlJTbGtKMVN6Rjg4cm5tdm83Qm1URUtyK1pTdUl4a3pEMW52K2psUEE9IiwgInRpbWVaWtMYzNETmQ4ekpScmk0ZVNwbTlVU21iSTFlMDQ9In0=",

    "method": "GET"
}
```

### Step 6:

Copy the url and paste it in browser to get the .playback mpd HLS url  
OR  
Use the GET method to fetch the playback mpd or HLS url.
