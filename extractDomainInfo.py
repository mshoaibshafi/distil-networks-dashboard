
import json,os,csv,requests,sys
from pprint import pprint

def extractDomainInfo(domainId):
    # input = domainId ( distil domain ID)
    # output = return a full dictionary of domain information 

    # This program will extract all info about a particular domain 
    
    # Extract Cache enable or not value 
    # get /api/v1/platform/domains/{domain_id}/config_settings 

    # base url for domain search
    base = 'https://api.distilnetworks.com'

    # set the endpoint you need
    endpoint = '/api/v1/platform/domains/'

    # set the tail end 
    tailend = '/config_settings'

    # construct the full target url
    target = base + endpoint + domainId + tailend   

    # set the Auth Token as an envrionment variable
    # $ export API_AUTH_TOKEN=844001-xx-yy-zz
    query = {'auth_token': os.environ.get('API_AUTH_TOKEN')}
    #print ("target >> " + target)
    #print ("query >> " + query)
    #sys.exit()

    headers = {'content-type': 'application/json', 'Accept' : 'application/json'}

    r = requests.get(target, params=query, headers=headers)

    # convert json str to python dictionary 
    resp_data =  json.loads(json.dumps(r.json()))
    return resp_data
