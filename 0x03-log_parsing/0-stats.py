#!/usr/bin/python3
"""log parsing"""
import sys
import re
from signal import signal, SIGINT


total_file_size = 0
status_code_counts = {200: 0, 301: 0,
                      400: 0, 401: 0,
                      403: 0, 404: 0,
                      405: 0, 500: 0
                      }
line_count = 0

log_pattern = re.compile(
    r'^(\d{1,3}\.){3}\d{1,3} - \['
    r'(.*?)'
    r'\] "GET /projects/260 HTTP/1.1" '
    r'(\d{3}) (\d+)$'
)


def print_statistics():
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


def handle_interrupt(signal_received, frame):
    """Handle keyboard interrupt (CTRL + C)
    to print statistics before exiting.
    """
    print_statistics()
    sys.exit(0)


signal(SIGINT, handle_interrupt)


try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            total_file_size += file_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
