from gensim.models import Word2Vec
sentences = [
["I", "love", "machine", "learning"],
["Deep", "learning", "is", "fun"],
["Python", "is", "great", "for", "AI"]
]
model = Word2Vec(sentences, vector_size=50, window=3,
min_count=1, workers=2)
vector = model.wv['Python']
print(vector)
similar = model.wv.most_similar('learning', topn=3)
print(similar)