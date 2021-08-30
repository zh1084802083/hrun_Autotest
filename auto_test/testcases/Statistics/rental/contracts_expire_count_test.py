# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/Statistics/rental/contracts_expire_count.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.Buildings.buildings_test import TestCaseBuildings as Buildings


class TestCaseContractsExpireCount(HttpRunner):

    config = (
        Config("数据舱--到期提醒合同份数/面积/工位数")
        .variables(**{"access_token": "${get_token()}"})
        .export(*["building_id"])
    )

    teststeps = [
        Step(RunTestCase("获取楼宇id").call(Buildings).export(*["building_id"])),
        Step(
            RunRequest("到期提醒合同份数，面积--房源")
            .get("${ENV(api_url)}/v3/contracts/notice/statistics")
            .with_params(
                **{"buildingIds": "$building_id", "statisticsSpaceType": "ROOM"}
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("到期提醒合同份数，工位数--工位")
            .get("${ENV(api_url)}/v3/contracts/notice/statistics")
            .with_params(
                **{"buildingIds": "$building_id", "statisticsSpaceType": "CUBICLE"}
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("到期提醒合同份数，面积--房源+工位")
            .get("${ENV(api_url)}/v3/contracts/notice/statistics")
            .with_params(
                **{"buildingIds": "$building_id", "statisticsSpaceType": "ALL"}
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseContractsExpireCount().test_start()
