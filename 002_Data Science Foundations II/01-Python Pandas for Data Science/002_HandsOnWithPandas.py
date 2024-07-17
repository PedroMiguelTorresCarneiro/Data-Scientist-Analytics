# ----------------------------------------------------------------------
'''
	You run an online clothing store called Panda’s Wardrobe. 
	You need a DataFrame containing information about your products.

	Create a DataFrame with the following data 
	that your inventory manager sent you:

	Product ID	Product Name	Color
	1			t-shirt			blue
	2			t-shirt			green
	3			skirt			red
	4			skirt			black

	We have already filled in the 
	information for Product ID in df1.

	Add the code to create the columns 
	Product Name and Color and 
	their associated data.
'''

import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
  # add Product Name and Color here
})

print(df1)

# ----------------------------------------------------------------------
'''
	You’re running a chain of pita shops called Pita Power. 
	You want to create a DataFrame with information on 
	your different store locations.

	Use a list of lists to create a 
	DataFrame with the following data:

	Store ID	Location	Number of Employees
	1			San Diego			100
	2			Los Angeles			120
	3			San Francisco		90
	4			Sacramento			115

	We have filled in the information for the 
	first two rows in df2.

	Add the code to create the 3rd and 4th rows, 
	and the column names.
'''

import pandas as pd

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115],
  # Fill in rows 3 and 4
],
  columns=[
    'Store ID',
    'Location',
    'Number of Employees'
  ])

print(df2)

# ----------------------------------------------------------------------
'''
	You’re working for the County of Whoville and you just 
	received a CSV of data about the different cities in your 
	county. Read the CSV 'sample.csv' into a variable called df, 
	so that you can learn more about the cities.

	Let’s inspect the CSV.
	Type print(df) on the next line and then run your code. 
	What sort of data were you sent?
'''

import codecademylib3
import pandas as pd

df = pd.read_csv('sample.csv')

print(df)


# ----------------------------------------------------------------------
'''
	You’re working for a Hollywood studio, trying to use 
	data to predict the next big hit. Load the CSV 
	imdb.csv into a variable called df, so that you 
	can learn about popular movies from the past 90 years.

	> Let’s learn about these movies.
	Paste the following code into script.py:

	> What exactly is in this dataset?
	Paste the following code into script.py to learn more about this data:
'''

import codecademylib3
import pandas as pd
#load the CSV below:

df = pd.read_csv('imdb.csv')

print(df.head())
	'''
	   id                                       name   genre  year  imdb_rating
	0   1                                     Avatar  action  2009          7.9
	1   2                             Jurassic World  action  2015          7.3
	2   3                               The Avengers  action  2012          8.1
	3   4                            The Dark Knight  action  2008          9.0
	4   5  Star Wars: Episode I - The Phantom Menace  action  1999          6.6
	'''
print(df.info())
	'''
	<class 'pandas.core.frame.DataFrame'>
	RangeIndex: 220 entries, 0 to 219
	Data columns (total 5 columns):
	id             220 non-null int64
	name           220 non-null object
	genre          220 non-null object
	year           220 non-null int64
	imdb_rating    220 non-null float64
	dtypes: float64(1), int64(2), object(2)
	memory usage: 8.7+ KB
	None
	'''

# ----------------------------------------------------------------------
'''
	The DataFrame df represents data collected by four 
	health clinics run by the same organization. Each row 
	represents a month from January through June and shows 
	the number of appointments made at four different clinics.

	You want to analyze what’s been happening at the 
	North location. Create a variable called clinic_north 
	that contains ONLY the data from the column clinic_north.

	> What exactly have you selected?
		After you create the variable, enter the command:
			- print(type(clinic_north))
		to see what data type you’ve created.

	> How is this different from what you get if you type the following?
		- print(type(df))
'''

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df.clinic_north

print(type(clinic_north))
	'''
	<class 'pandas.core.series.Series'>
	'''

print(type(df))
	'''
	<class 'pandas.core.frame.DataFrame'>
	'''

