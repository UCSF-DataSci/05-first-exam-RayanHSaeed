import argparse

def read_fasta(random_sequence):
    with open(random_sequence, 'r') as file:                    
        sequence = file.read().replace('\n', '')           #read all lines and remove newlines
    return sequence                                        #read the FASTA file and return the DNA sequence as a single string (no whitespace)

def find_cut_sites(sequence, cut_site):                    #find all occurrences of the cut site
    cut_site = cut_site.replace('|', '')                   #remove the '|' symbol
    cut_positions = []
    
    start = 0                                              #find all positions of the cut site in the sequence
    while True:
        pos = sequence.find(cut_site, start)
        if pos == -1:
            break
        cut_positions.append(pos)
        start = pos + 1                                    #move to the next position
    return cut_positions

def find_distant_pairs(cut_positions):                     #find pairs of cut sites that are 80-120 kbp apart
    pairs = []
    for i in range(len(cut_positions)):
        for j in range(i + 1, len(cut_positions)):
            distance = cut_positions[j] - cut_positions[i]
            if 80000 <= distance <= 120000:  
                pairs.append((cut_positions[i], cut_positions[j]))
    return pairs


def main():
    parser = argparse.ArgumentParser(description="Find distant cut site pairs in a DNA sequence.")
    parser.add_argument("fasta_file", help="Path to the FASTA file.")
    parser.add_argument("cut_site", help="Cut site sequence")
    args = parser.parse_args()
    
    sequence = read_fasta('/workspaces/05-first-exam-RayanHSaeed/bioinformatics_project/data/random_sequence.fasta')          #read the DNA sequence from the FASTA file
    
    cut_positions = find_cut_sites(sequence, args.cut_site)                         #find all cut site locations
    
    cut_site_pairs = find_distant_pairs(cut_positions)                              #find all pairs of cut sites that are 80-120 kbp apart
    
    
    print(f"Analyzing cut site: {args.cut_site}")
    print(f"Total cut sites found: {len(cut_positions)}")
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}")
    

    if cut_site_pairs:
        print("First 5 pairs:")                                        #first 5 cut site pairs
        for i, (start, end) in enumerate(cut_site_pairs[:5]):
            print(f"{i + 1}. {start} - {end}")
    
    
    summary_file = '/workspaces/05-first-exam-RayanHSaeed/bioinformatics_project/results/cutsite_summary.txt'           #save the summary to the results directory
    with open(summary_file, 'w') as file:
        file.write(f"Analyzing cut site: {args.cut_site}\n")
        file.write(f"Total cut sites found: {len(cut_positions)}\n")
        file.write(f"Cut site pairs 80-120 kbp apart: {len(cut_site_pairs)}\n")
        file.write("First 5 pairs:\n")
        for i, (start, end) in enumerate(cut_site_pairs[:5]):
            file.write(f"{i + 1}. {start} - {end}\n")

if __name__ == "__main__":
    main()