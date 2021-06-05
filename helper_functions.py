from reading_file import *
def dict_containing_train_as_key(G, stop, dict_of_train_with_time):
    '''returns train name with its timing and interval at which it will stop
    format: dictionary containing ==> stop : [trainname, time]'''
    if stop not in dict_of_train_with_time:
        dict_of_train_with_time[stop] = []

    for train in G:
        for sstop in G[train]:
            if sstop[1] == stop:

                dict_of_train_with_time[stop].append((train, sstop[2:]))
    return dict_of_train_with_time

def train_routes(G_containing_trains_and_routes, stops):
    '''returns a dict of cities as keys and trains as values with their timing'''
    all_routes = {}
    for stop_ in stops:
        dict_containing_train_as_key(G_containing_trains_and_routes, stop_, all_routes)
    return all_routes

# print(train_routes())
cities_as_keys={}
trains_as_keys={}
final_dict={} # {sample_city:[(sample_city, train_name, arrival, departure), ......]}


## now connect each city with others ::

#making seperate graph for each train so that they may be used for dfs

def train_path(dict_having_train_as_key, train_name):
    '''returns a tuple containing train_name and dict of all the cities it connects'''
    dfs_able_dictionary = {}

    for node__ in range( len(dict_having_train_as_key[train_name]) - 1): # this node contains all the information about the stop
       city = dict_having_train_as_key[train_name][node__][1]
       next = dict_having_train_as_key[train_name][node__ + 1][1]
       dfs_able_dictionary[city] = ''
       dfs_able_dictionary[city] = next
        # tuple_containing_train_and_dict = (train_name
    return train_name, dfs_able_dictionary

def all_trains_with_connected_routes(dict_having_train_as_key, list_of_trains):
    '''returns a list of tuples containing train names with a dict(city names as keys)'''
    all_route_arr = []
    for train in list_of_trains:
        all_route_arr.append(train_path(dict_having_train_as_key, train))
    return all_route_arr

# def connecting_trains(city_connections):
#     '''This fucntion connects each train with another train on the
#     basis of stations in common'''
#     previous_city = {}
#     current_city = {}
#     for train, dict_of_cities in city_connections:
#         previous_city = dict_of_cities

def connecting_trains(city_connections, dict_of_city_connections, train): # modify this to include a parameter for containing all the dicts of trains and ctities wala graph
    '''searches for a city in all of the dataset and connects train having same stops
    ***returns a dict having connected train with the stops which connect them '''
    connections = {train: []}
    for name, dict_ in city_connections:
        if name != train:
            for searching in dict_.values():

                if searching in dict_of_city_connections[1].values():
                    connections[train].append((name, searching))
    return connections


def route_finder(start_node, end_node, all_routes, trains_as_keys):
    #you need to call connecting trains function inside this function with the train name you want connected.

    possible_starting_trains = []
    for train, dict_ in all_routes:
        if start_node in dict_.keys():
            possible_starting_trains.append(train)

    # now for the difficult part of them all::
    # DONTYOUGIVEUP NANANA
    # searching throughout all the graphs so that
    # we can find all the paths to one station to another
    for train, dict_ in all_routes:
        if train in possible_starting_trains:
            flag_if_end_is_reached = False # this checks if the destination is found or not
            master_list_of_tracks = []
            stack = []
            visited = []
            trains_stack = [train]
            visited_trains = []
            stops_list = [start_node]
            #this runs dfs on all trains connected to each other
            while trains_stack:
                crnt_train = trains_stack.pop()
                visited_trains.append(crnt_train)
                # this is the block of code for dfs of one graph at a time
                stack = [stops_list.pop()]
                while stack:
                    current_stop = stack.pop()
                    if current_stop == end_node:

                        visited.append(current_stop)
                        master_list_of_tracks.append(visited)
                        return master_list_of_tracks, visited_trains
                    #adding neighbors:
                    for srch_for_train, _that_dict in all_routes:
                        if srch_for_train == crnt_train:
                            if current_stop in _that_dict.keys():

                                stack.append(_that_dict[current_stop])
                            else:
                                break
                    visited.append(current_stop)
                master_list_of_tracks.append(visited)
                visited_trains.append(crnt_train)
                visited = [] #reemptying visited for next
                #this code goes into the neighbouring trains and creates a list of them:

                onetrains_path = train_path(trains_as_keys, crnt_train)
                one_trains_connection_with_other = connecting_trains(all_routes, onetrains_path, crnt_train)
                connection_with_other = one_trains_connection_with_other[crnt_train]
                # now creating a list of trains that are to be visited next:
                for next_to_be_train, stop_ in connection_with_other:
                    if next_to_be_train not in trains_stack:

                        trains_stack.append(next_to_be_train)
                        stops_list.append(stop_)


def back_track(full_route):
    '''takes route finders output as input and returns a list of trains and list of stops to follow'''
    route, list_of_trains = full_route
    modified_trains = []
    for repetition in list_of_trains:
        if repetition not in modified_trains:
            modified_trains.append(repetition)
    final_route = []
    break_points = []

    if len(modified_trains) > 1:
        for r in range(len(route)-1):
            for element in range(len(route[r])):
                final_route.append(route[r][element])
                if route[r][element] == route[-1][-1]:
                    return final_route
                elif route[r][element] == route[r+1][0]:
                    break_points.append(route[r][element])
                    break
        for remaining in range(element, len(route[r+1])):
            final_route.append(route[r+1][remaining])
    else:
        for element_ in route[0]:
            final_route.append(element_)
    return modified_trains, final_route, break_points


def route_with_time(train_as_key, trains, breaker, list_of_stops):
    '''this function searches for the train in trains list and returns its timing and details'''
    list_containing_stops_with_time = []
    for tr in trains:
        for searching in train_as_key[tr]:
            if breaker !=[] and searching[1] == breaker[0]:
                list_containing_stops_with_time.append((tr, searching))
                list_of_stops.pop(0)
                breaker.pop()
                break
            elif searching[1] in list_of_stops:
                list_of_stops.pop(0)
                list_containing_stops_with_time.append((tr, searching))
    return list_containing_stops_with_time

def tickets_to_buy(trains):
    '''this function tells you how many tickets have to be bought by the user'''
    return len(trains)

def input_function_for_user(stops):
    '''inputs stops to break the journey at'''
    breaker = int(input('Enter number of stops you want to have in your journey:\n'))
    print('Select Stop to mark it as a break point')
    print(stops)
    list_of_breaks = []
    for running in range(breaker):
        temp = str(input())
        list_of_breaks.append(temp)
    return list_of_breaks

def making_path_for_all_breakpoints(list_of_breaks, all_routes, trains_as_keys):
    # creating combinations:
    master_list = []
    if len(list_of_breaks) > 1:

        for x in range(len(list_of_breaks) - 1):
                shortest_track = route_finder(list_of_breaks[x], list_of_breaks[x+1], all_routes, trains_as_keys)
                # print(shortest_track)
                back_trains, back_tracked_route, breaker = back_track(shortest_track)
                # print(back_tracked_route)
                route_with_time_final = route_with_time(trains_as_keys, back_trains, breaker, back_tracked_route)
                # print(route_with_time_final)
                # print('\n\n\n\n\n\n\n\n\n\n\n')
                master_list.append(route_with_time_final)
    return master_list