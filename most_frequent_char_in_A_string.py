"""   Assignment 7  """
"""my_captain_Assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LLWVvopwtDg5e2aRH0WSbnkgiX9whPRr
"""

# Write a Python Program for printing the letters in the string in decreasing order of frequency.

def most_frequent(s):
  d = {}
  s = list(s)
  
  for i in s:
    if ( i in d):
      d[i] = d[i]+1 
    else:
      d[i] = 1 
  l = reversed(sorted(d.values()))
  d1 = {}
  
  for v in l:
    for k,j in d.items():
      count = 1
      if( v == j and count == 1 ):
        d1.setdefault(k,v)
        count = count + 1
  
  
  for k,v in d1.items(): 
    print( k , v , sep="=",end = " " )
  

  

S = input("Please enter a string : ")
most_frequent(S)
