# src/cli.py

import click
from db import add_citizen, get_all_citizens, update_citizen, delete_citizen

@click.group()
def cli():
    pass

@cli.command()
@click.option("--name", prompt="Name", help="Name of the citizen")
@click.option("--age", prompt="Age", type=int, help="Age of the citizen")
@click.option("--address", prompt="Address", help="Address of the citizen")
def add(name, age, address):
    add_citizen(name, age, address)

@cli.command()
def list():
    print("All Citizens:")
    print(get_all_citizens())

@cli.command()
@click.option("--id", prompt="Citizen ID", type=int, help="ID of the citizen to update")
@click.option("--name", prompt="Name", help="Updated name of the citizen")
@click.option("--age", prompt="Age", type=int, help="Updated age of the citizen")
@click.option("--address", prompt="Address", help="Updated address of the citizen")
def update(id, name, age, address):
    update_citizen(id, name, age, address)

@cli.command()
@click.option("--id", prompt="Citizen ID", type=int, help="ID of the citizen to delete")
def delete(id):
    delete_citizen(id)

if __name__ == "__main__":
    cli()
