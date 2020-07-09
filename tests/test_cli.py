# test_cli.py

import pytest
import subprocess
import pathlib
import time
import signal

insertion = '/usr/local/bin/profiler'

no_input_flags = [
    '--host_ssid',
    '--noAP',
    '--no11ax',
    '--no11r',
    '--menu_mode',
    '--clean',
    '--oui_update',
    '--version',
    '-V',
    '-h',
    '--help'
]

input_needed = [
    '--file <FILE>',
    '--config <FILE>',
    '--menu_file <FILE>',
    '--files_root <PATH>',
]

debug_types = ['debug', 'warning']

@pytest.mark.parametrize('flag', no_input_flags)
def test_cli_no_args(flag):
    output = subprocess.Popen([insertion, flag], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output.wait(15)
    except subprocess.TimeoutExpired:
        output.send_signal(signal.SIGINT)
        output.wait()
    assert output.returncode == 0, "Program did not exit cleanly with no args"


def test_channel_flag():
    output = subprocess.Popen([insertion, '-c 3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output.wait(15)
    except subprocess.TimeoutExpired:
        output.send_signal(signal.SIGINT)
        output.wait()
    assert output.returncode == 0, "Program did not exit cleanly with no args"


def test_ssid_flag():
    output = subprocess.Popen([insertion, '--ssid', ' pytest'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output.wait(15)
    except subprocess.TimeoutExpired:
        output.send_signal(signal.SIGINT)
        output.wait()
    assert output.returncode == 0, "Program did not exit cleanly with no args"



@pytest.mark.parametrize('debug', debug_types)
def test_logging_flag(debug):
    output = subprocess.Popen([insertion, '--logging', debug], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output.wait(15)
    except subprocess.TimeoutExpired:
        output.send_signal(signal.SIGINT)
        output.wait()
    assert output.returncode == 0, "Program did not exit cleanly with no args"



def test_interface_flag():
    output = subprocess.Popen([insertion, '-i wlan0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output.wait(15)
    except subprocess.TimeoutExpired:
        output.send_signal(signal.SIGINT)
        output.wait()
    assert output.returncode == 0, "Program did not exit cleanly with no args"
