# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/Statistics/assets/cashflow_predictions_detail.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.Buildings.buildings_test import TestCaseBuildings as Buildings


class TestCaseCashflowPredictionsDetail(HttpRunner):

    config = (
        Config("数据舱--现金流预测详情")
        .variables(
            **{
                "access_token": "${get_token()}",
                "month_endDate": "2021-08-31",
                "month_startDate": "2021-08-01",
                "quarter_endDate": "2021-09-30",
                "quarter_startDate": "2021-07-01",
                "year_endDate": "2021-12-31",
                "year_startDate": "2021-01-01",
            }
        )
        .verify(False)
        .export(*["building_id"])
    )

    teststeps = [
        Step(RunTestCase("获取楼宇id").call(Buildings).export(*["building_id"])),
        Step(
            RunRequest("现金流预测详情--按月查询")
            .get("${ENV(api_url)}/assets/cashflow-predictions/detail")
            .with_params(
                **{
                    "billSelectAmount": "AMOUNT",
                    "buildingIds": "$building_id",
                    "endDate": "$month_endDate",
                    "startDate": "$month_startDate",
                    "page": "0",
                    "size": "100",
                    "temporalUnit": "MONTH",
                    "billTypes": "租金,物业费",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("现金流预测详情--按季查询")
            .get("${ENV(api_url)}/assets/cashflow-predictions/detail")
            .with_params(
                **{
                    "billSelectAmount": "AMOUNT",
                    "buildingIds": "$building_id",
                    "endDate": "$quarter_endDate",
                    "startDate": "$quarter_startDate",
                    "page": "0",
                    "size": "100",
                    "temporalUnit": "QUARTER",
                    "billTypes": "租金,物业费",
                }
            )
            .with_headers(**{"authorization": "Bearer $access_token"})
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("现金流预测详情--按年查询")
            .get("${ENV(api_url)}/assets/cashflow-predictions/detail")
            .with_params(
                **{
                    "billSelectAmount": "AMOUNT",
                    "buildingIds": "$building_id",
                    "endDate": "$year_endDate",
                    "startDate": "$year_startDate",
                    "page": "0",
                    "size": "100",
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
    TestCaseCashflowPredictionsDetail().test_start()
