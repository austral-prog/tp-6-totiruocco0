def remove_elements(removeele):
    return removeele[1:4] + removeele[7:]

def add_elements(listadd):

    return ["Pink"] + listadd + ["Yellow"]

def is_empty(list_to_check):
    if list_to_check == []:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    if list_to_compare1[2:3] == [] or list_to_compare2[2:3] == []:
        return False
    elif list_to_compare1[2:3] == list_to_compare2[2:3]:
        return True




def list_of_lists(listss):
    return [listss[0][0:2]] + [listss[1][1:4]] + [listss[2][-2:]]
