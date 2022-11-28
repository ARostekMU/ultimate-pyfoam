from pathlib import Path

from ultimate_pyfoam.domain.dimensions import Dimensions
from ultimate_pyfoam.service.case_dumper import CaseDumper


def test_init() -> None:
    CaseDumper(case={})


dummy_case = {Path("dummyFile"): {"dummyKey": "dummyValue"}}


def test_dump_dummy(tmp_path: Path) -> None:
    cd = CaseDumper(case=dummy_case)
    cd.dump(case_dir=tmp_path)

    assert (tmp_path / "dummyFile").exists()


def test_dumped_content_is_correct(tmp_path: Path) -> None:
    cd = CaseDumper(case=dummy_case)
    cd.dump(case_dir=tmp_path)

    written_string = Path(tmp_path / "dummyFile").read_text().strip()
    string = "dummyKey dummyValue;"
    assert string == written_string


multidir_case = {
    Path("a"): {"x": 1},
    Path("b"): {"y": 2},
    Path("C/d"): {"z": 3},
    Path("E/F/g"): {"w": 4},
}


def test_dump_mutliple_directories(tmp_path: Path) -> None:
    cd = CaseDumper(case=multidir_case)
    cd.dump(case_dir=tmp_path)

    assert (tmp_path / "a").exists()
    assert (tmp_path / "b").exists()
    assert (tmp_path / "C" / "d").exists()
    assert (tmp_path / "E" / "F" / "g").exists()


realistic_case = {
    Path("0/U"): {"dimensions": Dimensions(0, 1, -1, 0, 0, 0, 0)},
    Path("constant/thermophysicalProperties"): {"thermoType": {"type": "hePsiThermo"}},
    Path("constant/turbulenceProperties"): {"simulationType": "laminar"},
    Path("system/fvSchemes"): {"fluxScheme": "Kurganov"},
}
