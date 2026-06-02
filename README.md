Note: You can also just get the gui ver. Easier to use. 

This is a tool used to optimize password dictionaries used in hashcat to brute force passwords.
You can rule out the passwords you think arent related to the brute force.

Example: wifi passwords are always more than 8 char not less, and rockyou.txt has smaller than 8 char passwords too so you can rule them out. 

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
