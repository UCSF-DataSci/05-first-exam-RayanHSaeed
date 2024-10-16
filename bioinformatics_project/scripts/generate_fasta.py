import random 

#nucleotides: 
nucleotides= ['A', 'C', 'G', 'T']

#generating a random sequence of 1million base pairs: 
length = 1000000
random_sequence = ''.join(random.choices(nucleotides, k=length))

#output file: 
output_file = '/workspaces/05-first-exam-RayanHSaeed/bioinformatics_project/data/random_sequence.fasta'

#editing file in write mode: 
with open(output_file, 'w') as fasta_file: 
    for i in range(0, length, 80):              #writing in lines of 80 nucleotides
        fasta_file.write(random_sequence[i:i+80] + '\n')
