from renamer import __version__
from renamer.cli import main


def test_versione():
    assert __version__ == "0.1.0"


def test_cli_senza_argomenti():
    main([])
