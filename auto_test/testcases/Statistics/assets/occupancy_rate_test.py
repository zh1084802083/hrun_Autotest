# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/Statistics/assets/occupancy_rate.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.Buildings.buildings_test import TestCaseBuildings as Buildings


class TestCaseOccupancyRate(HttpRunner):

    config = (
        Config("数据舱-计租率统计")
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
            RunRequest("计租率-房源-月查询")
            .get("${ENV(api_url)}/assets/occupancy-rate")
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
        ),
        Step(
            RunRequest("计租率-工位-月查询")
            .get("${ENV(api_url)}/assets/occupancy-rate")
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
        ),
        Step(
            RunRequest("计租率-房源+工位-月查询")
            .get("${ENV(api_url)}/assets/occupancy-rate")
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
        ),
        Step(
            RunRequest("计租率-房源-季查询")
            .get("${ENV(api_url)}/assets/occupancy-rate")
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
        ),
        Step(
            RunRequest("计租率-工位-季查询")
            .get("${ENV(api_url)}/assets/occupancy-rate")
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
        ),
        Step(
            RunRequest("计租率-房源+工位-季查询")
            .get("${ENV(api_url)}/assets/occupancy-rate")
            .with_params(
                **{
                    "beginDate": "$beginDate",
                    "endDate": "$endDate",
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
            RunRequest("计租率-房源-年查询")
            .get("${ENV(api_url)}/assets/occupancy-rate")
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
        ),
        Step(
            RunRequest("计租率-工位-年查询")
            .get("${ENV(api_url)}/assets/occupancy-rate")
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
        ),
        Step(
            RunRequest("计租率-房源+工位-年查询")
            .get("${ENV(api_url)}/assets/occupancy-rate")
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
        ),
    ]


if __name__ == "__main__":
    TestCaseOccupancyRate().test_start()
