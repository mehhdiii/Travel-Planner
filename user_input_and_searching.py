from reading_file import *
from helper_functions import *
arr = file_reading()

stops_chunk = train_and_stops(arr) #list of stops as a chunk

sep_list = stops_seperator(stops_chunk) #sorted out list of stops

trains = list_of_trains(sep_list) #list containing the names of trains

trains_as_keys = add_nodes({}, trains) # dict creation of trains as keys

add_edges(trains_as_keys, sep_list)
# print(trains_as_keys)
# print(G)
stops_ = list_of_stops(sep_list, trains)
# print(stops_)

src = dict_containing_train_as_key(trains_as_keys, 'LAHORE JN.', {})
dst = dict_containing_train_as_key(trains_as_keys, 'KARACHI CITY', {})
# def common(src, dst):
#     for x in src:
#         for y in dst:

# print(src)
# print(dst)
# trains_at_starting_node = searching_stop_in_graph(G, 'SUKKUR')
#
# trains_at_end_node = searching_stop_in_graph(G, 'KARACHI CITY')

# print(trains_at_starting_node)
#
# print(trains_at_end_node)
# print(trains_as_keys)
# print(stops_)
# print(G['23UP Akber Express'])
# print('Enter Your current Stop:')
# starting = str(input())
#
# print('Enter Your Destination:')
# ending = str(input())
# print(stops_)
dic = {}
# print(dict_containing_train_as_key(G, stops_[0], dic))
city_as_keys = train_routes(trains_as_keys, stops_)
# print(city_as_keys)
Onetrains_path =  train_path(trains_as_keys, '23UP Akber Express')
# print(Onetrains_path)
all_routes = all_trains_with_connected_routes(trains_as_keys, trains)
connection_of_one_train_with_another = connecting_trains(all_routes, Onetrains_path, "23UP Akber Express")
# print(all_routes)
# print('\n\n\n\n\n\n\n\n')
# print(connection_of_one_train_with_another)


shortest_track = route_finder('GHOTKI', 'PESHAWAR CITY', all_routes, trains_as_keys)
# print(shortest_track)
back_trains, back_tracked_route, breaker = back_track(shortest_track)
# print(back_tracked_route)
route_with_time_final = route_with_time(trains_as_keys, back_trains, breaker, back_tracked_route)
print(route_with_time_final)





















# Total_tickets = tickets_to_buy(back_trains)
# print('You have to buy a total of',Total_tickets, 'Tickets', 'of Trains :', back_trains)

# if no path exists then the output should be the last node that it goes to and also a notification to the user
# making it user input based::::

# list_containing_all_breakpoints = input_function_for_user(stops_)
# print(list_containing_all_breakpoints)
# print(making_path_for_all_breakpoints(list_containing_all_breakpoints, all_routes, trains_as_keys))

# from gui import *
# print(gui_list_of_input)
# gui_lst = []
# for x in gui_list_of_input:
#     if x != 'STATION':
#         gui_lst.append(x)
# print(making_path_for_all_breakpoints(gui_lst, all_routes, trains_as_keys))