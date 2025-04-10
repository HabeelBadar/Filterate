import sys
import time

arg = sys.argv[1:]

input_path = None
output_path = None

#print(arg[0])

if arg[0] == "-i":
	input_path = arg[arg.index("-i")+ 1]
if arg[2] == "-o":
	output_path = arg[arg.index("-o") + 1]

with open(input_path , "r", errors='ignore') as file:
	n = int(input("Enter min limit: "))
	start_time = time.time()
	with open(output_path , "a") as fileO:
		for line in file:
			line = line.strip()
		#	print(len(line))
		#	print(line)
			if len(line) >= n:
					#print(line)
					fileO.write(line +"\n")
end_time = time.time()
print(f"execution time: {end_time - start_time:.2f}")
print(f"Filtered: {arg[1]} => {arg[3]}")
print(f"Filtered: (path): {input_path} => {output_path}")
print("Filtering succesful!")