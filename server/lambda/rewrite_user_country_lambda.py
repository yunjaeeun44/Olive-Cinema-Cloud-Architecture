import os
 
def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']

    suffix = build_suffix(request['headers'])
    request['body']['viewer_country'] = suffix; 
    request['headers']['viewer_country'] = [{'key': 'viewer_country', 'value': suffix}]; 
    request['origin']['custom']['customHeaders'] = [{'key': 'viewer_country', 'value': suffix}]; 
    request['querystring'] = 'cc='+suffix
    request['uri'] = "/" + suffix.lower() + request['uri']
    print(event)
    return request
   
def build_suffix(headers):
    country = headers['cloudfront-viewer-country'][0]['value']
    return country