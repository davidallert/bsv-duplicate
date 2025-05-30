import pytest
from unittest.mock import MagicMock
from unittest.mock import patch
from src.util.detector import detect_duplicates

@pytest.fixture
def correct_temp_file():
  with open("./data/references.bib", "r") as source_file:
    content = source_file.read()

  return content

@pytest.fixture
def incorrect_temp_file():
  with open("./data/incorrect_references.bib", "r") as source_file:
    content = source_file.read()

  return content

def test_correct_file_format(correct_temp_file):
  result = detect_duplicates(correct_temp_file)
  assert result == ["frattini2023requirements"]

def test_correct_file_format(incorrect_temp_file):
  with pytest.raises(Exception):
    detect_duplicates(incorrect_temp_file)