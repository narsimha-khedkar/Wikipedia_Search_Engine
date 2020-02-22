import re
from collections import defaultdict

#Main function to create the index
def main(fh):
    print("Creating Index..")
    #create a dictionary collection of type SET
    results = defaultdict(set)

    #Iterate over the Input file per line.
    for index, line in enumerate(fh, start=1):
        #Split each line into words
        words = re.findall(r'\w+', line)
        #For each word add into the results collection with a pointer to its position
        for word in words:
            results[word].add(index)
        
    print ("Number of Unique Terms in document: " +str(len(results)))

    return results

if __name__ == '__main__': 
    #Static Input & Indexer file for now       
    try:
        inputFile, outputFile = "570.txt", "index.idx"
    except IndexError:
        print("File not found")
        exit(1)

    #Open the input file & create a pointer
    with open(inputFile) as input_file:
        #Call the main function
        index = main(input_file)

    #Open the Output file for creatingt the index
    with open(outputFile, 'w') as out_fh:
        #Sort the terms and print each occurences
        for word in sorted(index):            
            print(word + " " +  " ".join(str(i) for i in sorted(index[word])),file=out_fh)
        print("Index Created Successfully")