# ----------------------------------------------------------------------
'''
	Now, you want to compare visits to the Northern and 
	Southern clinics.
	Create a variable called clinic_north_south that 
	contains ONLY the data from the columns 
	clinic_north and clinic_south.

	> When we select multiple columns, do we get a Series 
	or a DataFrame?
		After you’ve created the variable, enter the command:
			- print(type(clinic_north_south))
		to see what data type you’ve created.

	> How is this different from what happened in the 
	previous exercise?
'''

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north_south = df[['clinic_north','clinic_south']]

print(type(clinic_north_south))
	'''
	<class 'pandas.core.frame.DataFrame'>
	'''

# ----------------------------------------------------------------------
'''
	You’re getting ready to staff the clinic for March this 
	year. You want to know how many visits took place in 
	March last year, to help you prepare.

	Write a command that will produce a Series made up 
	of the March data from df from all four clinic sites and 
	save it to the variable march.

'''

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

march = df.iloc[2]
	'''
	month           March
	clinic_east        81
	clinic_north       96
	clinic_south       65
	clinic_west        96
	Name: 2, dtype: object
	'''

# ----------------------------------------------------------------------
'''
	One of your doctors thinks that there are more clinic 
	visits in the late Spring.
	Write a command that will produce a DataFrame made 
	up of the data for April, May, and June from df for all 
	four sites (rows 3 through 6), and save it to april_may_june.

	Inspect april_may_june using print.
'''

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

april_may_june = df.iloc[3:6]

print(april_may_june)
	'''
		month	clinic_east	clinic_north	clinic_south	clinic_west
	3	April	80	80	54	180
	4	May	51	54	54	154
	5	June	112	109	79	129
	'''

# ----------------------------------------------------------------------
'''
	You’re going to staff the clinic for January of this year. 
	You want to know how many visits took place in 
	January of last year, to help you prepare.
	Create variable january using a logical statement 
	that selects the row of df where the 'month' 
	column is 'January'.

	Inspect january using print.
'''

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

january = df[df.month == 'January']

print(january)
	'''
		month	clinic_east	clinic_north	clinic_south	clinic_west
	0	January	100	100	23	100
	'''

# ----------------------------------------------------------------------
'''
	You want to see how the number of clinic visits 
	changed between March and April.
	Create the variable march_april, which contains the 
	data from March and April. Do this using two logical 
	statements combined using |, which means “or”.

	Inspect march_april using print.
'''

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

march_april = df[ (df.month == 'March')| (df.month == 'April')]

print(march_april)
	'''
		month	clinic_east	clinic_north	clinic_south	clinic_west
	2	March	81	96	65	96
	3	April	80	80	54	180
	'''


# ----------------------------------------------------------------------
'''
	Another doctor thinks that you have a lot of clinic 
	visits in the late Winter.
	Create the variable january_february_march, containing the 
	data from January, February, and March. Do this 
	using a single logical statement with the isin command.

	Inspect january_february_march using print.
'''

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])
    
january_february_march = df[df.month.isin(['January','February', 'March'])]

print(january_february_march)
	'''
		month	clinic_east	clinic_north	clinic_south	clinic_west
	0	January	100	100	23	100
	1	February	51	45	145	45
	2	March	81	96	65	96
	'''


# ----------------------------------------------------------------------
'''
	Examine the code in the workspace. Note that df2 
	is a subset of rows from df.
	Type the following and press “Run”:
		- print(df2)

	Note that the indices on df2 are not consecutive.
	Create a new DataFrame called df3 by resetting 
	the indices on df2 (don’t use inplace or drop). 
	Did df2 change after you ran this command?

	Reset the indices of df2 by using the keyword 
	inplace=True and drop=True. Did the indices 
	of df2 change? How is df2 different from df3?
'''

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

df2 = df.loc[[1, 3, 5]]

print(df2)
	'''
		month	clinic_east	clinic_north	clinic_south	clinic_west
	1	February	51	45	145	45
	3	April	80	80	54	180
	5	June	112	109	79	129
	'''

df3 = df2.reset_index(inplace=True, drop=True)

print('---------\n')
print(df2)
	'''
		month	clinic_east	clinic_north	clinic_south	clinic_west
	0	February	51	45	145	45
	1	April	80	80	54	180
	2	June	112	109	79	129
	'''

