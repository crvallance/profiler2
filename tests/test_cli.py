# test_cli.py

import subprocess
import pathlib

insertion = '/opt/wlanpi/pipx/bin/profiler'

def test_cli_no_args():
    output = subprocess.run(["sudo", insertion], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert output.returncode == 0, "Program did not exit cleanly with no args"
