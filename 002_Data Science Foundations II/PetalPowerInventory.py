Petal Power Inventory

'''
You’re the lead data analyst for a chain of gardening stores called Petal Power. Help them analyze their inventory!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

> Answer Customer Emails

1.
	Data for all of the locations of Petal Power is in the file inventory.csv. Load the data into a DataFrame called inventory.
2.
	Inspect the first 10 rows of inventory.
3.
	The first 10 rows represent data from your Staten Island location. Select these rows and save them to staten_island.
4.
	A customer just emailed you asking what products are sold at your Staten Island location. Select the column product_description from staten_island and save it to the variable product_request.
5.
	Another customer emails to ask what types of seeds are sold at the Brooklyn location.
	Select all rows where location is equal to Brooklyn and product_type is equal to seeds and save them to the variable seed_request.


>Inventory

6.
	Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.
7.
	Petal Power wants to know how valuable their current inventory is.
	Create a column called total_value that is equal to price multiplied by quantity.
8.
	The Marketing department wants a complete description of each product for their catalog.
	The following lambda function combines product_type and product_description into a single string:

		combine_lambda = lambda row: \
		    '{} - {}'.format(row.product_type,
		                     row.product_description)

		Paste this function into script.py.
9.
	Using combine_lambda, create a new column in inventory called full_description that has the complete description of each product.
'''

import codecademylib3
import pandas as pd

inventory = pd.read_csv('inventory.csv')

print(inventory.head(10))
	'''
		location	product_type	product_description	quantity	price
	0	Staten Island	seeds	daisy	4	6.99
	1	Staten Island	seeds	calla lily	46	19.99
	2	Staten Island	seeds	tomato	85	13.99
	3	Staten Island	garden tools	rake	4	13.99
	4	Staten Island	garden tools	wheelbarrow	0	89.99
	5	Staten Island	garden tools	spade	93	19.99
	6	Staten Island	pest_control	insect killer	74	12.99
	7	Staten Island	pest_control	weed killer	8	23.99
	8	Staten Island	planter	20 inch terracotta planter	0	17.99
	9	Staten Island	planter	8 inch plastic planter	53	3.99
	'''

staten_island = inventory.head(10)
print(staten_island)
	'''
		location	product_type	product_description	quantity	price
	0	Staten Island	seeds	daisy	4	6.99
	1	Staten Island	seeds	calla lily	46	19.99
	2	Staten Island	seeds	tomato	85	13.99
	3	Staten Island	garden tools	rake	4	13.99
	4	Staten Island	garden tools	wheelbarrow	0	89.99
	'''

product_request = staten_island.product_description
print(product_request)
	'''
		product_description
	0	daisy
	1	calla lily
	2	tomato
	3	rake
	4	wheelbarrow
	5	spade
	6	insect killer
	7	weed killer
	8	20 inch terracotta planter
	9	8 inch plastic planter
	'''

seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)
	'''
		location	product_type	product_description	quantity	price
	10	Brooklyn	seeds	daisy	50	6.99
	11	Brooklyn	seeds	calla lily	0	19.99
	12	Brooklyn	seeds	tomato	0	13.99
	'''

inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)
print(inventory[[ 'quantity', 'in_stock']])
	'''
		quantity	in_stock
	0	4	True
	1	46	True
	2	85	True
	3	4	True
	4	0	False
	5	93	True
	6	74	True
	7	8	True
	8	0	False
	9	53	True
	10	50	True
	11	0	False
	12	0	False
	13	15	True
	14	82	True
	15	36	True
	16	80	True
	17	76	True
	18	5	True
	19	26	True
	20	57	True
	21	95	True
	22	45	True
	23	21	True
	24	98	True
	25	26	True
	26	0	False
	27	16	True
	28	87	True
	'''

inventory['total_value'] = inventory.price * inventory.quantity
print(inventory[[ 'price', 'quantity', 'total_value']])
	'''
		price	quantity	total_value
	0	6.99	4.0	27.96
	1	19.99	46.0	919.54
	2	13.99	85.0	1189.15
	3	13.99	4.0	55.96
	4	89.99	0.0	0.0
	5	19.99	93.0	1859.07
	6	12.99	74.0	961.26
	7	23.99	8.0	191.92
	8	17.99	0.0	0.0
	9	3.99	53.0	211.47
	10	6.99	50.0	349.5
	11	19.99	0.0	0.0
	12	13.99	0.0	0.0
	13	13.99	15.0	209.85
	14	89.99	82.0	7379.179999999999
	15	19.99	36.0	719.64
	16	12.99	80.0	1039.2
	17	23.99	76.0	1823.2399999999998
	18	17.99	5.0	89.94999999999999
	19	3.99	26.0	103.74000000000001
	20	6.99	57.0	398.43
	21	19.99	95.0	1899.05
	22	13.99	45.0	629.55
	23	13.99	21.0	293.79
	24	89.99	98.0	8819.019999999999
	25	19.99	26.0	519.74
	26	12.99	0.0	0.0
	27	23.99	16.0	383.84
	28	17.99	87.0	1565.1299999999999
	'''

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full description'] = inventory.apply(combine_lambda, axis=1)
print(inventory.head(5))
	'''
		location	product_type	product_description	quantity	price	in_stock	total_value	full description
	0	Staten Island	seeds	daisy	4	6.99	True	27.96	seeds - daisy
	1	Staten Island	seeds	calla lily	46	19.99	True	919.54	seeds - calla lily
	2	Staten Island	seeds	tomato	85	13.99	True	1189.15	seeds - tomato
	3	Staten Island	garden tools	rake	4	13.99	True	55.96	garden tools - rake
	4	Staten Island	garden tools	wheelbarrow	0	89.99	False	0.0	garden tools - wheelbarrow
	'''
	