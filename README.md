# Text-Analysis-and-Web-Scraping
Extracted textual data articles from the URLs and performed text analysis to compute some defined parameters.

WEB SCRAPING
* I used Beautifulsoup4 to extract data from the news articles link given in the sheet Input.xlsx. I saved them in separate text files in a folder with name as URL_ID.
* The first part is over.

TEXT ANALYSIS
* First I had to read the Master Dicitonary and Stopwords folder.
* I kept Positive and Negative words in separate string variables.
* I combined all Stopwards text files into one string and stored it in a variable.
* I created a function named “Text_Analysis” which accepted a file path as its input
* I read that particular file and removed the words found in Stopwords string. 
* I used nltk.tokenize.wordpunct_tokenize to separate words in the string and calculate the no of Positive and Negative words.
* Calculated the POLARITY SCORE and SUBJECTIVITY SCORE from the formula given.
* I used Regex module to split the text into sentences as nltk wasn’t working for sentences. I got AVG SENTENCE LENGTH from this. 
* Removed the puncuations from the words and calculated WORD COUNT.
* Using Vowels, for loop and re.compile, calculated the COMPLEX WORD COUNT, PERSONAL PRONOUNS and SYLLABLE PER WORD.
* From the above data I was able to get the remaining variables FOG INDEX, PERCENTAGE OF COMPLEX WORDS, AVG NUMBER OF WORDS PER SENTENCE, FOG INDEX
* At last I calculated AVG WORD LENGTH. 
* I saved all these values in a list and returned it in the function.
* I read the Output Data Structure.xlsx file and using URL_ID executed the Text_Analysis function to every URLs text files and got the parameters and stored them into the missing values in the dataframe and kept it in a new file Output.csv.

INSTRUCTIONS TO RUN  Text Analysis.py FILE
* First run Scraping of websites.py file. It will create Text Files folder with 100 text files in it with correct names. ( Make sure you have download and loaded Input.xlsx file. 
* Put that folder as a path in “string” variable at line 160 of Text Analysis.py
* Add the path of Output Data Structure.xlsx file in “csvFile” variable in line 156.
* You will get a file named Output.csv in the same path. 


