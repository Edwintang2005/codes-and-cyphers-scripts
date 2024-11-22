# codes-and-cyphers-scripts

**Valid ISBN**


This is a program that takes in a 10 digit ISBN and verifies if it is a valid ISBN or not. In the case that it isn't, it will ask the user to determine a digit that is invalid and will try alternative digits until it can find a corrected isbn.

This is in validISBN.py.

**Average Codeword Length Helper**


This file is a collection of algorithms that will calculate the average codeword lengths of given codes.

For Markov Sources, we can find the average codeword length given a transition matrix and equilibirum vector of the code, hence the tool will guide you through a process of doing the matrix multiplication. This requires the user to calculate the lengths for each column by using knuth's lemma, which shouldn't be too difficult. Basically construct a simple huffman tree and encode as usual, except sum up the probabilities at the child nodes. (e.g. For a code with probabilities 1/10, 1/5, 7/10 - Sorted this goes in order 1/10, 1/5, 7/10 hence first child node has probability 1/10 + 1/5 = 3/10. next child node has probability 3/10 + 7/10 = 1. hence average length is 3/10 + 1 = 13/10).

For a Shanon-Fano code, using the probability of the element we can calculate the length of the codeword, hence the tool will calculate these lengths, outputting as we go and ultimately provide you with the average codeword length.

For a Shanon-Fano code of the nth extension as n-> ∞, we have to do a slightly different calculation but the tool will guide you through inputting the probabilities and output an answer

This is available in averageCodewordLengthHelper.py.

**Comma Code Encoder**


Using the standard comma code where the first symbol is 0, second 10, third 110 etc, this tool takes in the length of the codewords, then a message to be encoded and outputs the encoding

This is run in commaCode.py

**Arithmetic Encoding and Decoder for 3 values**


Building on the principles of arithmetic encoding between 0 and 1, this script implements an encoder and decoder for codes of 3 values. Following the prompts in the program will allow you to input the boundaries of each value, and later selecting encoding or decoding, the program will do its task. The default values used are s1, s2, and *, but the progam will prompt the user to override this if necessary.

An Encode specification for input would be for a message s1s2*, provide this as "s1,s2,*".

This is run in arithmeticEncodingDecode3v.py

**Modulo and Euler Function**


This is a series of programs that work on a modulo field to determine things like the euler function, inverse in the field, order etc. A full list of functionality is available when the program is run and simply follow the instructions inside the code.

This is run in moduloAndEulerFunction.py

**Fermat Factorisation**


This is code to determine the fermat factorisation of a number. This is quite straightforward and just an implementation of the mathematical algorithm.

This is in fermatFactorisation.py

**Pseudo Primes**


Psuedoprimes are primes that have a gcd of 0 with the base of the modulo field that they exist in. This tool takes in a number, and a list of bases to determine if any the number is a pseudoprime to any of these bases. 

NOTE: This tool does not check for strong pseduoprimes, although strong pseudoprimes must be pseudoprime.

This is in pseudoPrime.py