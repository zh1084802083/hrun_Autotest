# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/Statistics/assets/bill_list_detail.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.Buildings.buildings_test import TestCaseBuildings as Buildings


class TestCaseBillListDetail(HttpRunner):

    config = (
        Config("数据舱--收缴率/分摊收缴率详情")
        .variables(
            **{
                "access_token": "${get_token()}",
                "month_payDateFrom": "2021-08-01",
                "month_payDateTo": "2021-08-31",
                "quarter_payDateFrom": "2021-07-01",
                "quarter_payDateTo": "2021-09-30",
                "year_payDateFrom": "2021-01-01",
                "year_payDateTo": "2021-12-31",
            }
        )
        .verify(False)
        .export(*["building_id"])
    )

    teststeps = [
        Step(RunTestCase("获取楼宇id").call(Buildings).export(*["building_id"])),
        Step(
            RunRequest("收缴率/分摊收缴率详情--按月查询")
            .get("${ENV(api_url)}/api/web/v2/bills/list")
            .with_params(
                **{
                    "buildingIds": "$building_id",
                    "page": "0",
                    "payDateFrom": "$month_payDateFrom",
                    "payDateTo": "$month_payDateTo",
                    "size": "100",
                    "type": "租金,物业费",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("收缴率/分摊收缴率详情--按季查询")
            .get("${ENV(api_url)}/api/web/v2/bills/list")
            .with_params(
                **{
                    "buildingIds": "$building_id",
                    "page": "0",
                    "payDateFrom": "$quarter_payDateFrom",
                    "payDateTo": "$quarter_payDateTo",
                    "size": "100",
                    "type": "租金,物业费",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("收缴率/分摊收缴率详情--按年查询")
            .get("${ENV(api_url)}/api/web/v2/bills/list")
            .with_params(
                **{
                    "buildingIds": "$building_id",
                    "page": "0",
                    "payDateFrom": "$year_payDateFrom",
                    "payDateTo": "$year_payDateTo",
                    "size": "100",
                    "type": "租金,物业费",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseBillListDetail().test_start()
