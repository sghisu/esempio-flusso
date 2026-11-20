import re

import pytest

from renamer.slug import slugify


@pytest.mark.parametrize(
    ("testo", "atteso"),
    [
        ("Città Vecchia 2024", "citta-vecchia-2024"),
        ("  --Foto__Mare!! ", "foto-mare"),
        ("日本", ""),
        ("", ""),
        ("!!! ??? --", ""),
        ("2024", "2024"),
        ("a---b__c  d", "a-b-c-d"),
        ("Perché È così", "perche-e-cosi"),
    ],
)
def test_slugify(testo, atteso):
    assert slugify(testo) == atteso


def test_risultato_contiene_solo_caratteri_ammessi():
    risultato = slugify("../Foto: mare/2024 (1).jpeg")
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", risultato)
    assert risultato == "foto-mare-2024-1-jpeg"
