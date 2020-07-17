import json
from pallycon.sample.watermark.pallycon_wm_api import execute

"""
THIS IS A SAMPLE CODE FOR GENERATE PallyCon HTTP API specification.
"""


def generate(**kwargs):
    print('data requested', json.dumps(kwargs, indent=4))

    # set the parameters for generate.
    site_id = kwargs.get('site_id')
    access_key = kwargs.get('access_key')
    site_key = kwargs.get('site_key')
    json_req = kwargs.get('json_req')

    # get a result using execute function from module `pallycon_wm_api`
    result = execute(site_id, access_key, site_key, json_req)

    print('result', json.dumps({'pallycon-apidata': result}, indent=4))


"""
you can customize ``json_req`` parameter.
as you can see below, the ``json_req`` should be a json string. 
either way is good for use, choose a version you prefer.
"""
json_str = {
    "storage_type": "S3",
    "region": "RG011"
}

# version 1
generate(site_id='<your site_id>',
         site_key='<your site_key>',
         access_key='<your access_key>',
         json_req='{"region": "RG011"}')

# version 2
generate(site_id='<your site_id>',
         site_key='<your site_key>',
         access_key='<your access_key>',
         json_req=json.dumps(json_str))
