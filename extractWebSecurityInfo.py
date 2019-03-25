
import json,argparse,os,csv,requests,sys
from pprint import pprint

def extractWebSecurityInfo(accountId,domainId):
    # input = accountId, domainId ( distil domain ID)
    # output = return a full dictionary of web security information 

    # This program will extract all web security info about a particular domain 
    
    # Extract Cache enable or not value 
    # get https://api.distilnetworks.com/api/v1/platform/web_security_settings
    #  ?account_id=944ec01c-xxxxxxxxx
    #  &domain_id=09c97930-xxxxxx
    #  &auth_token=xxxxxxxxx
    

    # base url for domain search
    base = 'https://api.distilnetworks.com'

    # set the endpoint you need
    endpoint = '/api/v1/platform/web_security_settings'

    # construct the full target url
    target = base + endpoint   
    
    # set the Auth Token as an envrionment variable
    # $ export API_AUTH_TOKEN=844001-xx-yy-zz
    query = {'account_id' : accountId, 'domain_id': domainId, 'auth_token': os.environ.get('API_AUTH_TOKEN')}


    headers = {'content-type': 'application/json', 'Accept' : 'application/json'}

    r = requests.get(target, params=query, headers=headers)

    # convert json str to python dictionary 
    resp_data =  json.loads(json.dumps(r.json()))
    return resp_data
