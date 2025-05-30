import pytest
from unittest.mock import MagicMock
from unittest.mock import patch
from src.util.detector import detect_duplicates
import os

@pytest.mark.unit
def test_detect_duplicates():
    assert True

@pytest.fixture
def temp_file():
  filename = "test.txt"
  with open(filename, "w") as f:
      f.write("""@article{frattini2023requirements, title={Requirements quality research: a harmonized theory, evaluation, and roadmap}, author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael}, journal={Requirements Engineering}, pages={1--14},year={2023}, publisher={Springer}, doi={10.1007/s00766-023-00405-y}}""")

  yield filename

  os.remove(filename)

def test_correct_file_format(temp_file):
  detect_duplicates(temp_file)

def test_incorrect_file_format():
  pass

def test_incorrect_file_format():
  pass