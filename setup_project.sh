#main project directory: 
mkdir bioinformatics_project

#subdirectories in main directory: 
mkdir -p bioinformatics_project/data bioinformatics_project/scripts bioinformatics_project/results

#python files in scripts directory: 
touch bioinformatics_project/scripts/generate_fasta.py bioinformatics_project/scripts/dna_operations.py bioinformatics_project/scripts/find_cutsites.py

#file in results directory: 
touch bioinformatics_project/results/cutsite_summary.txt

#file in data directory: 
touch bioinformatics_project/data/random_sequence.fasta

#file in main directory: 
touch bioinformatics_project/README.md

#brief description in readme file: 
echo "Bioinformatics Project file contains the following:" > bioinformatics_project/README.md
echo "Files include 'data', 'scripts', and 'results'.
- The 'data' file contains input data. 
- The 'scripts' file contains python files for bioinformatics operations. 
- The 'results' file contains the results and summary.
" >> bioinformatics_project/README.md

 
