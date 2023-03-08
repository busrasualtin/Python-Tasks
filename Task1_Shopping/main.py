# The HR department asks you to list the items you would need to improve your work efficiency

# Mandatory:
# Laptop
# Headset
# Second monitor

# Optional:
# Mousepad
# USB drive
# External drive
# 📌 Create a shopping list that contains items above and print it.
# Create the item_list
item_list = ['Laptop', 'Headset', 'Second Monitor', 'Mousepad', 'USB drive', 'External drive']

# Print the list
print(item_list)

# What is mandatory and what is optional?
# 📌 Use list slicing to devide your list in two list: 'mandatory_item_list' and 'optional_item_list' and print both to the screen.
# Use list slicing to divide the mandatory items
mandatory_item_list = item_list[0:3]

# Use list slicing to divide the optional items
optional_item_list = item_list[3:6]

# Print both to the screen
print(mandatory_item_list)
print(optional_item_list)

# Next, you will have to go and purchase these items, the finance department confirmed a budget of $5000.
# 📌 Assign 5000 to a variable called limit, so you know how much you can spend.
limit = 5000

# Before you start shopping yo need to find the best items that you can buy within the company budget.
# 📌 Prepare a dictionary called “price_sheet” that includes the items as keys and the prices as values.
# Create a dictionary that contains each item and its price
price_sheet = {
    'Laptop': 1500,
    'Headset': 100,
    'Second Monitor': 200,
    'Mousepad': 50,
    'USB drive': 70,
    'External drive': 250
}

# Initialize the cart list
cart = []


# Define the "add_to_cart" function
# Define a function for both adding items to the cart and removing them from the item_list.
# 📌 The "add_to_cart" function should take the item name and the quantity to buy as an argument.
def add_to_cart(item, quantity):
    cart.append((item, quantity))
    item_list.remove(item)


# Define a function that will create an invoice.
# 📌 The "create_invoice" function should calculate the taxes of each item (18%) and add it to the total amount.
# Define the "create_invoice" function
def create_invoice():  # fatura oluşturma
    total_amount_inc_tax = 0  # tax dahil fiyat
    for item, quantity in cart:
        price = price_sheet[item]
        tax = 0.18 * price
        total = (tax + price) * quantity
        total_amount_inc_tax += total
        print("Item:", item, "\t",
              "Price:", price, "\t",
              "Quantity:", quantity, "\t",
              "Tax:", tax, "\t",
              "Total:", total, "\n")
    print("After the taxes are applied the total amount is:", "\t", total_amount_inc_tax)
    return total_amount_inc_tax


# Define a function for the checkout.
# 📌 The "checkout" function should subtract the total amount from the budget
# and print a statement to inform if the payment was successful.
def checkout():
    global limit
    total_amount = create_invoice()
    if limit == 0:
        print("You don't have any budget")
    elif total_amount > limit:
        print("The amount you have to pay is above the spending limit. You have to drop some items")
    else:
        limit -= total_amount
        print(f"The total amount (incl. taxes) you've paid is {total_amount}. You have {limit} dollars left. ")


# Call the "add_to_cart" function for each item

# Add first item to cart
add_to_cart("Laptop", 1)

# Add second item to cart
add_to_cart("Headset", 8)

# Add third item to cart
add_to_cart("Second Monitor", 1)

# Add fourth item to cart
add_to_cart("Mousepad", 1)

# Add fifth item to cart
add_to_cart("USB drive", 2)

# Add last item to cart
add_to_cart("External drive", 4)

# Call the creation "checkout" function to pay for all your items
checkout()