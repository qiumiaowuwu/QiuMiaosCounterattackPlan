def display_message():
    print("函数")
display_message()

def favoritr_book(title):
    print( f'one of my favorote book is {title}')

favoritr_book('alice in wonderland')
favoritr_book('lalalal')

def describe_pet(name,type='dog'):
    print(f'{name} is a {type}')

describe_pet("xiaofeng",'cat')

def make_shirt(size,format):
    print(f'{size} is {format}')
make_shirt('xs','miao')

def make_shirt(size='l',format='i love python'):
    clothes = f'{size} is {format}'
    return clothes

mm=make_shirt()
print(mm)
make_shirt('m')
#print(mm1)

def city_country(city,country):
    local = f"{city},{country}"
    return  local.title()
m = city_country('beijing','china')
print(m)
m1 = city_country('chongqing','china')
print(m1)
m2 = city_country('shanghai','china')
print(m2)

def make_album(singer,album,qty=None):
    if qty:
        message = {"sin": singer, "alb": album,"q":qty}
    else:
         message = {"sin":singer, "alb":album}
    return message

m1 = make_album('feng','princes')
print(m1)
m1 = make_album('feng','princes','3')
print(m1)


def show_message(texts):
    for text in texts:
        print(text)


def send_message(texts,sends):
    while texts:
        text = texts.pop()
        sends.append(text)
    print(texts)
    print(sends)

texts =['lala','haha','yaya']
sends = []
show_message(texts)
send_message(texts,sends)


def send_message(texts,sends):
    while texts:
        text = texts.pop()
        sends.append(text)


texts =['lala','haha','yaya']
sends = []
show_message(texts)
send_message(texts[:],sends)
print(texts)
print(sends)
