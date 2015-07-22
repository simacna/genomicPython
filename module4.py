# 7/22
# reading/writing files

f = open('myfile', 'a')
f.write('This is a third line') #returns 20 which is the number of characters added
#when done with file, want to close it

f.close() #in general, if you don't close it'll close it

#Module 4 - Lecture 2

#Excercise: build a dictionary containing all sequences from a FASTA file

#pseudo-code:

#open file

# read line

# is line a header?

# if yes, get sequence name

# create new entry in dictionary

# if no, update sequence in dictionary

# finally, are there any more lines? continue.

try:
	f = open("myufile.fa")
except IOError:
	print("File myfile.fa does not exist!")

seqs = {}

for line in f:
	#lets discard the newline at the end (if any)
	line = line.rstrip() #distinguis header from sequence
				#method rstrip([chars]) returns a copy of the string with trailing characters chars removed

	if line[0]=='>': # or line.startswitch('>') -first character always starts with >; that would mean we're at the beginning 
	#of entry
		words = line.split() #splits header line on whitespace
		name = words[0][1:]
		seqs[names]='' #we initialize a new entry. 
	else:
		seqs[name] = seqs[name] + line #if not at header line, we're at sequence. we append append sequence on current line
		#to the end of our dna entry

close(f)
















