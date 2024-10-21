import sys
import argparse


def complement(sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}         #complement dictionary
    return ''.join(complement_dict[base] for base in sequence)         #new string to join the complements for bases in sequence

def reverse(sequence):
    return sequence[::-1]                     #slice the string in reverse

def reverse_complement(sequence):
    return reverse(complement(sequence))      #first complement the sequence, then reverse it


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DNA sequence operations.')
    parser.add_argument('sequence', type=str, nargs=1, help='DNA sequence to process')       #positional argument for the DNA sequence, and store it in a list with 'append'
    args = parser.parse_args()
    
    sequence = args.sequence[0].upper()                     #first element of the list; get the sequence, convert to uppercase
    
    print(f"Original sequence: {sequence}")                 #print original sequence and its transformations
    print(f"Complement: {complement(sequence)}")
    print(f"Reverse: {reverse(sequence)}")
    print(f"Reverse complement: {reverse_complement(sequence)}")