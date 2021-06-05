##########################################################

## TARGET DICTIONARIES ##

#cities_as_keys={}
#trains_as_keys={}
#final_dict={} # {sample_city:[(sample_city, train_name, arrival, departure), ......]}

##########################################################

from reading_file import *
from helper_functions import *
arr = file_reading()

stops_chunk = train_and_stops(arr) #list of stops as a chunk
#print(stops_chunk)
sep_list = stops_seperator(stops_chunk) #sorted out list of stops
#print(sep_list)
trains = list_of_trains(sep_list) #list containing the names of trains
#print(trains)
trains_as_keys = add_nodes({}, trains) # dict creation of trains as keys
#print(trains_as_keys)
add_edges(trains_as_keys, sep_list)
#print(trains_as_keys) # This is the final version of the dict with train as keys
stops_ = list_of_stops(sep_list)
#print(stops_)

dic = {}

for i in stops_:
    dict_containing_stop_as_key(trains_as_keys, i, dic)
cities_as_keys=dic
#print(cities_as_keys)

final_dict = {}
final_dict=cities_to_cities_map(trains_as_keys, cities_as_keys, final_dict)
#print(final_dict['AB-I-GUM'])

################################################################################

required_path = []

print('Enter Your Starting Station:')
starting = input()
required_path.append(str(starting).upper())

def asking_for_stops():
    startOver = False
    for i in range(5):  
        print('Enter Your Stop No. '+str(i+1)+' (if there are no more stops, please enter "None"):')
        x=input()
        if i != 0 and (x == 'None' or x == 'none'):
            break
        elif i == 0 and (x == 'None' or x == 'none'):
            print('\nPlease Enter At Least One Stop\n')
            startOver = True
            break
        required_path.append(str(x).upper())
    if startOver == True:
        asking_for_stops()

asking_for_stops()
#required_path = list(zip(required_path, required_path[1:]))
print(required_path)

print(route_finder(required_path, final_dict))

################################################################################


## JUST PRESS F5 TO RUN THE PROGRAM ##
## ADD THE STOPS AS INPUT AND IT WILL GIVE ALL TRAINS BETWEEN THOSE STOPS ##
## RIGHT NOW THE LIMIT OF INPUT STOPS IS 6 BUT WE CAN ALWAYS INCREASE THAT ##


################################################################################
