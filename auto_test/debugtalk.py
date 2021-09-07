import datetime
import os
from os import environ
import random
import time
import requests
import yaml
import json
import pathlib

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


def get_token():
    get_params_value = {
        'client_id': 'creams_mobile_app',
        'grant_type': 'password',
        'password': 'Creams820',
        'username': '13787340624'
    }
    response = requests.post(url=login_url()+'/oauth/token', data=get_params_value, verify=False)
    return response.json()['access_token']


# 获取房态列表内房源面积、数量
def room_status():
    get_rooms_value = {
        'page': 0,
        'size': 1000,
        'beginDate': '2021-01-01',
        'endDate': '2021-12-31',
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'ROOM,CUBICLE'
    }
    headers = {'authorization': 'Bearer '+get_token()}
    response = requests.get(headers=headers, url=api_url()+'/buildings/rooms', params=get_rooms_value, verify=False)
    body = response.json()['content']
    sum_areaSize = 0
    sum_cubicle = 0
    for i in range(len(body)):
        room_size = body[i]['realAreaSize']
        sum_areaSize = room_size+sum_areaSize
        space_type = body[i]['spaceType']
        if space_type == 'CUBICLE':
            cubicle_count = len(body[i]['areaSize'])
            sum_cubicle = cubicle_count+sum_cubicle
    total_size = round(sum_areaSize, 2)
    total_count = len(body)
    total_cubicle = round(sum_cubicle, 2)
    return total_size, total_count, total_cubicle


def total_roomSize():
    total_size = room_status()[0]
    return total_size


def total_roomCount():
    total_conunt = room_status()[1]
    return total_conunt


def total_cubileCount():
    total_cubileCount = room_status()[2]
    return total_cubileCount


# 获取房源列表管理面积、房源数量
def room_list():
    get_rooms_value = {
        'page': 0,
        'size': 1000,
        'beginDate': '2021-01-01',
        'endDate': '2021-12-31',
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'ROOM'
    }
    headers = {'authorization': 'Bearer '+get_token()}
    response = requests.get(headers=headers, url=api_url()+'/buildings/rooms', params=get_rooms_value, verify=False)
    body = response.json()['content']
    sum_areaSize = 0
    for i in range(len(body)):
        room_size = body[i]['realAreaSize']
        sum_areaSize = room_size+sum_areaSize
    room_size = round(sum_areaSize, 2)
    room_count = len(body)
    return room_size, room_count


def room_Size():
    total_size = room_list()[0]
    return total_size


def room_Count():
    total_conunt = room_list()[1]
    return total_conunt


# 获取工位类型房源列表内房源面积、房源数量、工位数量
def cubicle_room():
    get_cubicle_rooms = {
        'page': 0,
        'size': 1000,
        'beginDate': '2021-01-01',
        'endDate': '2021-12-31',
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'CUBICLE'
    }
    headers = {'authorization': 'Bearer '+get_token()}
    response = requests.get(headers=headers, url=api_url()+'/buildings/rooms', params=get_cubicle_rooms, verify=False)
    body = response.json()['content']
    sum_areaSize = 0
    sum_cubicle = 0
    for i in range(len(body)):
        cubicle_room_size = body[i]['realAreaSize']
        sum_areaSize = cubicle_room_size+sum_areaSize
        cubicle_count = len(body[i]['areaSize'])
        sum_cubicle = cubicle_count+sum_cubicle
    cibicle_size = round(sum_areaSize, 2)
    cubicle_room_count = len(body)
    cubicle_num = round(sum_cubicle, 2)
    return cibicle_size, cubicle_room_count, cubicle_num


def cubileSize():
    cubile_size = cubicle_room()[0]
    return cubile_size


def cubicleRoom_count():
    cubicle_room_rount = cubicle_room()[1]
    return cubicle_room_rount


def cubicleNum():
    cubicle_num = cubicle_room()[2]
    return cubicle_num


# 获取房源+工位类型房源列表管理面积、房源数量、工位数量
def total_room_cubile():
    get_rooms_value = {
        'page': 0,
        'size': 1000,
        'loadOccupancyInfo': 'false',
        'loadRentingInfo': 'true',
        'buildingIds': 21568,
        'spaceTypes': 'ROOM,CUBICLE'
    }
    headers = {'authorization': 'Bearer '+get_token()}
    response = requests.get(headers=headers, url=api_url()+'/buildings/rooms', params=get_rooms_value, verify=False)
    body = response.json()['content']
    sum_areaSize = 0
    sum_cubicle = 0
    for i in range(len(body)):
        room_size = body[i]['realAreaSize']
        sum_areaSize = room_size+sum_areaSize
        space_type = body[i]['spaceType']
        if space_type == 'CUBICLE':
            cubicle_count = len(body[i]['areaSize'])
            sum_cubicle = cubicle_count+sum_cubicle
    room_cubice_size = round(sum_areaSize, 2)
    room_count = len(body)
    cubicle_num = round(sum_cubicle, 2)
    return room_cubice_size, room_count, cubicle_num


def room_cubicleSize():
    room_cubice_size = room_cubickeSize()[0]
    return room_cubice_size


def room_cubicleCount():
    room_cubicle_count = room_cubickeSize()[1]
    return room_cubicle_count


def room_cubicleNum():
    room_cubicle_num = room_cubicleSize()[2]
    return room_cubicle_num


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