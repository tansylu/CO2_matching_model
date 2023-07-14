from model_class import string_embedder
from pickle_processor import ex_to_ei_flat, ei_to_ex_flat
model = string_embedder('paraphrase-MiniLM-L6-v2')

model.embed_list_of_strings(ex_to_ei_flat)
match = model.get_closest_from_list_of_strings('newspaper')
print(match)