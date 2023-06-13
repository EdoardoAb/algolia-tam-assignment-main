import json
# Opening Products JSON file
original_products = json.load( open('.\data\products.json', encoding="utf8") )

# Just to see how many records I am about to upload to the Algolia index
print(len(original_products))

"""
  Manipulating the original dataset to apply a 20% discount. The final price is rounded to the lowest whole number, and formatted with two decimal zeros to be consistent with the original pricing formatting.
  Also, adding a boolean property to keep track of discounted product just in case this needs to be used when consuming the indexed results (e.g. pushing discounted products higher up in the result hits)
"""
import math
updated_products = []

for product in original_products[:5]:
  print(product)
  product['discounted'] = False
  if 'Cameras & Camcorders' in product['categories']:
    product['price'] = format(math.floor( product['price'] * 0.8 ), '.2f')
    product['discounted'] = True
    
  updated_products.append(product)


from algoliasearch.search_client import SearchClient

client = SearchClient.create('61799YVHWS', '2ab2f8f7286be6fab11166bc10741f39')
index = client.init_index('cse_test')
index.save_objects(updated_products).wait()

# The updated products JSON array is now fully sent to Algolia index "cse_test"

