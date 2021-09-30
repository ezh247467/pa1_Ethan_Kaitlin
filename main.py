#Part 1.1
def ounce_to_grams(weight_in_oz):
  return weight_in_oz * 28.35

#Part 1.3
def grams_to_ounce(weight_in_g):
  return weight_in_g / 28.35

#Part 1.2
weight_in_oz_str = input("Enter the weight in oz: ")
#weight_in_oz_str = "4.5" #Fill in this line
weight_in_oz = float(weight_in_oz_str) #Fill in this line
weight_in_g = ounce_to_grams(weight_in_oz)
print("Weight in grams =", weight_in_g)

#Part 1.4
weight_in_oz = grams_to_ounce(weight_in_g)
print("Weight converted back to ounces =", weight_in_oz)
