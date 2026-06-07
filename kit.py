#!/usr/bin/env python3
"""
Kit — unified CLI launcher for pythernel's security tools
"""
import sys
import os
import subprocess
import argparse

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))

REPOS = {
    "stay": os.path.join(TOOLS_DIR, "..", "Stay"),
    "token": os.path.join(TOOLS_DIR, "..", "Token"),
    "callback": os.path.join(TOOLS_DIR, "..", "Callback"),
    "relay": os.path.join(TOOLS_DIR, "..", "Relay"),
    "shroud": os.path.join(TOOLS_DIR, "..", "Shroud"),
    "spectrec2": os.path.join(TOOLS_DIR, "..", "SpectreC2"),
    "pentest-toolkit": os.path.join(TOOLS_DIR, "..", "pentest-toolkit"),
    "discord": os.path.join(TOOLS_DIR, "..", "Discord"),
}


def cmd_stay(args):
    script = os.path.join(REPOS["stay"], "stay.py")
    subprocess.run([sys.executable, script] + args)


def cmd_token(args):
    script = os.path.join(REPOS["token"], "tok.py")
    subprocess.run([sys.executable, script] + args)


def cmd_callback(args):
    script = os.path.join(REPOS["callback"], "callback.py")
    subprocess.run([sys.executable, script] + args)


def cmd_relay(args):
    script = os.path.join(REPOS["relay"], "relay.py")
    subprocess.run([sys.executable, script] + args)


def cmd_shroud(args):
    script = os.path.join(REPOS["shroud"], "shroud.py")
    subprocess.run([sys.executable, script] + args)


def cmd_scan(args):
    script = os.path.join(REPOS["pentest-toolkit"], "port_scanner", "scanner.py")
    subprocess.run([sys.executable, script] + args)


def cmd_pe(args):
    script = os.path.join(REPOS["pentest-toolkit"], "pe_analyzer", "analyzer.py")
    subprocess.run([sys.executable, script] + args)


def cmd_sniff(args):
    script = os.path.join(REPOS["pentest-toolkit"], "packet_sniffer", "sniffer.py")
    subprocess.run([sys.executable, script] + args)


def cmd_shellcode(args):
    script = os.path.join(REPOS["pentest-toolkit"], "shellcode_runner", "runner.py")
    subprocess.run([sys.executable, script] + args)


def cmd_exploit(args):
    script = os.path.join(REPOS["pentest-toolkit"], "exploit_dev", "exploit_tools.py")
    subprocess.run([sys.executable, script] + args)


def cmd_crypto(args):
    script = os.path.join(REPOS["pentest-toolkit"], "crypto_tools", "crypto_tools.py")
    subprocess.run([sys.executable, script] + args)


def cmd_discord(args):
    script = os.path.join(REPOS["discord"], "discord.py")
    subprocess.run([sys.executable, script] + args)


COMMANDS = {
    "stay": cmd_stay,
    "token": cmd_token,
    "callback": cmd_callback,
    "relay": cmd_relay,
    "shroud": cmd_shroud,
    "scan": cmd_scan,
    "pe": cmd_pe,
    "sniff": cmd_sniff,
    "shellcode": cmd_shellcode,
    "exploit": cmd_exploit,
    "crypto": cmd_crypto,
    "discord": cmd_discord,
}

HELP_TEXT = """Kit — unified tool launcher

Usage: kit <command> [args...]

Commands:
  stay              Persistence toolkit (install/check/remove)
  token             Token manipulation & privesc check
  callback          Reverse shell generator
  relay             TCP port relay/forwarder
  shroud            PE crypter
  scan              Port scanner
  pe                PE analyzer
  sniff             Packet sniffer
  shellcode         Shellcode runner
  exploit           Exploit development utilities
  crypto            Crypto analysis toolkit
  discord           Full Discord terminal client (needs: pip install websockets)
"""


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print(HELP_TEXT)
        return

    cmd = sys.argv[1].lower()
    args = sys.argv[2:]

    if cmd in COMMANDS:
        COMMANDS[cmd](args)
    else:
        print(f"Unknown command: {cmd}")
        print("Run 'kit' or 'kit help' for available commands")


if __name__ == "__main__":
    main()
