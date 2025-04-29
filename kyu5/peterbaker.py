"""
Write a function cakes(), which takes the recipe (object) 
and the available ingredients (also an object) and returns 
the maximum number of cakes Pete can bake (integer). 
For simplicity there are no units for the 
amounts (e.g. 1 lb of flour or 200 g of sugar are 
simply 1 or 200). Ingredients that are not present in the 
objects, can be considered as 0.
"""

def cakes(recipe, available):
    max = float("inf")
    for ingr, cant in recipe.items():
        if ingr not in available:
            return 0

        how_many = available[ingr] // cant

        if how_many < max:
            max = how_many
    
    return max