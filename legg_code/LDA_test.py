from pyspark.mllib.clustering import LDA, LDAModel
from pyspark.mllib.linalg import Vectors

# Load and parse the data
# [u'1 2 6 0 2 3 1 1 0 0 3', u'1 3 0 1 3 0 0 2 0 0 1', u'1 4 1 0 0 4 9 0 1 2 0', u'2 1 0 3 0 0 5 0 2 3 9', u'3 1 1 9 3 0 2 0 0 1 3', u'4 2 0 3 4 5 1 1 1 4 0', u'2 1 0 3 0 0 5 0 2 2 9', u'1 1 1 9 2 1 2 0 0 1 3', u'4 4 0 3 4 2 1 3 0 0 0', u'2 8 2 0 3 0 2 0 2 7 2', u'1 1 1 9 0 2 2 0 0 3 3', u'4 1 0 0 4 5 1 3 0 1 0']
data = sc.textFile("file:///home/w205/data_test/sample_lda_data.txt")
data = data.filter(lambda x: x!= "")
parsedData = data.map(lambda line: Vectors.dense([str(x) for x in line.strip().split(' ')]))
# [DenseVector([1.0, 2.0, 6.0, 0.0, 2.0, 3.0, 1.0, 1.0, 0.0, 0.0, 3.0]), DenseVector([1.0, 

# Index documents with unique IDs
corpus = parsedData.zipWithIndex().map(lambda x: [x[1], x[0]]).cache()
# [[0, DenseVector([1.0, 2.0, 6.0, 0.0, 2.0, 3.0, 1.0, 1.0, 0.0, 0.0, 3.0])], [1, DenseVector([1.0, 3.0, 0.0, 1.0, 3.0, 0.0, 0.0, 2.0, 0.0, 0.0, 1.0])]]

# Cluster the documents into three topics using LDA
ldaModel = LDA.train(corpus, k=3)

# Output topics. Each is a distribution over words (matching word count vectors)
print("Learned topics (as distributions over vocab of " + str(ldaModel.vocabSize()) + " words):")
topics = ldaModel.topicsMatrix()
for topic in range(3):
    print("Topic " + str(topic) + ":")
    for word in range(0, ldaModel.vocabSize()):
        print(" " + str(topics[word][topic]))
		
# Save and load model
model.save(sc, "myModelPath")
sameModel = LDAModel.load(sc, "myModelPath")
