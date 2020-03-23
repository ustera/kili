import vk_api
import re
import pymorphy2


def inputlink():
    regex = r"vk\.com\/[0-9A-Za-z]+"
    result = None
    while result == None:
        a = input('Введите ссылку на группу VK в формате vk.com/xxx, где xxx - id группы: ')
        result = re.match(regex, a)
    return a


def subst (link):
    regex = r"(vk\.com\/)"
    subst = ""
    result = re.sub(regex, subst, link, 0, re.MULTILINE)
    if result:
        return result


def import_posts(name):
    #вставить свой токен
    session = vk_api.VkApi(token='0fd7c05ea20c0ba3079a9910ec4fb2cbcf972fbc43183b69b85296de4f34643f1273527999b93cabe6a06')
    vk = session.get_api()

    offset = 0
    c = 0
    post = []

    for i in range(0,50):
        data = vk.wall.get(domain=name, count=50, offset=offset)
        offset += 50
        for i in data['items']:
            post.append(i['text'])
            c += 1
            #sleep(20)

    return post


def pymorph(mas):
    morph = pymorphy2.MorphAnalyzer()
    text = re.sub('\W', ' ', mas).split()
    #выбрать какие строки нам нужны
    return

h = inputlink()
name = subst(h)
mas1 = import_posts(name)
print(mas1)