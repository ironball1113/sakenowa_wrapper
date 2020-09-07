import glob
import os
import pathlib
import re

import pytest

from src.sakenowa_wrapper import SakenowaAPI


def test_sakenowa_get_key():
    sakenowa_areas = SakenowaAPI("areas")
    assert sakenowa_areas._set_key() == "areas"

