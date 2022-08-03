# pallycon-wm-api-request-sample

This sample is to get specification for PallyCon Watermark APIs for python
<br><br>

## Prerequisites

### Language

This works on `PYTHON` version :

- 3.7.6 and greater

<br>

### IDE

- PyCharm
- Anaconda 4.8.2

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

Clone this git repository and go to the `sample.py`. This code below is from `sample.py`.

**NOTE**
See `UrlInfo` enum class for request url and it's method.

```python
import json
from pallycon.sample.watermark.pallycon_wm_api import execute
from pallycon.sample.config.url_info import UrlInfo

"""
THIS IS A SAMPLE CODE FOR GENERATE PallyCon HTTP API specification.
"""


def generate(request_url: UrlInfo, **kwargs):
    print('data requested', json.dumps(kwargs, indent=4))

    # set the parameters for generate.
    site_id = kwargs.get('site_id')
    access_key = kwargs.get('access_key')
    site_key = kwargs.get('site_key')
    json_req = kwargs.get('json_req')

    # get a result using execute function from module `pallycon_wm_api`
    api_data_str = execute(site_id, access_key, site_key, json_req)

    result = request_url.request_url_method(api_data_str, site_id)
    print('result', json.dumps(result, indent=4))


json_str = {
    "storage_type": "S3",
    "region": "RG011"
}

# Sample Code
generate(UrlInfo.PACK_JOB_LIST,
         site_id='TUTO',
         site_key='lU5D8s3PWoLls3PWFWkClULlFWk5D8oC',
         access_key='LT2FVJDp2Xr018zf4Di6lzvNOv3DKP20',
         json_req=json.dumps(json_str))

```
<br>

#### Result of quick start

```
data requested {
    "site_id": "TUTO",
    "site_key": "lU5D8s3PWoLls3PWFWkClULlFWk5D8oC",
    "access_key": "LT2FVJDp2Xr018zf4Di6lzvNOv3DKP20",
    "json_req": "{\"storage_type\": \"S3\", \"region\": \"RG011\"}"
}
result {
    "description": "DETECT_REGISTER",
    "pallycon-apidata": "eyJkYXRhIjogIjFoY0crOUhMckR1ZWlJTjlDWXQ4SVNvekIzY0x6Zy9Db2VHNE5PKzY2cW9WRWo5eEJ1S2JzZkNUaVM3KzZrWWoiLCAidGltZXN0YW1wIjogIjIwMjItMDMtMzBUMDg6Mjk6NTdaIiwgImhhc2giOiAibWlUaUxSbmh5ZnBWdmEyZHlVbXdHVHI1VzV3NUpkRmFrbnl0YXdFNTVzaz0ifQ==",
    "url": "https://api.pallycon.com/api/v2/detect/TUTO/url?pallycon-apidata=eyJkYXRhIjogIjFoY0crOUhMckR1ZWlJTjlDWXQ4SVNvekIzY0x6Zy9Db2VHNE5PKzY2cW9WRWo5eEJ1S2JzZkNUaVM3KzZrWWoiLCAidGltZXN0YW1wIjogIjIwMjItMDMtMzBUMDg6Mjk6NTdaIiwgImhhc2giOiAibWlUaUxSbmh5ZnBWdmEyZHlVbXdHVHI1VzV3NUpkRmFrbnl0YXdFNTVzaz0ifQ==",
    "method": "POST"
}
```


<br><br>

### HOW IT WORKS ?

If want to see how it works, go to module  `pallycon.sample.watermark.pallycon_wm_api`. On the top of this module, there is a simple note how it works.

> 1. get `site_id`, `access_key`, `site_key`, and `json_req`
> 2. encrypt `json_req` with `_make_data()`.
> 3. make `timestamp` with `_make_timestamp()`.
> 4. make `hash` with `_make_hash()`.
> 5. return PallyCon Watermark API specificated String from the values `#2 ~ #4`

<br><br><br><br><br><br>

