
'''   Assignment 4    '''

# Write Python program to accept a filename from the user and print the extension of that.

fname = input("Input the Filename:")
for i in fname:
  if( i == "."):
    s = fname.index(i)+1
    ext = fname[s:]

if( ext == "py"):
  ext = 'python'
  print("The extension of the file is :",ext)
 
if( ext == "bin"):
  ext = 'binary'
  print("The extension of the file is :",ext)
  ext = ""
  
if( ext == "txt"):
  ext = 'text'
  print("The extension of the file is :",ext)
  ext = ""

if( len(ext) >=3 ):
  print("The extension of the file is :",ext)
