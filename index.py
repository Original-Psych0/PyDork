#Dependencies
from googlesearch import search
import sys
import time

#Variables
args = sys.argv

#Main
if len(args) == 1:
    print("python index.py <output> <amount> <dork>")
    sys.exit()
    
if len(args) == 2:
    print("Invalid amount.")
    sys.exit()
    
if args[2] == "0":
    args[2] = "10"
    
if len(args) == 3:
    print("Invalid dork.")
    sys.exit()
    
if args[2].isnumeric() == False:
    print("amount is invalid, make sure It's an int.")
    sys.exit()

print("Searching your dork, please wait(This might take a while).")
results = search(args[3], num_results=int(args[2]) - 1)

if len(results) == 0:
    print("No links found.")
    sys.exit()

print(f"{len(results)} links found.")
time.sleep(3)
print("Printing the links")
print()
for result in results:
    print(result)
    
print()
print(f"Saving the links to {args[1]}")

output = open(args[1], "w")
output.write("\n".join(results))
output.close()
print(f"Links has been saved to {args[1]}")
