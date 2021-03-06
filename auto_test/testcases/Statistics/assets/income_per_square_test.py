# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/Statistics/assets/income_per_square.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.Buildings.buildings_test import TestCaseBuildings as Buildings


class TestCaseIncomePerSquare(HttpRunner):

    config = (
        Config("数据舱-平效统计")
        .variables(
            **{
                "beginDate": "2021-01-01",
                "endDate": "2021-12-31",
                "access_token": "${get_token()}",
            }
        )
        .export(*["building_id"])
    )

    teststeps = [
        Step(RunTestCase("获取楼宇id").call(Buildings).export(*["building_id"])),
        Step(
            RunRequest("创建房源-1")
            .post("${ENV(api_url)}/buildings/$building_id/rooms")
            .with_headers(
                **{
                    "accept": "application/json",
                    "authorization": "Bearer $access_token",
                }
            )
            .with_json(
                {
                    "areaSize": 100,
                    "buildingId": "$building_id",
                    "cubicleUpdateRequests": [],
                    "floorName": "1",
                    "jsonData": '[{"required":false,"fieldName":"建筑面积","fieldType":"NUMBER","systemField":true},{"required":false,"fieldName":"装修","fieldType":"SINGLE_SELECT","values":["不限","毛坯","简装","精装"],"systemField":true},{"required":false,"fieldName":"预租单价","fieldType":"NUMBER","systemField":true}]',
                    "marketingAvailable": "true",
                    "realAreaSize": 100,
                    "roomNumber": 101,
                    "spaceType": "ROOM",
                }
            )
            .teardown_hook("${wait(1)}")
            .extract()
            .with_jmespath("body", "room_id")
            .validate()
            .assert_equal("status_code", 201)
        ),
        Step(
            RunRequest("创建房源-2")
            .post("${ENV(api_url)}/buildings/$building_id/rooms")
            .with_headers(
                **{
                    "accept": "application/json",
                    "authorization": "Bearer $access_token",
                }
            )
            .with_json(
                {
                    "areaSize": 120.5,
                    "buildingId": "$building_id",
                    "cubicleUpdateRequests": [],
                    "floorName": "1",
                    "jsonData": '[{"required":false,"fieldName":"建筑面积","fieldType":"NUMBER","systemField":true},{"required":false,"fieldName":"装修","fieldType":"SINGLE_SELECT","values":["不限","毛坯","简装","精装"],"systemField":true},{"required":false,"fieldName":"预租单价","fieldType":"NUMBER","systemField":true}]',
                    "marketingAvailable": "true",
                    "realAreaSize": 120.5,
                    "roomNumber": 102,
                    "spaceType": "ROOM",
                }
            )
            .teardown_hook("${wait(1)}")
            .validate()
            .assert_equal("status_code", 201)
        ),
        Step(
            RunRequest("创建工位类型房源")
            .post("${ENV(api_url)}/buildings/$building_id/rooms")
            .with_headers(
                **{
                    "accept": "application/json",
                    "authorization": "Bearer $access_token",
                }
            )
            .with_json(
                {
                    "areaSize": 50.5,
                    "buildingId": "$building_id",
                    "cubicleUpdateRequests": [
                        {
                            "number": "1",
                            "marketingAvailable": "true",
                            "jsonData": '[{"desc":"工位朝向","values":["朝北","朝南","朝西","朝东"],"fieldName":"工位朝向","fieldType":"SINGLE_SELECT"},{"desc":"天字号工位","fieldName":"天字号工位","fieldType":"SINGLE_TEXT"}]',
                        },
                        {
                            "number": "2",
                            "marketingAvailable": "true",
                            "jsonData": '[{"desc":"工位朝向","values":["朝北","朝南","朝西","朝东"],"fieldName":"工位朝向","fieldType":"SINGLE_SELECT"},{"desc":"天字号工位","fieldName":"天字号工位","fieldType":"SINGLE_TEXT"}]',
                        },
                        {
                            "number": "3",
                            "marketingAvailable": "true",
                            "jsonData": '[{"desc":"工位朝向","values":["朝北","朝南","朝西","朝东"],"fieldName":"工位朝向","fieldType":"SINGLE_SELECT"},{"desc":"天字号工位","fieldName":"天字号工位","fieldType":"SINGLE_TEXT"}]',
                        },
                        {
                            "number": "4",
                            "marketingAvailable": "true",
                            "jsonData": '[{"desc":"工位朝向","values":["朝北","朝南","朝西","朝东"],"fieldName":"工位朝向","fieldType":"SINGLE_SELECT"},{"desc":"天字号工位","fieldName":"天字号工位","fieldType":"SINGLE_TEXT"}]',
                        },
                        {
                            "number": "5",
                            "marketingAvailable": "true",
                            "jsonData": '[{"desc":"工位朝向","values":["朝北","朝南","朝西","朝东"],"fieldName":"工位朝向","fieldType":"SINGLE_SELECT"},{"desc":"天字号工位","fieldName":"天字号工位","fieldType":"SINGLE_TEXT"}]',
                        },
                    ],
                    "floorName": "2",
                    "jsonData": '[{"required":false,"fieldName":"建筑面积","fieldType":"NUMBER","systemField":true},{"required":false,"fieldName":"装修","fieldType":"SINGLE_SELECT","values":["不限","毛坯","简装","精装"],"systemField":true},{"required":false,"fieldName":"预租单价","fieldType":"NUMBER","systemField":true}]',
                    "marketingAvailable": "true",
                    "realAreaSize": 50.5,
                    "roomNumber": 201,
                    "spaceType": "CUBICLE",
                }
            )
            .teardown_hook("${wait(1)}")
            .extract()
            .with_jmespath("body", "cubicle_room_id")
            .validate()
            .assert_equal("status_code", 201)
        ),
        Step(
            RunRequest("获取工位类型房源中的工位")
            .get("${ENV(api_url)}/buildings/room/$cubicle_room_id/cubicles")
            .with_headers(**{"authorization": "Bearer $access_token"})
            .extract()
            .with_jmespath("body[0].id", "cubicleId_1")
            .with_jmespath("body[1].id", "cubicleId_2")
            .with_jmespath("body[2].id", "cubicleId_3")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("生成房源合同租金明细")
            .post("${ENV(api_url)}/v2/contracts/pays")
            .with_headers(**{"authorization": "Bearer $access_token"})
            .with_json(
                {
                    "baseTerm": {
                        "areaSize": 100,
                        "calculateOrder": "AREA_FIRST",
                        "deposit": 1,
                        "depositPayEnumDesc": "租金保证金",
                        "depositUnitEnum": "MONTH",
                        "leaseBeginDate": "2021-09-01",
                        "leaseEndDate": "2021-09-30",
                        "monetaryUnit": "人民币CNY",
                        "precisionEnum": "RESULT",
                        "signDate": "2021-09-01",
                        "spaceUnit": "P",
                        "theoryRounded": False,
                        "unitPricePrecision": 2,
                    },
                    "depositIncreasingRates": [],
                    "discounts": [],
                    "increasingRates": [],
                    "leaseTerms": [
                        {
                            "calculateEnum": "MONTH",
                            "dayNumberForYear": 365,
                            "deposit": False,
                            "intervalMonth": 1,
                            "leaseComputeWay": "FIXED_MONEY",
                            "leaseDivideRoleEnum": "NORMAL",
                            "leaseTermType": "RENT",
                            "leaseTermTypeDesc": "租金",
                            "monetaryUnit": "人民币CNY",
                            "payInAdvanceDay": 1,
                            "paymentDateEnum": "WORKDAY",
                            "price": 1,
                            "priceUnitEnum": "D",
                            "termBeginDate": "2021-09-01",
                            "termEndDate": "2021-09-30",
                        }
                    ],
                }
            )
            .extract()
            .with_jmespath("body", "contractPays")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("新建房源合同--按面积计算租金(不付款)")
            .post("${ENV(api_url)}/v3/contracts?")
            .with_headers(
                **{
                    "authorization": "Bearer $access_token",
                    "content-type": "application/json; charset=utf-8",
                }
            )
            .with_json(
                {
                    "baseTerm": {
                        "areaSize": 100,
                        "calculateOrder": "AREA_FIRST",
                        "contractNo": "001",
                        "leaseBeginDate": "2021-09-01",
                        "leaseEndDate": "2021-09-30",
                        "precisionEnum": "RESULT",
                        "signDate": "2021-09-01",
                        "spaceUnit": "P",
                        "theoryRounded": False,
                        "unitPricePrecision": 2,
                    },
                    "contractNo": "001",
                    "customKeywords": [],
                    "expenseTerms": [
                        {
                            "areaSize": 100,
                            "buildingType": "OFFICE",
                            "contractExpenseTermName": "租赁条款",
                            "contractPays": "$contractPays",
                            "deposit": 1,
                            "depositIncreasingRates": [],
                            "depositUnitEnum": "MONTH",
                            "discounts": [],
                            "expenseTermType": "RENT_TERM",
                            "increasingRates": [],
                            "itemPermission": "RENT_PERMISSION",
                            "leaseTerms": [
                                {
                                    "calculateEnum": "MONTH",
                                    "dayNumberForYear": 365,
                                    "deposit": False,
                                    "intervalMonth": 1,
                                    "leaseComputeWay": "FIXED_MONEY",
                                    "leaseDivideRoleEnum": "NORMAL",
                                    "leaseTermType": "RENT",
                                    "leaseTermTypeDesc": "租金",
                                    "monetaryUnit": "人民币CNY",
                                    "payInAdvanceDay": 1,
                                    "paymentDateEnum": "WORKDAY",
                                    "price": 1,
                                    "priceUnitEnum": "D",
                                    "termBeginDate": "2021-09-01",
                                    "termEndDate": "2021-09-30",
                                }
                            ],
                            "monetaryUnit": "人民币CNY",
                            "resourceIds": ["$room_id"],
                            "resourceType": "ROOM",
                            "spaceUnit": "P",
                            "termIndex": 1,
                        }
                    ],
                    "followId": 4990,
                    "followName": "13787340624",
                    "jsonData": "[]",
                    "legalPerson": {"name": "李传根"},
                    "remarkTerms": [],
                    "resourceIds": ["$room_id"],
                    "resourceType": "ROOM",
                    "tags": [],
                    "tenantId": 78327,
                    "tenantName": "湖南神雀网络科技有限公司",
                    "tenantNo": None,
                }
            )
            .extract()
            .with_jmespath("body", "contract_id")
            .validate()
            .assert_equal("status_code", 201)
        ),
        Step(
            RunRequest("提交房源合同")
            .setup_hook("${set_contract_sh()}")
            .post("${ENV(api_url)}/oa/start")
            .with_headers(
                **{
                    "accept": "application/json",
                    "authorization": "Bearer $access_token",
                }
            )
            .with_json(
                {
                    "buildingIds": ["$building_id"],
                    "subDomainType": "NEW_APPROVAL",
                    "domainType": "CONTRACT",
                    "customerId": 1013,
                    "description": "湖南神雀网络科技有限公司/测试楼宇/101",
                    "objectId": "$contract_id",
                }
            )
            .teardown_hook("${wait(2)}")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("生成工位合同租金明细")
            .post("${ENV(api_url)}/v2/contracts/pays")
            .with_headers(**{"authorization": "Bearer $access_token"})
            .with_json(
                {
                    "baseTerm": {
                        "areaSize": 3,
                        "calculateOrder": "AREA_FIRST",
                        "deposit": 1,
                        "depositPayEnumDesc": "租金保证金",
                        "depositUnitEnum": "MONTH",
                        "leaseBeginDate": "2021-09-01",
                        "leaseEndDate": "2021-09-30",
                        "monetaryUnit": "人民币CNY",
                        "precisionEnum": "RESULT",
                        "signDate": "2021-09-01",
                        "spaceUnit": "G",
                        "theoryRounded": False,
                        "unitPricePrecision": 2,
                    },
                    "depositIncreasingRates": [],
                    "discounts": [],
                    "increasingRates": [],
                    "leaseTerms": [
                        {
                            "calculateEnum": "MONTH",
                            "dayNumberForYear": 365,
                            "deposit": False,
                            "intervalMonth": 1,
                            "leaseComputeWay": "FIXED_MONEY",
                            "leaseDivideRoleEnum": "NORMAL",
                            "leaseTermType": "RENT",
                            "leaseTermTypeDesc": "租金",
                            "monetaryUnit": "人民币CNY",
                            "payInAdvanceDay": 1,
                            "paymentDateEnum": "WORKDAY",
                            "price": 10,
                            "priceUnitEnum": "GD",
                            "termBeginDate": "2021-09-01",
                            "termEndDate": "2021-09-30",
                        }
                    ],
                }
            )
            .extract()
            .with_jmespath("body", "contract_cubiclePays")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("新建工位合同--按工位数计算租金(不付款)")
            .post("${ENV(api_url)}/v3/contracts?")
            .with_headers(
                **{
                    "authorization": "Bearer $access_token",
                    "content-type": "application/json; charset=utf-8",
                }
            )
            .with_json(
                {
                    "baseTerm": {
                        "areaSize": 3,
                        "calculateOrder": "AREA_FIRST",
                        "contractNo": "001",
                        "leaseBeginDate": "2021-09-01",
                        "leaseEndDate": "2021-09-30",
                        "precisionEnum": "RESULT",
                        "signDate": "2021-09-01",
                        "spaceUnit": "G",
                        "theoryRounded": False,
                        "unitPricePrecision": 2,
                    },
                    "contractNo": "001",
                    "customKeywords": [],
                    "expenseTerms": [
                        {
                            "areaSize": 3,
                            "buildingType": "OFFICE",
                            "contractExpenseTermName": "租赁条款",
                            "contractPays": "$contract_cubiclePays",
                            "deposit": 1,
                            "depositIncreasingRates": [],
                            "depositUnitEnum": "MONTH",
                            "discounts": [],
                            "expenseTermType": "RENT_TERM",
                            "increasingRates": [],
                            "itemPermission": "RENT_PERMISSION",
                            "leaseTerms": [
                                {
                                    "calculateEnum": "MONTH",
                                    "dayNumberForYear": 365,
                                    "deposit": False,
                                    "intervalMonth": 1,
                                    "leaseComputeWay": "FIXED_MONEY",
                                    "leaseDivideRoleEnum": "NORMAL",
                                    "leaseTermType": "RENT",
                                    "leaseTermTypeDesc": "租金",
                                    "monetaryUnit": "人民币CNY",
                                    "payInAdvanceDay": 1,
                                    "paymentDateEnum": "WORKDAY",
                                    "price": 10,
                                    "priceUnitEnum": "GD",
                                    "termBeginDate": "2021-09-01",
                                    "termEndDate": "2021-09-30",
                                }
                            ],
                            "monetaryUnit": "人民币CNY",
                            "resourceIds": [
                                "$cubicleId_1",
                                "$cubicleId_2",
                                "$cubicleId_3",
                            ],
                            "resourceType": "CUBICLE",
                            "spaceUnit": "G",
                            "termIndex": 1,
                        }
                    ],
                    "followId": 4990,
                    "followName": "13787340624",
                    "jsonData": "[]",
                    "legalPerson": {"name": "李传根"},
                    "remarkTerms": [],
                    "resourceIds": ["$cubicleId_1", "$cubicleId_2", "$cubicleId_3"],
                    "resourceType": "CUBICLE",
                    "tags": [],
                    "tenantId": 78327,
                    "tenantName": "湖南神雀网络科技有限公司",
                    "tenantNo": None,
                }
            )
            .extract()
            .with_jmespath("body", "contract_cubicleId")
            .validate()
            .assert_equal("status_code", 201)
        ),
        Step(
            RunRequest("提交工位合同")
            .setup_hook("${set_contract_sh()}")
            .post("${ENV(api_url)}/oa/start")
            .with_headers(
                **{
                    "accept": "application/json",
                    "authorization": "Bearer $access_token",
                }
            )
            .with_json(
                {
                    "buildingIds": ["$building_id"],
                    "subDomainType": "NEW_APPROVAL",
                    "domainType": "CONTRACT",
                    "customerId": 1013,
                    "description": "湖南神雀网络科技有限公司/自动化测试楼宇/201",
                    "objectId": "$contract_cubicleId",
                }
            )
            .teardown_hook("${wait(2)}")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("数据舱-平效-房源-租金、按月")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ROOM",
                    "temporalUnit": "MONTH",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[8].data", 0.46)
        ),
        Step(
            RunRequest("数据舱-平效-房源-租金+物业费、按月")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金,物业费",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ROOM",
                    "temporalUnit": "MONTH",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[8].data", 0.46)
        ),
        Step(
            RunRequest("数据舱-平效-房源-按月")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ROOM",
                    "temporalUnit": "MONTH",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[8].data", 0.46)
        ),
        Step(
            RunRequest("数据舱-平效-工位-租金、按月")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "CUBICLE",
                    "temporalUnit": "MONTH",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[8].data", 6.08)
        ),
        Step(
            RunRequest("数据舱-平效-工位-租金+物业费、按月")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金,物业费",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "CUBICLE",
                    "temporalUnit": "MONTH",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[8].data", 6.08)
        ),
        Step(
            RunRequest("数据舱-平效-工位、按月")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "CUBICLE",
                    "temporalUnit": "MONTH",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[8].data", 6.08)
        ),
        Step(
            RunRequest("数据舱-平效-房源+工位-租金-按月")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ALL",
                    "temporalUnit": "MONTH",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[8].data", 0.49)
        ),
        Step(
            RunRequest("数据舱-平效-房源+工位-租金+物业费-按月")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金,物业费",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ALL",
                    "temporalUnit": "MONTH",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[8].data", 0.49)
        ),
        Step(
            RunRequest("数据舱-平效-房源+工位-按月")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ALL",
                    "temporalUnit": "MONTH",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[8].data", 0.49)
        ),
        Step(
            RunRequest("数据舱-平效-房源-租金-按季")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ROOM",
                    "temporalUnit": "QUARTER",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[2].data", 0.15)
        ),
        Step(
            RunRequest("数据舱-平效-房源-租金+物业费-按季")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金,物业费",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ROOM",
                    "temporalUnit": "QUARTER",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[2].data", 0.15)
        ),
        Step(
            RunRequest("数据舱-平效-房源-按季")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ROOM",
                    "temporalUnit": "QUARTER",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[2].data", 0.15)
        ),
        Step(
            RunRequest("数据舱-平效-工位-租金-按季")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "CUBICLE",
                    "temporalUnit": "QUARTER",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[2].data", 1.98)
        ),
        Step(
            RunRequest("数据舱-平效-工位-租金+物业费-按季")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金,物业费",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "CUBICLE",
                    "temporalUnit": "QUARTER",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[2].data", 1.98)
        ),
        Step(
            RunRequest("数据舱-平效-工位-按季")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "CUBICLE",
                    "temporalUnit": "QUARTER",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[2].data", 1.98)
        ),
        Step(
            RunRequest("数据舱-平效-房源+工位-租金-按季")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ALL",
                    "temporalUnit": "QUARTER",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[2].data", 0.16)
        ),
        Step(
            RunRequest("数据舱-平效-房源+工位-租金+物业费-按季")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金,物业费",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ALL",
                    "temporalUnit": "QUARTER",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[2].data", 0.16)
        ),
        Step(
            RunRequest("数据舱-平效-房源+工位-按季")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金,物业费",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ALL",
                    "temporalUnit": "QUARTER",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[2].data", 0.16)
        ),
        Step(
            RunRequest("平效-房源-租金-年")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ROOM",
                    "temporalUnit": "YEAR",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[0].data", 0.04)
        ),
        Step(
            RunRequest("平效-房源-租金+物业费-年")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金,物业费",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ROOM",
                    "temporalUnit": "YEAR",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[0].data", 0.04)
        ),
        Step(
            RunRequest("平效-房源-年")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ROOM",
                    "temporalUnit": "YEAR",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[0].data", 0.04)
        ),
        Step(
            RunRequest("平效-工位-租金-年")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "CUBICLE",
                    "temporalUnit": "YEAR",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[0].data", 0.5)
        ),
        Step(
            RunRequest("平效-工位-租金+物业费-年")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金,物业费",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "CUBICLE",
                    "temporalUnit": "YEAR",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[0].data", 0.5)
        ),
        Step(
            RunRequest("平效-工位-年")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "CUBICLE",
                    "temporalUnit": "YEAR",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[0].data", 0.5)
        ),
        Step(
            RunRequest("平效-房源+工位-租金-年")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ALL",
                    "temporalUnit": "YEAR",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[0].data", 0.04)
        ),
        Step(
            RunRequest("平效-房源+工位-租金+物业费-年")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "billTypes": "租金,物业费",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ALL",
                    "temporalUnit": "YEAR",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[0].data", 0.04)
        ),
        Step(
            RunRequest("平效-房源+工位-年")
            .get("${ENV(api_url)}/assets/income-per-square")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
                    "buildingIds": "$building_id",
                    "statisticSpaceType": "ALL",
                    "temporalUnit": "YEAR",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body[0].data", 0.04)
        ),
        Step(
            RunRequest("删除楼宇")
            .delete("${ENV(api_url)}/buildings/$building_id")
            .with_headers(
                **{
                    "authorization": "Bearer $access_token",
                    "content-type": "application/json; charset=utf-8",
                }
            )
            .validate()
            .assert_equal("status_code", 204)
        ),
    ]


if __name__ == "__main__":
    TestCaseIncomePerSquare().test_start()
