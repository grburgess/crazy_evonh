import logging
import os
import shutil
from glob import glob
from pathlib import Path

import pytest
from crazy_evonh.utils.package_utils import get_path_of_data_file



@pytest.fixture(scope="session")
def thing():
    pass
