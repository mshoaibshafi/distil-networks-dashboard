
import json,argparse,os,csv,requests,sys


def findDomainID(domain_name):
    # input domain name
    # output dommain id

    # this used in conjuction with extractDomain() function
    # this function rely on the CSV file created by extractDomain function

    filename = 'data/domain_info'

    with open(filename,'r') as f:
        # read the whole csv file into a list
        domainlist = csv.reader(f,delimiter=',')
        for row in domainlist:
            # if domain name matches then returns its ID
            if row[0] == domain_name:
                return row[1]
        return None
