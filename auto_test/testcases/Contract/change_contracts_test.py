# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/Contract/change_contracts.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.Auth.user_info_test import TestCaseUserInfo as UserInfo

from testcases.Buildings.buildings_test import TestCaseBuildings as Buildings


class TestCaseChangeContracts(HttpRunner):

    config = (
        Config("变更原合同")
        .variables(
            **{
                "access_token": "${get_token()}",
                "areaSize": "${str_to_int(10)}",
                "room_number": "${random_int(101,199)}",
            }
        )
        .verify(False)
        .export(*["room_id", "building_id", "contract_id", "customerId"])
    )

    teststeps = [
        Step(RunTestCase("获取用户id").call(UserInfo).export(*["customerId"])),
        Step(RunTestCase("获取楼宇id").call(Buildings).export(*["building_id"])),
        Step(
            RunRequest("新增可招商房源")
            .post("${ENV(api_url)}/buildings/$building_id/rooms")
            .with_headers(
                **{
                    "accept": "application/json",
                    "authorization": "Bearer $access_token",
                }
            )
            .with_json(
                {
                    "areaSize": "$areaSize",
                    "buildingId": "$building_id",
                    "cubicleUpdateRequests": [],
                    "floorName": "1",
                    "jsonData": '[{"required":false,"fieldName":"建筑面积","fieldType":"NUMBER","systemField":true},{"required":false,"fieldName":"装修","fieldType":"SINGLE_SELECT","values":["不限","毛坯","简装","精装"],"systemField":true},{"required":false,"fieldName":"预租单价","fieldType":"NUMBER","systemField":true}]',
                    "marketingAvailable": "true",
                    "realAreaSize": "$areaSize",
                    "roomNumber": "$room_number",
                    "spaceType": "ROOM",
                }
            )
            .extract()
            .with_jmespath("body", "room_id")
            .validate()
            .assert_equal("status_code", 201)
        ),
        Step(
            RunRequest("生成房源合同租金明细")
            .post("${ENV(api_url)}/v2/contracts/pays")
            .with_headers(**{"authorization": "Bearer $access_token"})
            .with_json(
                {
                    "baseTerm": {
                        "areaSize": "$areaSize",
                        "calculateOrder": "AREA_FIRST",
                        "deposit": 1,
                        "depositPayEnumDesc": "租金保证金",
                        "depositUnitEnum": "MONTH",
                        "leaseBeginDate": "${begin_date()}",
                        "leaseEndDate": "${end_180()}",
                        "monetaryUnit": "人民币CNY",
                        "precisionEnum": "RESULT",
                        "signDate": "${begin_date()}",
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
                            "price": 10,
                            "priceUnitEnum": "D",
                            "termBeginDate": "${begin_date()}",
                            "termEndDate": "${end_180()}",
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
            RunRequest("新建房源合同--按面积计算租金")
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
                        "areaSize": "$areaSize",
                        "calculateOrder": "AREA_FIRST",
                        "contractNo": "001",
                        "leaseBeginDate": "${begin_date()}",
                        "leaseEndDate": "${end_180()}",
                        "precisionEnum": "RESULT",
                        "signDate": "${begin_date()}",
                        "spaceUnit": "P",
                        "theoryRounded": False,
                        "unitPricePrecision": 2,
                    },
                    "contractNo": "001",
                    "customKeywords": [],
                    "expenseTerms": [
                        {
                            "areaSize": "$areaSize",
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
                                    "price": 10,
                                    "priceUnitEnum": "D",
                                    "termBeginDate": "${begin_date()}",
                                    "termEndDate": "${end_180()}",
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
            RunRequest("提交合同")
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
                    "customerId": "$customerId",
                    "description": "湖南神雀网络科技有限公司/测试楼宇/$room_number",
                    "objectId": "$contract_id",
                }
            )
            .teardown_hook("${wait($response,0.5)}")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("查看合同详情")
            .get("${ENV(api_url)}/v2/contracts/$contract_id")
            .with_headers(**{"authorization": "Bearer $access_token"})
            .extract()
            .with_jmespath("body.baseTerm", "baseTerm")
            .with_jmespath("body.expenseTerms", "expenseTerms")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("修改原房源合同--按面积计算租金")
            .post("${ENV(api_url)}/v3/contracts/change")
            .with_params(
                **{"changeWay": "CHANGE_ORIGIN_CONTRACT", "id": "$contract_id"}
            )
            .with_headers(
                **{
                    "authorization": "Bearer $access_token",
                    "content-type": "application/json; charset=utf-8",
                }
            )
            .with_json(
                {
                    "attachments": [],
                    "newContract": {
                        "baseTerm": "$baseTerm",
                        "contractNo": "001",
                        "customKeywords": [],
                        "expenseTerms": "$expenseTerms",
                        "followId": 4990,
                        "followName": "13787340624",
                        "industryName": None,
                        "jsonData": "[]",
                        "legalPerson": {"name": "李传根"},
                        "remarkTerms": [],
                        "resourceIds": ["$room_id"],
                        "resourceType": "ROOM",
                        "tags": [],
                        "tenantId": 78327,
                        "tenantName": "湖南神雀网络科技有限公司",
                        "tenantNo": None,
                    },
                    "newContractStartDate": "${begin_date()}",
                    "terminationContractCarryForward": {
                        "billList": [],
                        "contractId": "$contract_id",
                    },
                }
            )
            .validate()
            .assert_equal("status_code", 201)
        ),
        Step(
            RunRequest("提交原合同变更")
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
                    "subDomainType": "CHANGE_APPROVAL",
                    "domainType": "CONTRACT",
                    "customerId": "$customerId",
                    "description": "湖南神雀网络科技有限公司/测试楼宇/$room_number",
                    "objectId": "$contract_id",
                }
            )
            .teardown_hook("${wait($response,1)}")
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseChangeContracts().test_start()
