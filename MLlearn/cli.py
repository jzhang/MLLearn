# -*- coding: utf-8 -*-

"""Console script for MLlearn."""

import click
import MLlearn

@click.command()
def main(args=None):
    """Console script for MLlearn."""
    click.echo("#1 try scilearn LDA model")
    MLlearn.tryLDA()

if __name__ == "__main__":
    main()
