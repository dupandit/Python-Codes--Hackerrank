#----------------Example 1
import re
print (re.split(r's*','Here are some words'))

# import regex library
# . split to convert string into list
# r  to signify that pattern in ' ' should be processed specially and different than the regular string
# \s* signifies space. * means any number of spaces
# Next ' ' signifies the string to be acted on






#--------------Example 2
import re
print (re.split(r'(s*)','Here are some words'))

# () used for group and including. So it will split at space as well as include space in the list. Check the result






#---------------Example 3
import re
print (re.split(r'[a-f]','finqwenlaskdjriewasDKFEG'))

# This will split at alphabets a-f not including those. To include thuse add curly bracket () around them
#Notice that it will not be split up at F or E as regex is case sensitive







#-------------Example 4
import re
print (re.split(r'[a-f0-9]','finqwenlaskdjriewasDKFEG',flags=re.I|re.M))

# Notice we can add any range of characters in [a-fA-F0-9...]. To make it work case "insensitive" instead of typing in [] we can use flags like above. .I for case insenstive and .M to include multiline splitting. 







#-------------Example 5
import re
print (re.split(r'[a-f][a-f]','finqwefnlaskcdjriewabsDKFEG',flags=re.I|re.M))

# Here we splitted the string with Two character matching pair viz .[a-f][a-f] eg. cd, ab,etc.







#--------------Example 6
import re
print (re.findall(r'\d','oc324 main st.boulevard'))


# findall to search a pattern. IN the above examples we will get just the digits as output
#Note : \d = digits
#       \D = non-digits
#       \S = non-Space


import re
print (re.findall(r'\S','oc324 main st.boulevard'))







#---------------Example 7

#NOte : * = 0 or more ...
#       + = 1 or more ...
#       ? = 0 or 1 of ...
#      [5] = exact number of ...
#     {1,60] = range of number of ...






import re
print (re.findall(r'\d{1,5}','oc324 main st.boulevard'))

# \d{1,5} indicates that we need pattern of "1 to 5 digits continuously"









#----------------Example 8

import re
print (re.findall(r'\d{1,5}\s\w+','oc324 main st.boulevard'),re.I|re.M)


# \d{1,5} we know already number may be max 5 digits before the street name indicating (say city  code).

#then we know that there is a space for sure which is matched with \s.
#then there is a street name which can contain alphabets like "Gorman St" or numbers like "9th s treet".
#SO to cover both alphabets and numbers we use \w+.

#To summarize these important notations : 
#+ = 1 or more
#\w = alphanumeric
#\s = space




import re
print (re.findall(r'\d{1,5}\s\w+\s\w+\.','oc324 main street.boulevard'),re.I|re.M)



#MOre notations : 
# \. = regular period (.)
# . = ANy character but newline (\n)





