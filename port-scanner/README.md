# Simple TCP Port Scanner

A basic Python TCP connect scanner built while learning network programming fundamentals.

## What it does
Scans a target host across a range of ports (1-1024) and reports which ones are open, using raw sockets.

## Usage
\`\`\`
python3 port_scanner.py
\`\`\`
(Currently hardcoded to scan scanme.nmap.org — CLI arguments coming soon)

## Disclaimer
For educational and authorized testing purposes only. Only scan systems you own or have explicit permission to test. `scanme.nmap.org` is a legal public test target provided by the Nmap project.

## Status
🚧 Work in progress — next steps: threading for speed, banner grabbing, CLI argument support.