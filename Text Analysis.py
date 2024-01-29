# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 18:05:46 2024

@author: User
"""


#Reading MastDict folder
MastDict_positive=open(r"C:\Users\User\Downloads\MasterDictionary\positive-words.txt",'r')
Positivetext=MastDict_positive.read()
MastDict_positive.close()
#print(Positivetext)
MastDict_negative=open(r"C:\Users\User\Downloads\MasterDictionary\negative-words.txt",'r')
Negativetext=MastDict_negative.read()
MastDict_negative.close()
#print(Negativetext)


#Reading StopWords folder
StopWords_1=open(r"C:\Users\User\Downloads\StopWords\StopWords_Auditor.txt",'r')
Auditortext=StopWords_1.read()
StopWords_1.close()
StopWords_2=open(r"C:\Users\User\Downloads\StopWords\StopWords_Currencies.txt",'r')
Currenciestext=StopWords_2.read()
StopWords_2.close()
StopWords_3=open(r"C:\Users\User\Downloads\StopWords\StopWords_DatesandNumbers.txt",'r')
DatesandNumberstext=StopWords_3.read()
StopWords_3.close()
StopWords_4=open(r"C:\Users\User\Downloads\StopWords\StopWords_Generic.txt",'r')
Generictext=StopWords_4.read()
StopWords_4.close()
StopWords_5=open(r"C:\Users\User\Downloads\StopWords\StopWords_GenericLong.txt",'r')
GenericLongtext=StopWords_5.read()
StopWords_5.close()
StopWords_6=open(r"C:\Users\User\Downloads\StopWords\StopWords_Geographic.txt",'r')
Geographictext=StopWords_6.read()
StopWords_6.close()
StopWords_7=open(r"C:\Users\User\Downloads\StopWords\StopWords_Names.txt",'r')
Namestext=StopWords_7.read()
StopWords_7.close()
#Final StopWords
StopWords=Auditortext+Currenciestext+DatesandNumberstext+Generictext+GenericLongtext+Geographictext+Namestext
#print(StopWords)


def Text_Analysis(filename):
    #accessing global data
    global Positivetext
    global Negativetext
    global StopWords
    #Cleaning using stopwords
    file=open(filename,'r',encoding="utf-8")
    filetext=file.read()
    filetext_cleaned=""
    filetext_length=0
    for word in filetext.split():
        if word not in StopWords:
            filetext_cleaned+=word+" "
            filetext_length+=1
    #print(filetext_cleaned)
    #print(filetext_length)
    
    #splitting cleaned data into words using nltk
    from nltk.tokenize import wordpunct_tokenize
    file_tokenized=wordpunct_tokenize(filetext_cleaned)
    #print(file_tokenized)
    Positive_score=0
    Negative_score=0
    for word in file_tokenized:
        #sorting into Positive and Negative
        if word in Positivetext:
            Positive_score+=1
        elif word in Negativetext:
            Negative_score+=1
   #print(Positive_score)
   #print(Negative_score)
   #Calculating Polarity Score
    Polarity_score=(Positive_score-Negative_score)/((Positive_score+Negative_score)+0.000001)
   #print(Polarity_score)
   #Calculating Subjectivity score
    Subjectivity_score=(Positive_score+Negative_score)/((filetext_length)+0.000001)
    #rint(Subjectivity_score)
    
    
    #Analysis of Readability
    #import nltk # wasnt working
    import re
    #from nltk.tokenize import PunktSentenceTokenizer
    #filetext_cleaned.decode("utf8")
    #splitting text into sentences
    sentences=re.split(r'[.!?]+', filetext_cleaned)
    filetext_sentencesno=len(sentences)
   #print(len(sentences))
   #calculating avgerage sentence length
    avg_sent_length=filetext_length/filetext_sentencesno
    
    #cleaning strings from punctuation marks
    filetext_cleaned2=""
    for word in filetext_cleaned:
        filetext_cleaned2+=re.sub(r'[^\w\s]', '', word)
    file_tokenized2=wordpunct_tokenize(filetext_cleaned2)  
    word_count=len(file_tokenized2)
    
    
    #pronoun and total characters
    tot_char=0
    pronoun=0
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    vowel_count=0
    complexword_count=0
    for word in file_tokenized2:
        tot_char+=len(word)
        if "US" not in word:
            pronoun_re = re.compile(r'\b(I|my|we|us|ours)\b',re.I)
            pronoun+= len(pronoun_re.findall(word))
        #elif word[-2:]!="es" and word[-2:]!="ed":
        for i in word:
                if i in vowels and i!="e":
                    vowel_count+=1
                elif i=="e":
                    if word[-2:]!="es" and word[-2:]!="ed":
                        vowel_count+=1
        syl_count=0
        for i in word:
            if i in vowels and i!="e":
                syl_count+=1
            elif i=="e":
                if word[-2:]!="es" and word[-2:]!="ed":
                    syl_count+=1
            elif syl_count>=2:
                complexword_count+=1
                break
   #print(vowel_count,"vowels",complexword_count,"complex")        
            
            
   #print(pronoun,tot_char)
    avg_word_length=tot_char/word_count
   #print(avg_word_length)
    #print(file_tokenized2)
    
    
    perc_complex=complexword_count/word_count
   #print(perc_complex)
    fog_index=0.4*(avg_sent_length+perc_complex)
   #print(fog_index)
    
    
    org_wordcount=len(filetext.split())
   #print(org_wordcount)
    org_sentcount=len(re.split(r'[.!?]+', filetext_cleaned))
   #print(org_sentcount)
    avg_numwordpersent=org_wordcount/org_sentcount
   #print(avg_numwordpersent)
    
   #returning all parameters calculated
    return [Positive_score,Negative_score,Polarity_score,Subjectivity_score,avg_sent_length,perc_complex,fog_index,avg_numwordpersent,complexword_count,word_count,vowel_count,pronoun,avg_word_length]

import pandas

#reading Output Data Structure.csv
csvFile = pandas.read_csv(r"C:\Users\User\Downloads\Output Data Structure.xlsx - Sheet1.csv")
#print(csvFile)
#creating loop to analyze every text file
for i in range(0,len(csvFile)):
     string='C:\\Users\\User\\Downloads\\Text Files\\'+csvFile['URL_ID'][i]
     #Storing analyzed data in List
     List=Text_Analysis(string)
     #Editing the csv file dataframe
     csvFile.loc[i, 'POSITIVE SCORE'] = List[0]
     csvFile.loc[i, 'NEGATIVE SCORE'] = List[1]
     csvFile.loc[i, 'POLARITY SCORE'] = List[2]
     csvFile.loc[i, 'SUBJECTIVITY SCORE'] = List[3]
     csvFile.loc[i, 'AVG SENTENCE LENGTH'] = List[4]
     csvFile.loc[i, 'PERCENTAGE OF COMPLEX WORDS'] = List[5]
     csvFile.loc[i, 'FOG INDEX'] = List[6]
     csvFile.loc[i, 'AVG NUMBER OF WORDS PER SENTENCE'] = List[7]
     csvFile.loc[i, 'COMPLEX WORD COUNT'] = List[8]
     csvFile.loc[i, 'WORD COUNT'] = List[9]
     csvFile.loc[i, 'SYLLABLE PER WORD'] = List[10]
     csvFile.loc[i, 'PERSONAL PRONOUNS'] = List[11]
     csvFile.loc[i, 'AVG WORD LENGTH'] = List[12]
#Creating a new csv file with the newly added data
csvFile.to_csv(r"C:\Users\User\OneDrive\Desktop\Output.csv",index=False)










