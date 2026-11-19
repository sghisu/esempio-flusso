import argparse

from renamer import __version__


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="renamer", description="Normalizza i nomi dei file (in sviluppo)."
    )
    parser.add_argument("--version", action="version", version=__version__)
    parser.parse_args(argv)


if __name__ == "__main__":
    main()
