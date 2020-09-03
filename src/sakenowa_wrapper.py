import ast
import urllib.request

import pandas as pd
from pandas.core.frame import DataFrame


class SakenowaAPI(object):
    urls = {
        "areas": "https://muro.sakenowa.com/sakenowa-data/api/areas",
        "brands": "https://muro.sakenowa.com/sakenowa-data/api/brands",
        "breweries": "https://muro.sakenowa.com/sakenowa-data/api/breweries",
        "rankings": "https://muro.sakenowa.com/sakenowa-data/api/rankings",
        "flavor-charts": "https://muro.sakenowa.com/sakenowa-data/api/flavor-charts",
        "flavor-tags": "https://muro.sakenowa.com/sakenowa-data/api/flavor-tags",
        "brand-flavor-tags": "https://muro.sakenowa.com/sakenowa-data/api/brand-flavor-tags",
    }

    def __init__(self, endpoint: str, ranking_type: str = None) -> None:
        self.endpoint = endpoint
        check_endpoint = self.endpoint in list(self.urls.keys())

        if check_endpoint:
            self.url = self.urls[self.endpoint]
            self.ranking_type = ranking_type

            print(f"\nThe current endpoint is {self.endpoint}")
            if ranking_type is not None:
                print(f"Rankings type is {ranking_type}")
            print("=" * 30)
        else:
            raise ValueError("引数が正しくありません。改めて指定してください。")

    def _get_body(self, url: str) -> str:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            body = res.read()
        return body.decode()

    def _set_key(self) -> str:
        if self.endpoint in ["areas", "brands", "breweries"]:
            return self.endpoint

        if self.endpoint == "flavor-charts":
            return "flavorCharts"

        if self.endpoint == "flavor-tags":
            return "tags"

        if self.endpoint == "brand-flavor-tags":
            return "flavorTags"

        if self.endpoint == "rankings" and self.ranking_type is not None:
            return self.ranking_type
        else:
            return "Failure"

    def set_df(self) -> DataFrame:
        body = self._get_body(self.url)
        dic = ast.literal_eval(body)
        key = self._set_key()
        return pd.DataFrame(dic[key])
