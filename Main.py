
import os,csv,requests,sys
from pprint import pprint
#from extractDomain import extractDomain
#from findDomainID import findDomainID
#from extractDomainInfo import extractDomainInfo
#from extractWebSecurityInfo import extractWebSecurityInfo
#from createDashboard import createDashboard

# set the account ID as an envrionment variable
# $ export Account_ID=844001-xx-yy-zz
accountId = os.environ.get('Account_ID')
#print (accountId)
#sys.exit()
#domain_name = None
#domain_name = 'meridianshenkman.evenue.net'
domain_name ='ev1.evenue.net'
#domain_name = 'theborgata.evenue.net'

#extractDomain(accountId)
domain_ID = findDomainID(domain_name)

print (".. {} >> {}".format(domain_name,domain_ID))

d_info = extractDomainInfo(findDomainID(domain_name))

#pprint (d_info)

#print ("\n\n=================================================================\n\n")

w_info = extractWebSecurityInfo(accountId,findDomainID(domain_name))

#pprint (w_info)
#print ("{} ".format(w_info['config_settings']))
# Next is to create a function that will take both d_info and w_info and create a dash board 


createDashboard(domain_name,d_info,w_info)