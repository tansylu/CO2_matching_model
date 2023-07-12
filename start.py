from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

data = {
    'Paddy rice': ['rice', 'rice seed, for sowing'],
    'Wheat': ['wheat grain', 'wheat grain, feed', 'wheat grain, feed, organic', ],
    'Cereal grains nec': ['barley grain, feed', 'barley grain, feed, organic', ],
    'Vegetables, fruit, nuts': ['peanut', 'peanut seed, at farm', ],
    'Oil seeds': ['rape seed', 'rape seed, organic', ],
    'Sugar cane, sugar beet': ['sugar beet', 'sugarcane', ],
    'Plant-based fibers': ['grass fibre', 'cotton fibre', ],
    'Crops nec': ['cocoa bean', 'coffee, green bean', ],
    'Cattle': ['red meat, live weight', 'cattle for slaughtering, live weight']
}

sentences1 = list(data.keys())
sentences2 = sum(data.values(), [])




# Compute embeddings for both lists
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)

# Compute cosine similarities
cosine_scores = util.cos_sim(embeddings1, embeddings2)

# Output all pairs with their scores
for i in range(len(sentences1)):
    for j in range(len(sentences2)):
        if(cosine_scores[i][j] >0.7):
            print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[j], cosine_scores[i][j]))



# Single list of sentences - Possible tens of thousands of sentences
sentences = ['The cat sits outside',
             'A man is playing guitar',
             'I love pasta',
             'The new movie is awesome',
             'The cat plays in the garden',
             'A woman watches TV',
             'The new movie is so great',
             'Do you like pizza?']

paraphrases = util.paraphrase_mining(model, sentences, corpus_chunk_size=len(sentences), top_k=1)

for paraphrase in paraphrases[0:10]:
    score, i, j = paraphrase
    print("{} \t\t {} \t\t Score: {:.4f}".format(sentences[i], sentences[j], score))