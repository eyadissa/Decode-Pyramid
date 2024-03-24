Given a list like  
  
3 love  
6 computers  
2 dogs  
4 cats  
1 I  
5 you

This function finds the values of the endge of a pyramid such that

1  
2 3  
4 5 6  
  
results in 1 3 6  
  
then returns the related sequence of words:  
I love computers


Details:  
First the code does basic checks on the input file to see if it is accessible and if it is a valid text file (UTF-8 encoded). Next the file lines are read into a dictionary where the number is set as the key and the word is set as the value. It is assumed that each line only has those two items and that they are separated by a space. The code then separates the keys into a list of integers and puts them in ascending order. This list is then ready to be processed into the triangle formation to find the last number in each pyramid line (the triangle edge). The indices of the triangle edge follow a known sequence called triangular numbers and are equivalent to the total number of numbers in the triangle up to the end of that line. For any given line number (i), those indices are equal to i*(i+2)//2. That formula is then used to retrieve the values at the keys at those indexes. The values are concatenated into a single string, printed and returned. 
