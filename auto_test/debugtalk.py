import datetime
import logging
import os
from os import environ
import random
import time
import requests
import yaml
import json
import pathlib
import redis

from httprunner import __version__
root_path = os.path.abspath(__file__)
file_path = os.path.abspath(os.path.dirname(root_path)+os.path.sep+".")
env_path = os.path.join(os.path.abspath(os.path.dirname(root_path)+os.path.sep+'./'), '.env')
with open(env_path, 'r') as f:
    a = f.readline().replace("\n", "").split('=', 1)[1]
    l = f.readline().split('=', 1)[1]


def login_url():
    return l


def api_url():
    return a


r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)


def login():
    get_params_value = {
        'client_id': 'creams_mobile_app',
        'grant_type': 'password',
        'password': 'Creams820',
        'username': '13787340624'
    }
    response = requests.post(url=login_url()+'/oauth/token', data=get_params_value, verify=False)
    r.set('access_token', response.json()['access_token'])
    return response.json()['access_token']


def get_token():
    access_token = r.get('access_token')
    if access_token is None:
        access_token = login()
        return access_token
    else:
        return access_token


# 封装获取房源列表管理面积、房源数量、工位数量方法
def room_test(data):
    headers = {'authorization': 'Bearer '+get_token()}
    response = requests.get(headers=headers, url=api_url()+'/buildings/rooms', params=data, verify=False)
    body = response.json()['content']
    sum_areaSize = 0
    sum_cubicle = 0
    for i in range(len(body)):
        room_size = body[i]['realAreaSize']
        sum_areaSize = room_size + sum_areaSize
        space_type = body[i]['spaceType']
        cubicle_count = body[i]['areaSize']
        if space_type == 'CUBICLE':
            sum_cubicle = cubicle_count + sum_cubicle
    room_cubice_size = round(sum_areaSize, 2)
    room_count = len(body)
    cubicle_num = int(sum_cubicle)
    return room_cubice_size, room_count, cubicle_num


# 获取房态列表内房源面积、数量
def room_status():
    data = {
        'page': 0,
        'size': 1000,
        'beginDate': '2021-01-01',
        'endDate': '2021-12-31',
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'ROOM,CUBICLE'
    }
    body = room_test(data=data)
    return body


def total_roomSize():
    total_size = room_status()[0]
    return total_size


def total_roomCount():
    total_conunt = room_status()[1]
    return total_conunt


def total_cubileCount():
    total_cubileCount = room_status()[2]
    return total_cubileCount


# 获取房源+工位类型房源数据
def total_room_cubile():
    data = {
        'page': 0,
        'size': 1000,
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'ROOM,CUBICLE'
    }
    body = room_test(data=data)
    return body


def room_cubicleSize():
    room_cubice_size = total_room_cubile()[0]
    return room_cubice_size


def room_cubicleCount():
    room_cubicle_count = total_room_cubile()[1]
    return room_cubicle_count


def room_cubicleNum():
    room_cubicle_num = total_room_cubile()[2]
    return room_cubicle_num


# 获取工位类型房源列表内房源面积、房源数量、工位数量
def cubicle_room():
    data = {
        'page': 0,
        'size': 1000,
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'CUBICLE'
    }
    body = room_test(data=data)
    return body


def cubileSize():
    cubile_size = cubicle_room()[0]
    return cubile_size


def cubicleRoom_count():
    cubicle_room_count = cubicle_room()[1]
    return cubicle_room_count


def cubicleNum():
    cubicle_num = cubicle_room()[2]
    return cubicle_num


# 获取房源列表管理面积、房源数量
def room_list():
    data = {
        'page': 0,
        'size': 1000,
        'beginDate': '2021-01-01',
        'endDate': '2021-12-31',
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'ROOM'
    }
    body = room_test(data=data)
    return body


def room_Size():
    total_size = room_list()[0]
    return total_size


def room_Count():
    total_conunt = room_list()[1]
    return total_conunt


# 获取房源+工位中可招商房源数据
def availale_room_totalSize():
    data = {
        'page': 0,
        'size': 1000,
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'ROOM,CUBICLE',
        'available': 'true'
    }
    body = room_test(data=data)
    return body


def available_room_totalSize():
    available_room_totalsize = availale_room_totalSize()[0]
    return available_room_totalsize


def available_room_tatalCount():
    available_room_tatalcount = availale_room_totalSize()[1]
    return available_room_tatalcount


