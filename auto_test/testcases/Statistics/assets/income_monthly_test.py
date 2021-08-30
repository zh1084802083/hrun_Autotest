# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/Statistics/assets/income_monthly.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.Buildings.buildings_test import TestCaseBuildings as Buildings


class TestCaseIncomeMonthly(HttpRunner):

    config = (
        Config("数据舱--收益")
        .variables(
            **{
                "access_token": "${get_token()}",
                "endDate": "2021-12-31",
                "startDate": "2021-01-01",
            }
        )
        .verify(False)
        .export(*["building_id"])
    )

    teststeps = [
        Step(RunTestCase("获取楼宇id").call(Buildings).export(*["building_id"])),
        Step(
            RunRequest("收益--按月查询")
            .get("${ENV(api_url)}/assets/income/monthly")
            .with_params(
                **{
                    "buildingIds": "$building_id",
                    "endDate": "$endDate",
                    "startDate": "$startDate",
                    "temporalUnit": "MONTH",
                    "billTypes": "租金,物业费",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("收益--按季查询")
            .get("${ENV(api_url)}/assets/income/monthly")
            .with_params(
                **{
                    "buildingIds": "$building_id",
                    "endDate": "$endDate",
                    "startDate": "$startDate",
                    "temporalUnit": "QUARTER",
                    "billTypes": "租金,物业费",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("收益--按年查询")
            .get("${ENV(api_url)}/assets/income/monthly")
            .with_params(
                **{
                    "buildingIds": "$building_id",
                    "endDate": "$endDate",
                    "startDate": "$startDate",
                    "temporalUnit": "YEAR",
                    "billTypes": "租金,物业费",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseIncomeMonthly().test_start()
