from reading_file import *
def dict_containing_stop_as_key(trains_as_keys, stop, dic):
    '''returns train name with its timing and interval at which it will stop
    format: dictionary containing ==> stop : [trainname, time]'''
    if stop not in dic:
        dic[stop] = []

    for train in trains_as_keys:
        for sstop in trains_as_keys[train]:
            if sstop[1] == stop:

                dic[stop].append((train, sstop[2:]))
    return dic


def cities_to_cities_map(trains_as_keys, cities_as_keys, final_dict):
    '''makes the cities to cities map as discussed'''
    for src_city in cities_as_keys.keys(): #this loop iterates over every stop/city
        final_dict[src_city]=[]
        for src_train in cities_as_keys[src_city]:  #iterates over all of the trains that pass through the src_city
            for train in trains_as_keys.keys(): #iterates over all trains
                if src_train[0] == train: #finds matching train in trains_as_keys
                    for dst_city in range(len(trains_as_keys[train])): #iterates over the dst_cities
                        if trains_as_keys[train][dst_city][1] == src_city:
                            for dst_city_ in trains_as_keys[train][(dst_city+1):]:
        #                        if dst_city_[3] > src_train[1][0]:
                                x=[]
                                x.append(dst_city_[1])
                                x.append(train)
                                x.extend(dst_city_[2:])
                                final_dict[src_city].append(x)
    return final_dict
''' The format of this final dictionary is
--> {src_city:[[dst_city, train, time1, time2], ...], ...}'''



##def push(lst, item):
##    lst.append(item)
##
##def pop(lst):
##    return(lst.pop())
##
##def top(lst):
##    return(lst[-1])
##
##def is_empty(lst):
##    if len(lst)==0:
##        return(True)
##    else:
##        return(False)
##    
##def route_finder(required_path, final_dict):
##    check_stack=required_path[::-1]
##    possible_starting_trains = []
##    while check_stack:
##        for src_city in final_dict[top(check_stack)]:
##            pop(check_stack)
##            if is_empty(check_stack)==True:
##                return possible_starting_trains
##            elif src_dst[0] == top(check_stack):
##                push(possible_starting_trains, src_dst)
##    return possible_starting_trains
        
def route_finder(required_path, final_dict):
    possible_trains = {}
    temp = []
    root = required_path[0]
    copy = required_path[1:]
    for i in copy:
        possible_trains[str(root)+' to '+str(i)]=[]
        for j in final_dict[root]:
            if j[0] == i:
                possible_trains[str(root)+' to '+str(i)].append(j[1:])
        root = i
    return possible_trains

        
        
