# News Article Clustering

Semi-supervised learning model to categorize online news articles into genres.

Modules included:
# Module 1 - Pre-Processing:
  • Simple model:
    Extract valid words after removal of non-ASCII characters
    
  • Advanced Model:
    Usage of NER and WordNet libraries.
    Words are tagged with their POS and then categorized into entities
    like Names, Places, Organizations etc., i.e., proper nouns and common
    nouns (using NER).
    The extracted common nouns are converted into lemmatized form (using WN).
   
# Module 2 - Word Counts:
  Calculates the frequency of each word from the expected vector space
  (feature set).
  The vector space consists of the union of all the words that were obtained
  after pre-processing all the documents that were fed to module 1.
  
# Module 3 - Calculating Tf-Idf:
  Each word in the vector space is assigned a weight for every document based
  on its TfIdf score.
  
# Module 4 - Create Feature Set:
  Thresholding is performed to reduce the effect of words having low TfIdf scores.
  Dimensionality reduction is then performed to remove words from the vector space
  if they have a score of 0 for all documents in the data set.
  The remaining words are used as the final feature set and the document vectors
  are shortened accordingly.
  
# Module 5 - Cosine Similarity:
  Calculate the cosine similarity for every pair of documents in the dataset
  
# Module 6 - Selection of seeds for clustering:
  Select some pre-classified seeds to calculate the initial centroid positions
  for Module 7.
  These are selected based on their feature coverage, i.e., the sum of the
  magnitudes on each axis for every vector.
  
# Module 7 - SK Means Clustering:
  Performs Spherical K-Means Clustering on the documents and returns k clusters.
  
# Module 8 - Accuracy Check:
  Since we have also classified the data based on our own interpretation or that
  provided by the news source, we can check the accuracy of the model.
  It computes a confusion matrix along with standard accuracy measures like
  F1 score.