def available_room_totalNum():
    available_room_totalnum = availale_room_totalSize()[2]
    return available_room_totalnum


# 获取可招商房源数据
def availale_room_size():
    data = {
        'page': 0,
        'size': 1000,
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'ROOM',
        'available': 'true'
    }
    body = room_test(data=data)
    return body


def available_roomSize():
    available_room_size = availale_room_size()[0]
    return available_room_size


def available_roomCount():
    available_room_count = availale_room_size()[1]
    return available_room_count


def available_roomNum():
    available_room_num = availale_room_size()[2]
    return available_room_num


# 获取可招商工位房源数据
def availale_cubicle_size():
    data = {
        'page': 0,
        'size': 1000,
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'CUBICLE',
        'available': 'true'
    }
    body = room_test(data=data)
    return body


def available_cubicleSize():
    available_cubicle_size = availale_cubicle_size()[0]
    return available_cubicle_size


def available_cubicleCount():
    available_cubicle_count = availale_cubicle_size()[1]
    return available_cubicle_count


def available_cubicleNum():
    available_cubicle_num = availale_cubicle_size()[2]
    return available_cubicle_num


# 获取房源+工位中不可招商房源数据
def unavailale_room_totalSize():
    data = {
        'page': 0,
        'size': 1000,
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'ROOM,CUBICLE',
        'available': 'false'
    }
    body = room_test(data=data)
    return body


def unavailable_room_totalSize():
    unavailable_room_totalsize = unavailale_room_totalSize()[0]
    return unavailable_room_totalsize


def unavailable_room_totalCount():
    unavailable_room_totalcount = unavailale_room_totalSize()[1]
    return unavailable_room_totalcount


def unavailable_room_totalNum():
    unavailable_room_tatalnum = unavailale_room_totalSize()[2]
    return unavailable_room_tatalnum


# 获取不可招商房源数据
def unavailale_room_Size():
    data = {
        'page': 0,
        'size': 1000,
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'ROOM',
        'available': 'false'
    }
    body = room_test(data=data)
    return body


def unavailable_room_Size():
    unavailable_room_size = unavailale_room_Size()[0]
    return unavailable_room_size


def unavailable_room_Count():
    unavailable_room_count = unavailale_room_Size()[1]
    return unavailable_room_count


def unavailable_room_Num():
    unavailable_room_num = unavailale_room_Size()[2]
    return unavailable_room_num


# 获取不可招商工位房源数据
def unavailale_cubicle_Size():
    data = {
        'page': 0,
        'size': 1000,
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'CUBICLE',
        'available': 'false'
    }
    body = room_test(data=data)
    return body


def unavailable_cubicle_Size():
    unavailable_cubicle_size = unavailale_cubicle_Size()[0]
    return unavailable_cubicle_size


def unavailable_cubicle_Count():
    unavailable_cubicle_count = unavailale_cubicle_Size()[1]
    return unavailable_cubicle_count


def unavailable_cubicle_Num():
    unavailable_cubicle_num = unavailale_cubicle_Size()[2]
    return unavailable_cubicle_num


def set_contract_sh():
    contract_sh = {
        "auditElements": [],
        "id": 1497,
        "name": "系统默认审批配置"
    }
    response = requests.post(url=api_url()+'/oa/selection', json=contract_sh, verify=False)


def sum_float(x, y):
    return float(x)+float(y)


def wait(response, x):
    if response.status_code == 200 | response.status_code == 201:
        time.sleep(x)
    else:
        time.sleep(0.5)


def random_int(x, y):
    return random.randint(x, y)


def str_to_int(arg):
    return int(arg)


def int_to_str(arg):
    return str(arg)


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def reduce_two(m, n):
    return m - n


def begin_date():
    return datetime.datetime.now().strftime('%Y-%m-%d')


def begin_date_rw():
    m = datetime.datetime.now()+datetime.timedelta(days=1)
    return m.strftime('%Y-%m-%d')


def end_month():
    m = datetime.datetime.now()+datetime.timedelta(days=29)
    return m.strftime('%Y-%m-%d')


def end_date():
    a = datetime.datetime.now()+datetime.timedelta(days=364)
    return a.strftime('%Y-%m-%d')


def end_180():
    a = datetime.datetime.now()+datetime.timedelta(days=180)
    return a.strftime('%Y-%m-%d')


def sleep(n_secs):
    time.sleep(n_secs)