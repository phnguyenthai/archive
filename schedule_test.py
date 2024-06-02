#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import win32com.client as win32

# Load the Excel file
file_path = 'C:/Users/phong/OneDrive/Desktop/auto_email/auto_email.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1', usecols=[0, 1, 2], nrows=50)

# Filter out rows where the first column (index 0) is null or 0
filtered_df = df[(df.iloc[:, 0].notnull()) & (df.iloc[:, 0] != 0)]

# Convert the filtered DataFrame to an HTML table
html_table = filtered_df.to_html(index=False)

# Create the email
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'phongnthai@gmail.com'
mail.Subject = 'Filtered Data from Excel'
mail.HTMLBody = f'<html><body>{html_table}</body></html>'

# Send the email
mail.Send()

print("Email sent successfully!")

