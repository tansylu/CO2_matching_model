from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# data = {
    # 'Paddy rice': ['rice', 'rice seed, for sowing'],
    # 'Wheat': ['wheat grain', 'wheat grain, feed', 'wheat grain, feed, organic', ],
    # 'Cereal grains nec': ['barley grain, feed', 'barley grain, feed, organic', ],
    # 'Vegetables, fruit, nuts': ['peanut', 'peanut seed, at farm', ],
    # 'Oil seeds': ['rape seed', 'rape seed, organic', ],
    # 'Sugar cane, sugar beet': ['sugar beet', 'sugarcane', ],
    # 'Plant-based fibers': ['grass fibre', 'cotton fibre', ],
    # 'Crops nec': ['cocoa bean', 'coffee, green bean', ],
    # 'Cattle': ['red meat, live weight', 'cattle for slaughtering, live weight']
# }

# sentences1 = list(data.keys())
# sentences2 = sum(data.values(), [])




# Compute embeddings for both lists
# embeddings1 = model.encode(sentences1, convert_to_tensor=True)
# embeddings2 = model.encode(sentences2, convert_to_tensor=True)

# Compute cosine similarities
# cosine_scores = util.cos_sim(embeddings1, embeddings2)

# Output all pairs with their scores
# for i in range(len(sentences1)):
    # for j in range(len(sentences2)):
        # if(cosine_scores[i][j] >0.7):
            # print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[j], cosine_scores[i][j]))


#Using the same model as before, we focus on paraphrasing
# Single list of sentences - Possible tens of thousands of sentences


categories = [
             'red meat, live weight', 'cattle for slaughtering, live weight',
             'wheat grain', 'wheat grain, feed', 'wheat grain, feed, organic',
             'rape seed', 'rape seed, organic',
             'peanut', 'peanut seed, at farm', 'banana', 'apple','oats','tomatoe','sausage','cow']

product=[input("Product to analyze: ")]
categories.extend(product)
#We add the product to analyze to the list and the use paraphasing to see where it relates the most

paraphrases = util.paraphrase_mining(model, categories, corpus_chunk_size=len(categories), top_k=1) 
#Top_k=1 will provide just the best match for each sentence in the list

for paraphrase in paraphrases[0:3]:
    score, i, j = paraphrase
    print("{} \t\t {} \t\t Score: {:.4f}".format(categories[i], categories[j], score))