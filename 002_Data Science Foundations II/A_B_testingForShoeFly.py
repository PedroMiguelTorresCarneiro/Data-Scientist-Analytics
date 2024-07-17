import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

# Analyzing Ad Sources -----------------------------------------------------

''' [1] 
  Examine the first few rows
'''
print('\nEX 1 ----------------\n')
print(ad_clicks.head())

''' [2] 
Your manager wants to know which ad platform is getting you the most views.

How many views (i.e., rows of the table) came from each utm_source?
'''
print('\nEX 2 ----------------\n')
views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(views)

''' [3]
If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.

Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
'''
print('\nEX 3 ----------------\n')
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.apply(lambda x: False if pd.isnull(x) else True) 
# easy way : ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head())

''' [4]
We want to know the percent of people who clicked on ads from each utm_source.

Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups. Save your answer to the variable clicks_by_source.
'''
print('\nEX 4 ----------------\n')
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)

''' [5]
Now lets pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.

Save your results to the variable clicks_pivot.
'''
print('\nEX 5 ----------------\n')
clicks_pivot = clicks_by_source.pivot(
    index='utm_source',
    columns='is_click',
    values='user_id'
).reset_index()

print(clicks_pivot)

''' [6]
Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.

Was there a difference in click rates for each source?
'''
print('\nEX 6 ----------------\n')

clicks_pivot['percent_clicked'] = (clicks_pivot[True]/ (clicks_pivot[True]+clicks_pivot[False]))

print(clicks_pivot)

# Analyzing an A/B Test -----------------------------------------------------

''' [7]
The column experimental_group tells us whether the user was shown Ad A or Ad B.

Were approximately the same number of people shown both ads?
'''
print('\nEX 7 ----------------\n')
ex7 = ad_clicks.groupby(['experimental_group']).count()

print(ex7)

''' [8]
Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.
'''
print('\nEX 8 ----------------\n')

ex8 = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()

print(ex8)

ex8_1 = ex8.pivot(
  index='experimental_group',
  columns='is_click',
  values='user_id',
).reset_index()

ex8_1['percent_clicked'] = (ex8_1[True]/(ex8_1[True]+ex8_1[False]))

print(ex8_1)

''' [9]
The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.

Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.
'''
print('\nEX 9 ----------------\n')
a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']

b_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'B']

print("Ad A Clicks")
print(a_clicks)
print('\nAd B Clicks')
print(b_clicks)

''' [10]
For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.
'''
print('\nEX 10 ----------------\n')
ex10_a = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()

ex10_a_pivot = ex10_a.pivot(
  index='day',
  columns='is_click',
  values='user_id'
).reset_index()

ex10_a_pivot['percent_clicked'] = (ex10_a_pivot[True]/(ex10_a_pivot[True]+ex10_a_pivot[False]))

ex10_b = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()

ex10_b_pivot = ex10_b.pivot(
  index='day',
  columns='is_click',
  values='user_id'
).reset_index()

ex10_b_pivot['percent_clicked'] = (ex10_b_pivot[True]/(ex10_b_pivot[True]+ex10_b_pivot[False]))

print("Ad A Clicks per day")
print(ex10_a_pivot)
print('\nAd B Clicks per day')
print(ex10_b_pivot)

''' [11]
Compare the results for A and B. What happened over the course of the week?

Do you recommend that your company use Ad A or Ad B?
'''
print('\nEX 11 ----------------\n')

comparison_a_b = ex10_a_pivot[['day', 'percent_clicked']].merge(
    ex10_b_pivot[['day', 'percent_clicked']],
    on='day',
    suffixes=(': A', ': B')
)
print(comparison_a_b)