
import json,os,requests,sys
from pprint import pprint

def extractDomains(accountId):
    # input = accountId ( distil account ID)
    # output = create a CSV file under data/domain_info conatins domain_name, domain_id, origin_server (bigip VIP ip)
    # required = It needs a folder name "data" to be created manually prior to run this script
    #            API_AUTH_TOKEN needs to be setup as an env variable prior to run this script
    

    # This program will extract all the domains info and create a csv file contains the following 
    # domain_name, domain_id, origin_server (bigip VIP ip)
    
    # TODO : Verify if 'data' folder exist
    filename = 'data/domain_info'

    # base url for domain search
    base = 'https://api.distilnetworks.com'

    # set the endpoint you need
    endpoint = '/api/v1/platform/domains'

    # construct the full target url
    target = base + endpoint

    # set the Auth Token as an envrionment variable
    # $ export API_AUTH_TOKEN=844001-xx-yy-zz
    query = {'account_id': accountId, 'auth_token': os.environ.get('API_AUTH_TOKEN')}
    

    headers = {'content-type': 'application/json', 'Accept' : 'application/json'}

    # Call REST API
    r = requests.get(target, params=query, headers=headers)

    # convert json str to python dictionary 
    resp_data =  json.loads(json.dumps(r.json()))

    # Open a file to store domain name , domain id , Origin server ip ( which is BigIP VIP IP )
    with open(filename, 'w') as file1:
        for i in range(0,len(resp_data['domains'])):
            file1.write("{},{},{}\n".format(resp_data['domains'][i]['name'],resp_data['domains'][i]['id'],resp_data['domains'][i]['default_origin_server']))

# Un comment below if you want to print the whole file at the end of this function 
#    with open(filename,'rt') as file2:
#        print(file2.read())

