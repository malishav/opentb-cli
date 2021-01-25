"""Test compile_and_test_for_board script."""

import os
import subprocess

import opentb.opentb as opentb 


def test_help_message():
    """Verify that the help message is in the script documentation."""
    script = 'opentb.py'

    # Read the help message from executing the script
    help_bytes = subprocess.check_output(['./%s' % script, '--help'])
    help_msg = help_bytes.decode('utf-8')
    docstring = opentb.__doc__

    assert help_msg in docstring, "Help message not in the documentation"

