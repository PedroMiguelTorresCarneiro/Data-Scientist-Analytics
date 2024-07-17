import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# Funnel for Cool T-Shirts Inc.

''' [1]
Inspect the DataFrames using print and head:

- 'visits' lists all of the users who have visited the website
- 'cart' lists all of the users who have added a t-shirt to their cart
- 'checkout' lists all of the users who have started the checkout
- 'purchase' lists all of the users who have purchased a t-shirt
'''
print('\nEX 1 ----------------\n')
print('\nVisits LIST')
print(visits.head())
print('\nCart LIST')
print(cart.head())
print('\nCheckout LIST')
print(checkout.head())
print('\nPurchase LIST')
print(purchase.head())

'''[2]
Combine visits and cart using a left merge.
'''
print('\nEX 2 ----------------\n')
mergedList = pd.merge(visits, cart, how='left')
print(mergedList.head())

'''[3]
How long is your merged DataFrame?
'''
print('\nEX 3 ----------------\n')
mergedList_size = mergedList.user_id.count()
print("Merged List Size: ", mergedList_size)

'''[4]
How many of the timestamps are null for the column cart_time?

What do these null rows mean?
R: Significa que aquele user ainda não fez uma compra 
'''
print('\nEX 4 ----------------\n')
null_timeStamps = mergedList.cart_time.isnull().sum()
print("Number of null timeStamps: ", null_timeStamps)

'''[5]
What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?

Note: To calculate percentages, it will be helpful to turn either the numerator or the denominator into a float, by using float(), with the number to convert passed in as input. Otherwise, Python will use integer division, which truncates decimal points.
'''
print('\nEX 5 ----------------\n')
total_users = mergedList.user_id.count()
no_cart_users = mergedList.cart_time.isnull().sum()
percent_no_cart = (no_cart_users/total_users)*100

print("Percentage of users who visited but did not place a t-shirt in their cart: {:.3f}%".format(percent_no_cart))

'''[6]
Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?
'''
print('\nEX 6 ----------------\n')
checkoutList = pd.merge(cart, checkout, how='left', on='user_id')
#print(checkoutList)
total_checkout_users = checkoutList.user_id.count()
no_checkout_users = checkoutList.checkout_time.count()
percent_no_check = (no_checkout_users/total_checkout_users)*100

print("Percentage of users who put items in their cart but did not proceed to checkout: {:.2f}%".format(percent_no_check))

'''[7]
Combine visits and cart using a left merge.
'''
print('\nEX 7 ----------------\n')
all_data = pd.merge(visits,cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

print(all_data.head())

'''[8]
What percentage of users proceeded to checkout, but did not purchase a t-shirt?
'''
print('\nEX 8 ----------------\n')
total_checkouts = all_data.checkout_time.notnull().sum()
no_purchase_users = all_data.checkout_time.notnull() & all_data.purchase_time.isnull()

percent_check_no_buy = (no_purchase_users.sum()/total_checkouts)*100 

print("Percentage of users who checkout their cart but did not proceed to purchaset: {:.2f}%".format(percent_check_no_buy))


'''[9]
Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?

How might Cool T-Shirts Inc. change their website to fix this problem?
R: 
  - Simplify the Checkout Process(Reduce Steps, Guest Checkout), 
  - Transparent Pricing(Clear Cost Breakdown, Shipping Information), 
  - Trust and Security(Secure Payment Gateway, Privacy Policy),
  - Multiple Payment Options(Payment Methods, Save Payment Information),
  - Cart Recovery Tactics(Abandoned Cart Emails, Push Notifications),
  - Incentives and Discounts(Discount Codes, Free Shipping),
  - Customer Support(Live Chat, Help Center),
  - User Experience (UX) Enhancements(Mobile Optimization,Loading Speed)
'''
print('\nEX 9 ----------------\n')

total_users = all_data.user_id.count()

# users who visited but did not add to cart
t_cart_u = all_data.cart_time.notnull().sum()
p_no_cart = ((total_users - t_cart_u)/total_users)*100

#users who added to cart but did not checkout
t_check_u = all_data.checkout_time.notnull().sum()
p_no_check = ((total_users - t_check_u)/total_users)*100

# users who proceeded to checkout but did not purchase
t_buy_u = all_data.purchase_time.notnull().sum()
p_no_buy = ((total_users - t_buy_u)/total_users)*100

print("users who visited but did not add to cart: {:.2f}%".format(p_no_cart))
print("users who added to cart but did not checkout: {:.2f}%".format(p_no_check))
print("users who proceeded to checkout but did not purchase: {:.2f}%".format(p_no_buy))

# Determine the weakest step
weakest_step_percentage = max(p_no_cart, p_no_check, p_no_buy)
if weakest_step_percentage == p_no_cart:
    weakest_step = "visiting the site to adding items to the cart"
elif weakest_step_percentage == p_no_check:
    weakest_step = "adding items to the cart to proceeding to checkout"
else:
    weakest_step = "proceeding to checkout to making a purchase"

print("\nThe weakest step in the funnel is: {} with a dropout percentage of {:.2f}%".format(weakest_step, weakest_step_percentage))

# Average Time to Purchase

'''[10]
Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase. Add a column that is the difference between purchase_time and visit_time.
'''
print('\nEX 10 ----------------\n')

all_data['time_to_purchase'] = (all_data.purchase_time - all_data.visit_time)
avg_time_table = all_data[['visit_time','time_to_purchase','purchase_time']]
#print(avg_time_table)

'''[11]
Examine the results by printing the new column to the screen.
'''
print('\nEX 11 ----------------\n')

print(avg_time_table)


'''[12]
Calculate the average time to purchase by applying the .mean() function to your new column.
'''
print('\nEX 12 ----------------\n')

avg_time = all_data.time_to_purchase.mean()
print("Average time from initial visit to final purchase: ", avg_time)