# tests/test_cli.py

import pytest
from click.testing import CliRunner

import sys
import os

# Add the parent directory of the current directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cli import cli

@pytest.fixture
def runner():
    return CliRunner()

def test_add_command(runner):
    result = runner.invoke(cli, ["add"], input="John Doe\n30\n123 Main Street\n")
    assert result.exit_code == 0
    assert "Citizen record added successfully!" in result.output

def test_list_command(runner):
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "All Citizens:" in result.output

# Add more test functions for other CLI commands (update, delete) as needed
