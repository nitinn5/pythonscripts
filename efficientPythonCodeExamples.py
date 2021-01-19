#:::::::::::::  Built-in practice: enumerate() :::::::::::::::::::::::::::::::::::::::::::

# Rewrite the for loop to use enumerate
indexed_names = []
for i, name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)


#:::::::::::::  Built-in practice: map()      :::::::::::::::::::::::::::::::::::::::::::

# Use map to apply str.upper to each element in names
names_map  = map(str.upper,names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)

#:::::::::::::  Basic NumPy indexing and operations     :::::::::::::::::::::::::::::::::

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums>6])

# Double every element of nums
nums_dbl = nums*2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)





