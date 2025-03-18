import re

# Step 1: Read and clean the sequence
with open("preproinsulin-seq.txt", "r") as file:
    data = file.read()

cleaned_sequence = re.sub(r"ORIGIN|\d+|//|\s+", "", data)

# Step 2: Save the cleaned sequence
with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(cleaned_sequence)

print(f"Cleaned sequence length: {len(cleaned_sequence)} (Expected: 110)")

# Step 3: Extract and save segments
segments = {
    "lsinsulin-seq-clean.txt": cleaned_sequence[:24],   # 1-24
    "binsulin-seq-clean.txt": cleaned_sequence[24:54],  # 25-54
    "cinsulin-seq-clean.txt": cleaned_sequence[54:89],  # 55-89
    "ainsulin-seq-clean.txt": cleaned_sequence[89:110], # 90-110
}

for filename, sequence in segments.items():
    with open(filename, "w") as file:
        file.write(sequence)
    print(f"{filename} saved with {len(sequence)} characters.")