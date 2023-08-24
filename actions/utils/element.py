def name_and_description_element(name, description): 
    element_pattern = '- {}: {}'.format(name, description)
    return element_pattern

def name_element(name):
    element_pattern = '- {}'.format(name)
    return element_pattern