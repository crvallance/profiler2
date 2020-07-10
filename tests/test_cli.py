# test_cli.py

import pytest
import subprocess
import signal
import pathlib
from profiler2 import helpers
import sys

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
    '--help',
    '--11r',
    '--11ax',
]

input_needed = [
    '--file <FILE>',
    '--menu_file <FILE>',
    '--files_root <PATH>',
    '--pcap <FILE>',
]

setup_needed = '--noprep'

debug_types = ['debug', 'warning']

@pytest.fixture()
def setup_interface():
    # log.info("start interface prep...")
    if not helpers.prep_interface('wlan0', "monitor", '6'):
    # if not helpers.prep_interface(interface, "monitor", channel):
        # log.error("failed to prep interface")
        print("exiting...")
        sys.exit(-1)
        # log.info("done prep interface...")

def test_no_prep(setup_interface):
    output = subprocess.Popen([insertion, '--noprep'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output.wait(15)
    except subprocess.TimeoutExpired:
        output.send_signal(signal.SIGINT)
        output.wait()
    assert output.returncode == 0, "Program did not exit cleanly with no args"

def test_config_input():
    config_ini = pathlib.Path('./profiler2/config.ini')
    output = subprocess.Popen([insertion, '--config', config_ini], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output.wait(15)
    except subprocess.TimeoutExpired:
        output.send_signal(signal.SIGINT)
        output.wait()
    assert output.returncode == 0, "Program did not exit cleanly with no args"    

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