# ----------------------------------------------------------------------
'''
	FINAL

	In this example, you’ll be the data analyst for ShoeFly.com, 
	a fictional online shoe store. You’ve seen this data; 
	now it’s your turn to work with it!

	Load the data from shoefly.csv into the variable orders.

	Inspect the first 5 lines of the data.

	Your marketing department wants to send out an 
	email blast to everyone who ordered shoes!
		Select all of the email addresses from the column 
		email and save them to a variable called emails.


	Frances Palmer claims that her order was wrong. 
	What did Frances Palmer order?
		Use logic to select that row of orders 
		and save it to the variable frances_palmer.

	We need some customer reviews for our comfortable shoes. 
		Select all orders for shoe_type: 
		clogs, boots, and ballet flats 
		and save them to the variable comfy_shoes.
'''

import codecademylib3
import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head())
	'''
		id	first_name	last_name	email	shoe_type	shoe_material	shoe_color
	0	54791	Rebecca	Lindsay	RebeccaLindsay57@hotmail.com	clogs	faux-leather	black
	1	53450	Emily	Joyce	EmilyJoyce25@gmail.com	ballet flats	faux-leather	navy
	2	91987	Joyce	Waller	Joyce.Waller@gmail.com	sandals	fabric	black
	3	14437	Justin	Erickson	Justin.Erickson@outlook.com	clogs	faux-leather	red
	4	79357	Andrew	Banks	AB4318@gmail.com	boots	
	'''

emails = orders.email
print(emails)
	'''
		email
	0	RebeccaLindsay57@hotmail.com
	1	EmilyJoyce25@gmail.com
	2	Joyce.Waller@gmail.com
	3	Justin.Erickson@outlook.com
	4	AB4318@gmail.com
	5	JulieMarsh59@gmail.com
	6	TJ5470@gmail.com
	7	Janice.Hicks@gmail.com
	8	GabrielPorter24@gmail.com
	9	FrancesPalmer50@gmail.com
	10	JessicaHale25@gmail.com
	11	LawrenceParker44@gmail.com
	12	SusanDennis58@gmail.com
	13	DO2680@gmail.com
	14	Rebecca.Charles@gmail.com
	15	JC2072@hotmail.com
	16	VS4753@outlook.com
	17	RoyTillman20@gmail.com
	18	Thomas.Roberson@gmail.com
	19	ANewton1977@outlook.com
	'''

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]
print(frances_palmer)
	'''
		id	first_name	last_name	email	shoe_type	shoe_material	shoe_color
	9	62083	Frances	Palmer	FrancesPalmer50@gmail.com	wedges	leather	white
	'''

comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots','ballet flats'])]
print(comfy_shoes)
	'''
		id	first_name	last_name	email	shoe_type	shoe_material	shoe_color
	0	54791	Rebecca	Lindsay	RebeccaLindsay57@hotmail.com	clogs	faux-leather	black
	1	53450	Emily	Joyce	EmilyJoyce25@gmail.com	ballet flats	faux-leather	navy
	3	14437	Justin	Erickson	Justin.Erickson@outlook.com	clogs	faux-leather	red
	4	79357	Andrew	Banks	AB4318@gmail.com	boots	leather	brown
	6	20487	Thomas	Jensen	TJ5470@gmail.com	clogs	fabric	navy
	7	76971	Janice	Hicks	Janice.Hicks@gmail.com	clogs	faux-leather	navy
	8	21586	Gabriel	Porter	GabrielPorter24@gmail.com	clogs	leather	brown
	10	91629	Jessica	Hale	JessicaHale25@gmail.com	clogs	leather	red
	12	45832	Susan	Dennis	SusanDennis58@gmail.com	ballet flats	fabric	white
	14	73431	Rebecca	Charles	Rebecca.Charles@gmail.com	boots	faux-leather	white
	16	39888	Vincent	Stephenson	VS4753@outlook.com	boots	leather	black
	17	35961	Roy	Tillman	RoyTillman20@gmail.com	boots	leather	white
	'''
