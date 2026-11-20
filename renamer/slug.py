"""Trasformazione di nomi in slug adatti a un nome di file."""

import re
import unicodedata


def slugify(testo: str) -> str:
    """Riduce ``testo`` a una forma normalizzata ``[a-z0-9-]``.

    Le lettere accentate diventano la lettera base, ogni sequenza di
    caratteri non latini o non cifre diventa un trattino e i trattini ai
    bordi vengono rimossi. Se non resta nulla il risultato è ``""``.
    """
    s = unicodedata.normalize("NFD", testo.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")
