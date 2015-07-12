__author__ = 'Nick Mullen AKA CMDR Eld Ensar'

import json

#the systems.json file is obtained from EDDB and is updated nightly http://eddb.io/archive/v3/systems.json   So as not to cripple them (as systems don't move) I've cached a copy
with open('systems.json') as data_file:
    raw_data = json.load(data_file)!


#the winters_sysyems.json file is maintained locally
with open('winters_systems.json') as data_file2:
    winters_data = json.load(data_file2)

searched_count=0
found_count=0
fail_count=0
fail_list=[]
for cc_system in winters_data['control_systems']:
    searched_count += 1
    for search_system in raw_data:
        if search_system['name'] == cc_system['name']:
            print (cc_system['name'] + ", " + str(search_system['x']) + ", " + str(search_system['y']) + ", " + str(search_system['z']))
            found_count += 1
    if found_count + fail_count != searched_count:
        fail_list.append(cc_system['name'])
        fail_count += 1

if fail_count != 0:
    print("FAILURES OCCURRED FOR THE FOLLOWING SYSTEMS:", fail_list)
else:
    print("SUCCESSFUL RUN LOCATING", found_count, "SYSTEMS WITH NO ERRORS")

