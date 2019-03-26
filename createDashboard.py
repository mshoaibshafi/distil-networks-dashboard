
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

    # Delete the CSV file at the first run or create daily versions
    if os.path.isfile(output_csv_file): 
        os.remove(output_csv_file)

    # TODO : Create Daily runs of csv file ... like csv_file.1, csv_file.2 ....

    # TODO : Create a header for the output_csv_file

    # Work Around  - should be removed after checking with Distil Tech Support
    # Issue  - "web security settings" REST API response has two dict items. 
    # Sometimes the first item has all the correct values where as the second one is all "null" or vice versa
    # So work around is 
    # Check for variable ajax_only for a reference - picked up this one as we are not using this one 
    # If ajax_only = null use the second item otherwise use the first item

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


            # Work around - explanation give above
            if w_info['web_security_settings'][0]['ajax_only'] == None:
                index = 1
            else:
                index = 0

            # Call XYZ

            # Create CSV File
            with open(output_csv_file,'a+') as ff:
                #ff.write("{},".format(len(w_info)))
                # domain name, domain ID and default origin server
                ff.write("{},{},{}".format(d[0],d[1],d[2]))

                # Machine Learning : Threshold and Action
                ff.write(",{},{}".format(w_info['web_security_settings'][index]['machine_learning_threshold'],\
                    w_info['web_security_settings'][index]['machine_learning_action']))

                # Rate Limiting :
                # Request per min : Value and Action
                ff.write(",{},{}".format(w_info['web_security_settings'][index]['requests_per_minute'],\
                    w_info['web_security_settings'][index]['requests_per_minute_action']))
                # Pages per sesssion : Value and Action
                ff.write(",{},{}".format(w_info['web_security_settings'][index]['requests_per_session'],\
                    w_info['web_security_settings'][index]['requests_per_session_action']))

                # Session Lenght : Value and Action
                ff.write(",{},{}".format(w_info['web_security_settings'][index]['session_length'],\
                    w_info['web_security_settings'][index]['session_length_action']))

                # Automated Threats Policy : Actions
                # known Violators, Identities
                # Aggregator User Agents
                # Known Violator Data Centers
                # Automated Browsers
                ff.write(",{},{}".format(w_info['web_security_settings'][index]['known_violators_action'],\
                    w_info['web_security_settings'][index]['bad_user_agent_action']))
                ff.write(",{},{},{}".format(w_info['web_security_settings'][index]['aggregator_user_agent_action'],\
                    w_info['web_security_settings'][index]['service_provider_action'],\
                    w_info['web_security_settings'][index]['javascript_action']))

                # Cache Enabled 
                ff.write(",{}".format(d_info['config_settings']['caching_enabled']))




                ff.write("\n")

            #input("Press any key to continue ... {}".format(d[0]))
