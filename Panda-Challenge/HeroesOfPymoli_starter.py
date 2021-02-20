#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[6]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[9]:


# Find unique players to calculate the total number of players
unique_names = purchase_data["SN"].unique()
unique_names
# Find total number of players
total = len(unique_names)

# Create a data frame to display total number of players
total_players = pd.DataFrame({"Total Players": [total]})
total_players


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[18]:


# Find number of unique items
unique_items  = purchase_data["Item ID"].unique()
unique = len(unique_items)

# Find average price
avg_price = purchase_data["Price"].mean()

# Find number of purchases
num_purchases = purchase_data["Item Name"].count()

# Find total revenue
revenue = purchase_data["Price"].sum()

# Create a summary table to display results
purchasing_analysis = pd.DataFrame({"Number of Unique Items": [unique],
                                   "Average Price": avg_price,
                                   "Number of Purchases": num_purchases,
                                    "Total Revenue": revenue})

# Format the table for average price and revenue values
purchasing_analysis["Average Price"] = purchasing_analysis["Average Price"].map("${:.2f}".format)
purchasing_analysis["Total Revenue"] = purchasing_analysis["Total Revenue"].map("${:.2f}".format)

purchasing_analysis


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[27]:


# Group purchase data by gender to find count of each gender
gender_df = purchase_data.groupby(["Gender"])

# Find number of unique names grouped by gender
gender_count = gender_df["SN"].nunique()

# Find percentages for each gender
percentage = gender_count / total *100

# Create a new data frame to display results
gender_demographics = pd.DataFrame({"Total Count": gender_count,
                                    "Percentage of Players": percentage})
# Reset index value to none
gender_summary = gender_demographics.rename_axis([""])

# Sort total count values 
gender_summary = gender_summary.sort_values("Total Count", ascending = False)

# Format percentage values
gender_summary["Percentage of Players"] = gender_summary["Percentage of Players"].map("{:.2f}%".format)
gender_summary


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[35]:


# Find purchase count for each gender
purchase_count = gender_df["Purchase ID"].count()

# Find average count by each group
avg_purchase = gender_df["Price"].mean()

# Find total purchase value for each gender
total_purchase = gender_df["Price"].sum()

# Find average purchase total per person by gender; by dividing each genders total purchases to unique gender count
avg_purchase_total = total_purchase / gender_count
avg_purchase_total

# Create a data frame to display results from the calculations
purchasing_df = pd.DataFrame({"Purchase Counts": purchase_count,
                             "Average Purchase Price": avg_purchase,
                             "Total Purchase Value": total_purchase,
                             "Average Total Purchase per Person": avg_purchase_total})

# Format average purchase price, total purchase values and average total purchase values
purchasing_df["Average Purchase Price"]= purchasing_df["Average Purchase Price"].map("${:.2f}".format)
purchasing_df["Average Total Purchase per Person"]= purchasing_df["Average Total Purchase per Person"].map("${:.2f}".format)
purchasing_df["Total Purchase Value"]= purchasing_df["Total Purchase Value"].map("${:.2f}".format)
purchasing_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[46]:


# Create bins and labels
# to get the idea for the bins' values, get min and max age values to assign bins
max_age = purchase_data["Age"].max()
min_age = purchase_data["Age"].min()

# Create bins and label lists acording to min age 7 and max age 45 to hold age data accordingly
bins = [5, 9.9, 14.9, 19.9 , 24.9, 29.9, 34.9, 39.9, 99]
label_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# Create a new column age range, for ages and put it in the original data frame
purchase_data["Age Ranges"] = pd.cut(purchase_data["Age"], bins, labels = label_names)

# Group data frame by age ranges to set it as index value, and calculate age count for each age range
age_df = purchase_data.groupby(["Age Ranges"])

# Calculate age count for unique name values for age labels 
age_count = age_df["SN"].nunique()

