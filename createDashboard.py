
import json,argparse,os,csv,requests,sys
from pprint import pprint
from extractDomainInfo import extractDomainInfo
from extractWebSecurityInfo import extractWebSecurityInfo


def createDashboard(accountID):
    # input account ID
    # output create a CSV file.

    # this function used in conjuction with extractDomain() function and extractDomainInfo() and extractWebSecurityInfo(()
    
    output_file = 'data/distil_dashboard.html'
    output_csv_file = 'data/distil.csv'
    input_file = 'data/domain_info'


    # TODO : check if data/domain_info file exist ?

    # TODO : Delete the CSV file at the first run or create daily versions
    # TODO : Create a header for the output_csv_file



    with open(input_file,'r') as f:
        # read the whole csv file into a list
        domainlist = csv.reader(f,delimiter=',')
        # d[0] - domain name like www.abcxyz.com
        # d[1] - distil domain ID
        # d[2] - default origin server
        for d in domainlist:
            print (d)
            # Call Domain Info
            d_info = extractDomainInfo(d[1])

            # Call extract Web Security 
            w_info = extractWebSecurityInfo(accountID,d[1])

            # Call XYZ

            # Create CSV File
            with open(output_csv_file,'a+') as ff:
                #ff.write("{},".format(len(w_info)))
                # domain name, domain ID and default origin server
                ff.write("{},{},{}".format(d[0],d[1],d[2]))

                # Machine Learning : Threshold and Action
                ff.write(",{},{}".format(w_info['web_security_settings'][0]['machine_learning_threshold'],\
                    w_info['web_security_settings'][0]['machine_learning_action']))

                # Rate Limiting :
                # Request per min : Value and Action
                ff.write(",{},{}".format(w_info['web_security_settings'][0]['requests_per_minute'],\
                    w_info['web_security_settings'][0]['requests_per_minute_action']))
                # Pages per sesssion : Value and Action
                ff.write(",{},{}".format(w_info['web_security_settings'][0]['requests_per_session'],\
                    w_info['web_security_settings'][0]['requests_per_session_action']))

                # Session Lenght : Value and Action
                ff.write(",{},{}".format(w_info['web_security_settings'][0]['session_length'],\
                    w_info['web_security_settings'][0]['session_length_action']))

                # Automated Threats Policy : Actions
                # known Violators, Identities
                # Aggregator User Agents
                # Known Violator Data Centers
                # Automated Browsers
                ff.write(",{},{}".format(w_info['web_security_settings'][0]['known_violators_action'],\
                    w_info['web_security_settings'][0]['bad_user_agent_action']))
                ff.write(",{},{},{}".format(w_info['web_security_settings'][0]['aggregator_user_agent_action'],\
                    w_info['web_security_settings'][0]['service_provider_action'],\
                    w_info['web_security_settings'][0]['javascript_action']))

                # Cache Enabled 
                ff.write(",{}".format(d_info['config_settings']['caching_enabled']))




                ff.write("\n")

            #input("Press any key to continue ... {}".format(d[0]))
