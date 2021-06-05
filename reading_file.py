def file_reading():
    '''reads file and returns a list of it with \n sep members.'''
    with open('train_route_times.txt') as train_route:

        arr = []
        for x in train_route:
            arr.append(x)

    return arr
def train_and_stops(arr):
    '''takes the file as an arr in input and returns sublists with trains
    and their stops all together as a nested list'''
    temp = []
    train_with_their_stops = []
    temp_holding_train_name = ''
    for one_node in arr:
        if one_node != '\n':
            temp.append(one_node)

        elif one_node == '\n' and temp[:-1]:
            train_with_their_stops.append(temp[:-1])
            temp_holding_train_name = temp[-1]
            temp = [temp_holding_train_name]

    return train_with_their_stops

def stops_seperator(train_with_their_stops):
    '''this function returns a list which contains sublists
    of a train with their stops... completely formatted'''

    seperated_list = []
    for one_whole_chunk in train_with_their_stops:

        temp = [one_whole_chunk[0].strip('\n')]
        for individual_elements_index in range(len(one_whole_chunk)):

            if individual_elements_index > 0:
                modified_element = one_whole_chunk[individual_elements_index].split('\t')

                final_mod_element = []
                for stripping in modified_element:
                    stripping = stripping.strip(' ')
                    stripping = stripping.strip('\n')

                    if stripping: # checking if an element is empty .. if empty then not appending it

                        final_mod_element.append(stripping)

                temp.append(final_mod_element)

        seperated_list.append(temp)
    return seperated_list

def list_of_stops(arr, trains):
    '''returns all the list of stops currently in database'''
    stops_in_database = []
    for x in arr:
        for y in x:
            if type(y) == list and y[1] not in stops_in_database:

                stops_in_database.append(y[1])
    stops_in_database.sort()
    return stops_in_database


def list_of_trains(arr):
    '''returns a list containing all the trains currently in database'''
    trains_list = []
    for train in arr:
        trains_list.append(train[0])
    return trains_list

def add_nodes(dic, list_of_nodes):
    '''This function adds nodes to a dictionary'''
    for node in list_of_nodes:
        dic[node] = []

    return dic
def add_edges(dict, train_and_stops):

    for one_whole_chunk in train_and_stops:
        start = one_whole_chunk[0]
        for edges in one_whole_chunk:
            if edges != start:
                dict[start].append(edges)