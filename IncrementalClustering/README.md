# Incremental Clustering


Incremental clusetering is useful when you have to add new data to a given
set of clusters. So rather than recomputing all the clusters all over again,
you can "incrementally" add new articles to the clusters.

In our project, we have used this method to classify documents returned by
crawlers over time.

## Module 1 - Pre-Processing:
  Usage of NER and WordNet libraries.
  Words are tagged with their POS and then categorized into entities
  like Names, Places, Organizations etc., i.e., proper nouns and common
  nouns (using NER).
  The extracted common nouns are converted into lemmatized form (using WN).
   
## Module 2 - Word Counts:
  Calculates the frequency of each word from the expected vector space
  (feature set).
  The vector space consists of the union of all the words that were obtained
  after pre-processing all the documents that were fed to module 1 during the
  construction of the inital structure of the clusters, prior to incremental
  clustering.
  This is done to ensure that the documents will remain in the same vector
  space.
  
## Module 3 - Calculating Tf-Idf:
  Each word in the vector space is assigned a weight for every document based
  on its TfIdf score.
  
## Module 4 - Create Feature Set:
  Thresholding is performed to reduce the effect of words having low TfIdf scores.
  Dimensionality reduction is then performed to remove words from the vector space
  if they have a score of 0 for all documents in the data set.
  The remaining words are used as the final feature set and the document vectors
  are shortened accordingly.
  
  *NOTE: In the case of Incremental Clustering, the words which were part of the
  feature set generated prior to incremental clustering will be retained to ensure
  that the document vectors belong to the same vector space.*
  
## Module 5 - Cosine Similarity:
  Calculate the cosine similarity for each new document fetched by the crawlers with
  the original set of documents collected prior to incremental clustering.
  
## Module 6 - Classifier:
  This module finally assigns each new article a cluster based on the average cosine
  similarity scores of the document with each cluster.
  The average similarity is calculated as sum of the Cosine Similarities of each document
  from that cluster with this new document. This is done for each cluster. These values
  are then normalised by dividing by the sizes of the respective clusters.
  An optional threshold can be set such that certain documents having very low similarity
  with all clusters can be discarded. (Set to 0 if not required)
  
## Module 7 - Computing Statistics:
  It returns the percentage of documents classified in each cluster, and also returns the
  number of unclassifed documents.
