import sys
import time
import os

help_text = """\
Usage: textfilter.py -i <input_file> -o <output_file> [--debug]

What it does:
Filters lines from a file based on minimum length.

Options:
  -i     Input file path
  -o     Output file path
  --debug Show filtering stats
  --help  Show this help message

Example:
  python textfilter.py -i input.txt -o output.txt --debug
"""

def show_help():
    print(help_text)

def get_unique_path(path):
    if not os.path.exists(path):
        return path

    base, ext = os.path.splitext(path)
    i = 1

    while True:
        new_path = f"{base}({i}){ext}"
        if not os.path.exists(new_path):
            return new_path
        i += 1


args = sys.argv[1:]

if not args or "--help" in args:
    show_help()
    sys.exit()

input_path = None
output_path = None
flag_debug = False

try:
    if "-i" in args:
        input_path = args[args.index("-i") + 1]
    if "-o" in args:
        output_path = args[args.index("-o") + 1]
    if "--debug" in args:
        flag_debug = True
except (ValueError, IndexError):
    print("Error: Invalid arguments. Use --help for usage.")
    sys.exit()

if not input_path or not output_path:
    print("Error: Missing input or output path. Use --help for usage.")
    sys.exit()

if not os.path.isfile(input_path):
    print("Error: Input file not found.")
    sys.exit()

# AUTO-RENAME OUTPUT FILE IF EXISTS
output_path = get_unique_path(output_path)

min_len = int(input("Enter minimum line length: "))

total = 0
kept = 0
start = time.time()

with open(input_path, "r", errors="ignore") as fin, open(output_path, "w") as fout:
    for line in fin:
        total += 1
        line = line.strip()
        if len(line) >= min_len:
            kept += 1
            fout.write(line + "\n")

end = time.time()

if flag_debug:
    print("------ DEBUG ------")

    input_name = os.path.basename(input_path)
    output_name = os.path.basename(output_path)

    print(f"Filtered: {input_name} => {output_name}")
    print(f"Filtered: (path): {input_path} => {output_path}")

    print(f"Total lines: {total}")
    print(f"Kept lines: {kept}")
    print(f"Removed: {total - kept}")
    print(f"Time: {end - start:.2f}s")

print("Filtering successful!")