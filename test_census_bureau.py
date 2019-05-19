from collections import namedtuple
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from census_bureau import render, fetch


Column = namedtuple("Column", "name, type")


def params_fixture(api_key=None, dataset=None, vintage=None, variables=None, for_clause=None, in_clause=None):
    """Helper to build params."""
    return {
        "api_key": api_key,
        "dataset": dataset,
        "vintage": vintage,
        "variables": variables,
        "for": for_clause,
        "in": in_clause
    }


class FetchTest(unittest.TestCase):
    def test_fetch(self):
        result = fetch(params_fixture(None, "cbp", "1986", "EMP,ESTAB", "us:*"))

        assert isinstance(result, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()
