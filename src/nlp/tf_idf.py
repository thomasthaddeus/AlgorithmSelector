from collections import Counter
import math

class TFIDF:
    def __init__(self, documents):
        self.documents = documents
        self.corpus = [doc.split() for doc in documents]
        self.idf_values = self.calculate_idf()

    def calculate_tf(self, document):
        """Calculate term frequency for a given document."""
        tf_dict = {}
        count_words = Counter(document)
        total_words = len(document)
        for word, count in count_words.items():
            tf_dict[word] = count / total_words
        return tf_dict

    def calculate_idf(self):
        """Calculate inverse document frequency across a set of documents."""
        idf_dict = {}
        total_documents = len(self.corpus)
        all_words_set = set(word for doc in self.corpus for word in doc)

        for word in all_words_set:
            count = sum(word in doc for doc in self.corpus)
            idf_dict[word] = math.log(total_documents / (1 + count))
        return idf_dict

    def calculate_tfidf(self, document):
        """Calculate TF-IDF for a given document."""
        tfidf_dict = {}
        tf_dict = self.calculate_tf(document.split())

        for word, tf_val in tf_dict.items():
            tfidf_dict[word] = tf_val * self.idf_values.get(word, 0)
        return tfidf_dict

# Example usage
documents = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "the cat sat on the dog"
]
tfidf = TFIDF(documents)

for doc in documents:
    print(f"TF-IDF for '{doc}':")
    tfidf_scores = tfidf.calculate_tfidf(doc)
    for word, score in tfidf_scores.items():
        print(f" - {word}: {score:.5f}")
