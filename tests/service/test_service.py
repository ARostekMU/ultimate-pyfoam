of_file = """FoamFile
{
    format      ascii;
    class       volScalarField;
    object      T;
}"""

from ultimate_pyfoam.service import Dumper
from ultimate_pyfoam.domain.dimensions import Dimensions
from ultimate_pyfoam.domain.of_dict import OfDict


def test_service() -> None:
    
    Dumper(
        {
            OfDict({
                "FoamFile": OfDict({
                    "format": "ascii",
                    "class": "volScalarField",
                    "object": "T",
                }),
            })
        }
    )

    Dumper(
        {
            "FoamFile": OfDict({
                "format": "ascii",
                "class": "volScalarField",
                "object": "T",
            })
        }
    )
    
    Dumper(
        header={
            "format": "ascii",
            "class": "volScalarField",
        },
    )