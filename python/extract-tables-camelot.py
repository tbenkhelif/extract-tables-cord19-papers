#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import json
import pickle
from tqdm.notebook import tqdm
from os import listdir
from os.path import isfile, join

# ### if number of lines is > 40 ->reject
# ### if average size of cell is > 25 -> reject


def isItATable(df):
    df.dropna(inplace=True) 
    if df.shape[0]>50:
        return False
    
    for column in df.columns:
        s = np.mean(df[column].map(str).apply(len))
        if s > 15:
            return False
    return True


import camelot
validTables = []
#tables = camelot.read_pdf(r'c:/Data/Covid_papers/Caruccio et al. - 2016 - On the Discovery of Relaxed Functional Dependencie.pdf', flavor='stream',pages='all',multiple_tables=True)
tables = camelot.read_pdf(r'c:/Data/Covid_papers/1471-2105-7-451.pdf', flavor='stream',pages='all',multiple_tables=True)
tables.export('foo.json', f='json', compress=True)
for n in range(len(tables)):
    df = tables[n].df
    if isItATable(df):
        validTables.append(tables[n].df)


def extractTablesFromPaper(paper):
    validTables = []
    tables = camelot.read_pdf(paper, flavor='stream',pages='all',multiple_tables=True)
    #tables.export('foo.json', f='json', compress=True)
    for n in range(len(tables)):
        df = tables[n].df
        if isItATable(df):
            validTables.append(tables[n].df)    
    return validTables


validTablesJson = [v.to_json() for v in validTables]


with open("c:/Data/Covid_papers/article_json.json", 'w') as outfile:
    outfile.write(json.dumps(validTablesJson))



papers_folder = r"C:\Data\Covid_papers\PCM_papers_scrapped"


onlyfiles = [join(papers_folder, f) for f in listdir(papers_folder) if isfile(join(papers_folder, f))]



paper_x_tables = {}
for article in tqdm(onlyfiles):
    print(article)
    
    try :
        validTables = extractTablesFromPaper(article)
        print(validTables)
        if len(validTables) > 0 :
            validTablesJson = [v.to_json() for v in validTables]
            paper_x_tables[article.split('\\')[-1]] = validTablesJson
    except:
        print('File format not supported')
    


with open('tables.json', 'w') as fp:
    json.dump(dict, paper_x_tables, sort_keys=True, indent=4)




# # Store data (serialize)
# with open('filename.pickle', 'wb') as handle:
#     pickle.dump(paper_x_tables, handle, protocol=pickle.HIGHEST_PROTOCOL)

# # Load data (deserialize)
# with open('filename.pickle', 'rb') as handle:
#     unserialized_data = pickle.load(handle)

# print(paper_x_tables == unserialized_data)



with open('paper_x_tables.pickle', 'rb') as handle:
    unserialized_data = pickle.load(handle)


with open("name_x_title.pickle", "rb") as fp:   # Unpickling
    name_x_title = pickle.load(fp)


smalldict = {}
for k,v in name_x_title.items():
    if len(v)>5:
        smalldict[k] = v
    


countI = 0

for i,j in tqdm(unserialized_data.items()):
    print(i)
    if i in smalldict.keys():
        old = i
        i = smalldict[i].replace(".pdf","")
    countI += 1 
    countJ = 0
    for js in j:
        y = json.loads(js)
        #print(y)
        df = pd.DataFrame(y)
        try :
            df.to_csv(r"Extracted_tables/"+i+"_"+str(countJ)+".csv",index=False)
        except:
            df.to_csv(r"Extracted_tables/"+old+"_"+str(countJ)+".csv",index=False)
        countJ += 1
        print(df)




































































# In[63]:


listPapers =  list(unserialized_data.keys())

with open("listPapers.picle", "wb") as fp:   #Pickling
    pickle.dump(listPapers, fp)


# In[7]:


from pdfrw import PdfReader

reader = PdfReader(r'C:\Data\Covid_papers\PCM_papers_scrapped\pmed.0020174.pdf')


# In[64]:


with open("listPapers.picle", "rb") as fp:   # Unpickling
    listPapers = pickle.load(fp)


# In[8]:


reader.Info

