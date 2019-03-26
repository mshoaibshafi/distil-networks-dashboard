# Input CSV File
# Output HTML Table

import os
import pandas as pd

def convertCSV2HTML():
    #TODO : Verify 'data' folder exist ?

    csv_file = 'data/distil.csv'
    output_distil_html_file = 'data/distil.html'
    
    # Delete the html file at the first run or create daily versions
    if os.path.isfile(output_distil_html_file):
    	os.remove(output_distil_html_file)



    # TODO : Create Daily runs of html file ... like distil_html.1 distil.html.2 ... 

    columns = ['Domain Name','domain id','BigIP VIP','machine_learning_threshold','machine_learning_action',\
				'requests_per_minute','requests_per_minute_action','requests_per_session','requests_per_session_action',\
				'session_length','session_length_action','known_violators_action','bad_user_agent_action','aggregator_user_agent_action',\
				'service_provider_action','javascript_action','caching_enabled']


    df = pd.read_csv(csv_file, names=columns)

    df.to_html(output_distil_html_file)







