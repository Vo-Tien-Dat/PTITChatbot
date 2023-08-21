import requests 

from config import CONST_DOMAIN

def test():
    domain = '{}/admission/documents'.format(CONST_DOMAIN)
    message_pattern = "Bạn cần chuẩn bị những bô hồ sơ sau: {} "
    request = requests.get(domain)
    print('oke')
    try: 
        if request.status_code == 200:
            data = request.json()
            docs = [ doc.get('name') for doc in list(data['data'].values())]
            message = message_pattern.format((',').join(docs))
            print(message)
    except Exception as e: 
        print(e)
    
    return message_pattern
test()

    