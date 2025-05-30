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
      f.write("""@article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer},
	  doi={10.1007/s00766-023-00405-y}
}

@article{fernandez2017naming,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
  author={M{\'e}ndez Fern{\'a}ndez, Daniel and Wagner, Stefan and Kalinowski, Marcos and Felderer, Michael and Mafra, Priscilla and Vetr{\`o}, Antonio and Conte, Tayana and Christiansson, M-T and Greer, Des and Lassenius, Casper and others},
  journal={Empirical software engineering},
  volume={22},
  number={5},
  pages={2298--2338},
  year={2017},
  publisher={Springer},
  doi={10.1007/s10664-016-9451-7}
}

@article{mendez2017naming,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
  author={M{\'e}ndez Fern{\'a}ndez, Daniel and Wagner, Stefan and Kalinowski, Marcos and Felderer, Michael and Mafra, Priscilla and Vetr{\`o}, Antonio and Conte, Tayana and Christiansson, M-T and Greer, Des and Lassenius, Casper and others},
  journal={Empirical software engineering},
  volume={22},
  number={5},
  pages={2298--2338},
  year={2017},
  publisher={Springer},
  doi={10.1007/s10664-016-9451-7}
}

@article{wagner2019status,
  title={Status quo in requirements engineering: A theory and a global family of surveys},
  author={Wagner, Stefan and M{\'e}ndez Fern{\'a}ndez, Daniel and Felderer, Michael and Vetr{\`o}, Antonio and Kalinowski, Marcos and Wieringa, Roel and Pfahl, Dietmar and Conte, Tayana and Christiansson, Marie-Therese and Greer, Desmond and others},
  journal={ACM Transactions on Software Engineering and Methodology (TOSEM)},
  volume={28},
  number={2},
  pages={1--48},
  year={2019},
  publisher={ACM New York, NY, USA}
}

@article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer}
}""")

  yield filename

  os.remove(filename)

def test_correct_file_format(temp_file):
  assert detect_duplicates(temp_file) == "frattini2023requirements"

def test_incorrect_file_format():
  pass