# Calculate percentages for each age labels
age_percentage = age_count / total *100

# Create a data frame to display results in a tabular format
age_demographic_df = pd.DataFrame({"Total Count": age_count,
                           "Percentage of Players": age_percentage})

# Format percentage values and change index name as none
age_demographic_df = age_demographic_df.rename_axis([""])
age_demographic_df["Percentage of Players"] = age_demographic_df["Percentage of Players"].map("{:.2f}%".format)
age_demographic_df


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[53]:


# Get the top five spenders by total purchase value
# Find purchase count for each age range
purchase_count = age_df["Purchase ID"].count()

# Find average purchse price for each age range
avg_purchase = age_df["Price"].mean()

# Find total purchase value for each age range
total_value = age_df["Price"].sum()

# Find average purchase total per person by dividing total value by unique age count
avg_total = total_value / age_count

# Create a summary table for results
age_purchasing_df = pd.DataFrame ({"Purchase Count": purchase_count,
                                  "Average Purchase Price": avg_purchase,
                                  "Total Purchase Value": total_value,
                                  "Average Purchase Total per Person": avg_total})

# Format Average price, total purchase and average purchase values
age_purchasing_df["Average Purchase Price"] = age_purchasing_df["Average Purchase Price"].map("${:.2f}".format)
age_purchasing_df["Total Purchase Value"] = age_purchasing_df["Total Purchase Value"].map("${:.2f}".format)
age_purchasing_df["Average Purchase Total per Person"] = age_purchasing_df["Average Purchase Total per Person"].map("${:.2f}".format)

age_purchasing_df


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[62]:


# Identify top spenders by total purchase value
# Group data frame by names 
spenders_df = purchase_data.groupby(["SN"])

# Calculate total purchases  for each spenders name
spenders_purchase = spenders_df["Price"].sum()

# Calculate number of purchase count for each spender
sep_purchase_count = spenders_df["Purchase ID"].count()

# Calculate average purchase for each spender
avg_purchase_price = spenders_df["Price"].mean()

# Create a data frame to display results
spenders_data = pd.DataFrame({"Purchase Count": sep_purchase_count,
                             "Average Purchase Price": avg_purchase_price,
                             "Total Purchase Value": spenders_purchase})

# Sort the data frame to get top five spenders
top_spenders = spenders_data.sort_values(["Total Purchase Value"], ascending = False)

# Format the values 
top_spenders["Average Purchase Price"] = top_spenders["Average Purchase Price"].map("${:.2f}".format) 
top_spenders["Total Purchase Value"] = top_spenders["Total Purchase Value"].map("${:.2f}".format) 

# Display the results
top_spenders.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[71]:


# Identify the 5 most popular items by purchase count, then list (in a table):

# Group the data frame by item id and item name    
popular_items = purchase_data.groupby(["Item ID","Item Name"])

# Calculate purchase count for each purchase id
purchase_count = popular_items["Purchase ID"].count()

# Calculate total price for each group values
total_value = popular_items["Price"].sum()

# Calculate item price by dividing total to count of purchase 
item_price = total_value / purchase_count


# Create a data frame to display data
top_items = pd.DataFrame({"Purchase Count": purchase_count,
                         "Item Price": item_price,
                         "Total Purchase Value": total_value})

# Sort the data to get top five popular items
popular_df = top_items.sort_values(["Purchase Count"], ascending = False)

# Format the values
popular_df["Item Price"] = popular_df["Item Price"].map("${:.2f}".format)
popular_df["Total Purchase Value"] = popular_df["Total Purchase Value"].map("${:.2f}".format)
                                                          
popular_df.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[73]:


# Sort the data frame by total purchase value 
profitable_items = top_items.sort_values(["Total Purchase Value"], ascending = False)

# Display the new data frame
profitable_items.head()


# In[ ]:


Most of the players are male
Final critic is the most profitable item
Highest percentage of players are between 20-24

