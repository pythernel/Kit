# Kit

Unified CLI launcher for all security tools. One command to rule them all.

```
kit scan 192.168.1.0/24 -p 1-1000
kit stay install reg beacon.exe
kit token list
kit callback generate python 10.0.0.1 4444
kit relay local 8080 target 80
kit shroud notepad.exe -o packed.exe
kit pe C:\Windows\System32\notepad.exe
kit sniff --interface 0
kit exploit pattern 100
kit crypto identify 5d41402abc4b2a76b9719d911017c592
```

### Install

```powershell
.\setup.ps1
```

Then restart your terminal and just type `kit <command> <args>` from anywhere.

### Commands

| Command | Tool | Description |
|---------|------|-------------|
| `scan` | Pentest Toolkit | Port scanner |
| `pe` | Pentest Toolkit | PE analyzer |
| `sniff` | Pentest Toolkit | Packet sniffer |
| `shellcode` | Pentest Toolkit | Shellcode runner |
| `exploit` | Pentest Toolkit | Exploit utilities |
| `crypto` | Pentest Toolkit | Crypto toolkit |
| `stay` | Stay | Persistence toolkit |
| `token` | Token | Token manipulation |
| `callback` | Callback | Reverse shell generator |
| `relay` | Relay | TCP relay/forwarder |
| `shroud` | Shroud | PE crypter |
