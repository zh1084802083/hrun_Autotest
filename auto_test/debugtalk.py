import datetime
import random
import time
import requests
import yaml
import json

from httprunner import __version__


def get_token():
    get_params_value = {
        'client_id': 'creams_mobile_app',
        'grant_type': 'password',
        'password': 'Creams820',
        'username': '13787340624'
    }
    response = requests.post(url='https://rc-accounts.creams.io/oauth/token', data=get_params_value, verify=False)
    return response.json()['access_token']


def set_contract_sh():
    contract_sh = {
        "auditElements": [],
        "id": 1497,
        "name": "系统默认审批配置"
    }
    response = requests.post(url='https://rc-app.creams.io/api/web/oa/selection', json=contract_sh, verify=False)


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
    a = datetime.datetime.now()+datetime.timedelta(days=182)
    return a.strftime('%Y-%m-%d')


def sleep(n_secs):
    time.sleep(n_secs)