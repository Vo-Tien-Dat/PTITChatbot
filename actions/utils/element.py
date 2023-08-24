def name_and_description_element(name, description): 
    element_pattern = '- {}: {}'.format(name, description)
    return element_pattern

def name_element(name):
    element_pattern = '- {}'.format(name)
    return element_pattern

def element_enumerate(data = [], start = 0 ):

    sub_enumerate = []
    sub_enumerate_pattern = '{}. {}'

    for index, value, in enumerate(data, start = start):
        sub_enumerate.append(sub_enumerate_pattern.format(index, value))

    return sub_enumerate