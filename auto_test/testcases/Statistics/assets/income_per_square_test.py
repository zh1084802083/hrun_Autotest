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
            RunRequest("数据舱-平效-房源-按月")
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
        ),
        Step(
            RunRequest("数据舱-平效-工位-按月")
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
        ),
        Step(
            RunRequest("数据舱-平效-房源+工位-按月")
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
        ),
        Step(
            RunRequest("数据舱-平效-房源-按季")
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
        ),
        Step(
            RunRequest("数据舱-平效-工位-按季")
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
        ),
        Step(
            RunRequest("数据舱-平效-房源+工位-按季")
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
        ),
        Step(
            RunRequest("平效-房源(楼层)-年")
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
        ),
        Step(
            RunRequest("平效-工位-年")
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
        ),
        Step(
            RunRequest("平效-房源+工位-年")
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
        ),
    ]


if __name__ == "__main__":
    TestCaseIncomePerSquare().test_start()
