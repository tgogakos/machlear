#!/usr/bin/env
import sys
import csv
from Bio import Entrez as ez
from Bio import Medline as ml
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# import gensim
# from sklearn.manifold import TSNE
import operator
import matplotlib.pyplot as plt
ez.email = "tasos.gogakos@gmail.com"

#set search term (e.g. DLBCL or DLBCL[MeSH terms])
t = sys.argv[1]

##Note: to find of all available search types for pubmed:
# handle = ez.einfo(db="pubmed")
# r = ez.read(handle)
# for field in r["DbInfo"]["FieldList"]:
#   print("%(Name)s, %(FullName)s, %(Description)s" % field)

#Getting info about pubmed
hPubmed = ez.einfo(db="pubmed")
rPubmed = ez.read(hPubmed)

print("Searched {} pubmed entries as of {}". format(rPubmed['DbInfo']['Count'], rPubmed['DbInfo']['LastUpdate']))  

#get handle for data, read it, and close it
h = ez.egquery(term=t)
r = ez.read(h)

#find how many entries are returned by the search
for row in r["eGQueryResult"]:
  if row["DbName"]=="pubmed":
    total_entries = int(row["Count"])
    print("There are {} articles relevatnt to {} in pubmed".format(row["Count"], t))
    
#get the list of PMIDs
h2 = ez.esearch(db="pubmed", term= t, retmax=total_entries)    
r2 = ez.read(h2)
h2.close()
# ret_items = sys.argv[2]
idlist = r2["IdList"]

print("Returning information for {} items".format(len(idlist)))

#fetch corresponding Medline records. Here resuls are split becuase maxret is 10,000 and restart parameter does not work in biopython. The step parameter needs to be reset, so that it is never higher than 10,000
step = int(len(idlist)/3) +1 
if step > 10000:
    print("Iteration step is {}, which is greater that 10,000".format(step))
    exit()
else:
    print("Iteration step is {}, which is acceptaple".format(step))

h3 = ez.efetch(db="pubmed", id=idlist[:step], rettype="medline", retmode="xml")
r3 = ez.read(h3)
h4 = ez.efetch(db="pubmed", id=idlist[step:step*2], rettype="medline", retmode="xml")
r4 = ez.read(h4)
h5 = ez.efetch(db="pubmed", id=idlist[step*2:], rettype="medline", retmode="xml")
r5 = ez.read(h5)

# #get tokenized words and/or sentences
# sentences = []
# tokens = []
# tokens_filt = []
#
# #remove stop words
# stop_words = set(stopwords.words('english'))

years1 = {}
years2 = {}

def getYears(x):
    """Used to parse years for each of the sublists created above. Results are added to years1 dict defined above, so that years1
    gets updted in every iteration step"""

    for record in x['PubmedArticle']:
        try:
            year1 = record["MedlineCitation"]["Article"]['Journal']['JournalIssue']['PubDate']['Year']
            if year1 in years1:
                years1[year1] += 1
            else:
                years1[year1] = 1
        except:
            pass
    return years1

getYears(r3)
getYears(r4)
x = getYears(r5)
print(x)

####### To capture dates that are not properly indexed#####
#     try:
#         year2 = record["MedlineCitation"]["Article"]['Journal']['JournalIssue']['PubDate']['MedlineDate']
#         # if year1 in years1:
#         #     years1[year1] += 1
#         # else:
#         #     years1[year1] = 1
#         if year2 in years2:
#             years2[year2] += 1
#         else:
#             years2[year2] = 1
#     except:
#         pass

sorted_years1 = sorted(years1.items(), key = operator.itemgetter(0), reverse = True)

#Print to output file
out_file = sys.argv[1] + ".csv"

with open(out_file, 'w') as of:
    csv_writer = csv.writer(of)
    csv_writer.writerow(['year', 'count'])
    csv_writer.writerows(sorted_years1)
















# if 'Abstract' in record["MedlineCitation"]["Article"]:
#   ab_text = record["MedlineCitation"]["Article"]['Abstract']['AbstractText'][0].strip()

    
 # # tokenized_abstract = sent_tokenize(ab_text)
 #  sentences.extend(sent_tokenize(ab_text))
 #  words = word_tokenize(ab_text)
 #  #if a list of lists of tokens is required:
 #  tokens.append(words)
 #  tokens_filt.extend([word for word in words if word not in stop_words])
 #  ##if one list of tokens is required:
 #  #tokens.extend(words)


# model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
# model = gensim.models.Word2Vec(tokens_filt)
# output = open("test.txt", 'wb')
# model.save(output)

# tsne = TSNE(n_components=2, random_state=1, metric='precomputed')
# X_tsne = tsne.fit_transform(distance_word2vec)
# plt.scatter(X_tsne[:, 0], X_tsne[:, 1], s=10)
# for label, x, y in zip(feature_terms, X_tsne[:, 0], X_tsne[:, 1]):
#     plt.annotate(label, xy=(x, y), xytext=(0, 0), fontsize=7, textcoords='offset points')
# plt.show()


  # print("%(Name)s, %(FullName)s, %(Description)s" % field)
  # #print(r['DbInfo']['LinkList'])
  # print("Searched {} pubmed entries as of {}". format(r['DbInfo']['Count'], r['DbInfo']['LastUpdate']))


#-------------------------------
###Alternatively, you can use an iterator/list by using the Medline parser. The keys are different in that case.
##to save records as iterator
#records = ml.parse(h3)
#to save records as list
# records = list(ml.parse(h3))
# for record in records:
#   # print("title: ", record.get("TI"))#, "?"))
#   # print("authors: ", record.get("AU"))#, "?"))
#   # print("source: ", record.get("SO"))#, "?"))
#   #print("source: ", record.get("AB").strip())#, "?"))
#   print(record.keys())#['MedlineCitation']['Article']['Abstract'])
#   print("----")
