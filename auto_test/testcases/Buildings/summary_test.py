# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/Buildings/summary.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.Buildings.buildings_test import TestCaseBuildings as Buildings


class TestCaseSummary(HttpRunner):

    config = (
        Config("楼宇统计")
        .variables(**{"access_token": "${get_token()}"})
        .export(*["building_id"])
    )

    teststeps = [
        Step(RunTestCase("获取楼宇id").call(Buildings).export(*["building_id"])),
        Step(
            RunRequest("楼宇统计---房源")
            .get("${ENV(api_url)}/data-statistics/building/summary")
            .with_params(
                **{
                    "ids": "$building_id",
                    "portfolioType": "BUILDING",
                    "statisticSpaceType": "ROOM",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("楼宇统计---工位")
            .get("${ENV(api_url)}/data-statistics/building/summary")
            .with_params(
                **{
                    "ids": "$building_id",
                    "portfolioType": "BUILDING",
                    "statisticSpaceType": "CUBICLE",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("楼宇统计---房源+工位")
            .get("${ENV(api_url)}/data-statistics/building/summary")
            .with_params(
                **{
                    "ids": "$building_id",
                    "portfolioType": "BUILDING",
                    "statisticSpaceType": "ALL",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseSummary().test_start()
