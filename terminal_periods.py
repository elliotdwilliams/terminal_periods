"""Analyzes a list of subject terms to identify terms that exist both with and without terminal periods

Accepts a filename as a command line argument. That file should contain one subject
term per row; the header row is skipped. Terms are analyzed to see if the same term
exists both with and without a period at the end. Results are output to a new file
with "_results" appended to the original filename.
"""

import sys
import os

# Get filename from command line argument
INPUT_FILE = sys.argv[1]

# Open the file in read mode
with open(INPUT_FILE, "r", encoding="UTF-8") as file:
    original_terms = file.readlines()  # Read all the lines of the file into a list
original_terms = original_terms[1:]  # Remove first row

# Remove newline and other whitespace, and remove ';' at end of string
original_terms = [x.strip() for x in original_terms]
original_terms = [x.rstrip(";") for x in original_terms]

# Dedup original terms
dedup_terms = []

for term in original_terms:
    if term not in dedup_terms:
        dedup_terms.append(term)

print("Total number of deduped terms: ", len(dedup_terms))
#print(dedup_terms)

# Separate terms based on whether they have a period at the end
period_terms = []
non_period_terms = []

for term in dedup_terms:
    try:
        if term[-1] == ".":
            period_terms.append(term)
        else:
            non_period_terms.append(term)
    except IndexError:
        period_terms.append(term)

print("Terms with periods: ", len(period_terms))
#print(period_terms)
print("Terms without periods: ", len(non_period_terms))
#print(non_period_terms)

# Check if term with period also exists without a period
results = []

for term in period_terms:
    if term[0:-1] in non_period_terms:
        results.append(term[0:-1])

print("Terms in both lists: ", len(results))
#print(results)

# Create filename for results
basename_without_ext = os.path.splitext(os.path.basename(INPUT_FILE))[0]
results_filename = basename_without_ext + "_results.txt"

# Save results to text file
with open(results_filename, "w", encoding="UTF-8") as f:
    f.write("*** Dublicate subjects with terminal periods: ***\n")
    for line in results:
        f.write(f"{line}\n")
