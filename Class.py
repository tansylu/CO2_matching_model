from sentence_transformers import SentenceTransformer, util
import numpy as np
import pickle

class string_embedder:
    def __init__(self, MODEL):
        """

        :rtype: object
        """
        # MODEL = 'all-MiniLM-L6-v2' a different model to test out
        # initialize the embedder transformer class and use a single variable
        self.model = SentenceTransformer(MODEL)

    def embed_list_of_strings(self, list_of_strings: [str]):
        #### embedding of a list of words - non topic specific
        #### to be used with the function get_closest_from_list_of_strings to get the closest term
        if not type(list_of_strings) == 'list':
            list_of_strings = list(list_of_strings)
            
        self.list_of_strings= list_of_strings
        self.embeddings = self.model.encode(self.list_of_strings)


    def get_closest_from_list_of_strings(self, item: str):
        #### returns the closest term to the string item from the list that was sent to 'embed_list_of_strings'
        val = util.cos_sim(self.embeddings, self.model.encode(item))
        amax = np.argmax(val)
        return self.list_of_strings[amax]
    


#load data set of matched products
data_categories=pickle.load(open("product_EX_to_EI.pickle", "rb")).values()
d = []
for x in data_categories:
    for e in x:
        d.append(e)
model = string_embedder('paraphrase-MiniLM-L6-v2')

model.embed_list_of_strings(d)
match=model.get_closest_from_list_of_strings('newspaper')
print(match)