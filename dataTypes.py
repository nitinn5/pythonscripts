# Create an empty dictionary: names_by_rank
names_by_rank = dict()

# Loop over the girl names
for rank, name in female_baby_names_2012.items():
    # Add each name to the names_by_rank dictionary using rank as the key
    names_by_rank[rank] = name
    
    
# Sort the names_by_rank dict by rank in descending order and slice the first 10 items
for listitem in sorted(names_by_rank,reverse=True)[:10]:
    print(names_by_rank[listitem])
