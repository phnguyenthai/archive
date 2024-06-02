#!/usr/bin/env python
# coding: utf-8

# In[9]:


#!pip install xlwings pillow pywin32


# In[11]:


import xlwings as xw
from PIL import ImageGrab
import os

# Define the file path
file_path = 'C:/Users/phong/OneDrive/Desktop/auto_email/auto_email.xlsx'
output_image_path = 'C:/Users/phong/OneDrive/Desktop/auto_email/copied_image.bmp'

# Open the workbook and select the sheet
app = xw.App(visible=False)
wb = xw.Book(file_path)
sheet = wb.sheets['Sheet1']

# Select the range and copy it as a picture
range_to_copy = sheet.range('A1:C10')
range_to_copy.api.CopyPicture(Format=2)  # Format=2 corresponds to Bitmap

# Get the picture from the clipboard and save it
img = ImageGrab.grabclipboard()
if img:
    img.save(output_image_path, 'BMP')
else:
    print("No image found in clipboard")

# Clean up
wb.close()
app.quit()


# In[14]:


##looping to find the condition.

import xlwings as xw
from PIL import ImageGrab
import os

# Define the file path
file_path = 'C:/Users/phong/OneDrive/Desktop/auto_email/auto_email.xlsx'
output_image_path = 'C:/Users/phong/OneDrive/Desktop/auto_email/copied_image.bmp'

# Open the workbook and select the sheet
app = xw.App(visible=False)
wb = xw.Book(file_path)
sheet = wb.sheets['Sheet1']

# Determine the dynamic range based on the condition
last_row = 1
for row in range(1, 101):
    cell_value = sheet.range(f'A{row}').value
    if cell_value is not None and cell_value != 0:
        last_row = row

range_to_copy = sheet.range(f'A1:C{last_row}')
range_to_copy.api.CopyPicture(Format=2)  # Format=2 corresponds to Bitmap

# Get the picture from the clipboard and save it
img = ImageGrab.grabclipboard()
if img:
    img.save(output_image_path, 'BMP')
    print(f"Image saved at {output_image_path}")
else:
    print("No image found in clipboard")

# Clean up
wb.close()
app.quit()


# In[13]:


import os
import win32com.client as win32

# Define the folder path
folder_path = 'C:/Users/phong/OneDrive/Desktop/auto_email'

# Get all BMP files in the folder
bmp_files = [f for f in os.listdir(folder_path) if f.endswith('.bmp')]

# Create an Outlook application instance
outlook = win32.Dispatch('outlook.application')

# Create a new mail item
mail = outlook.CreateItem(0)

# Define the recipient, subject, and body of the email
mail.To = 'phongnthai@gmail.com'
mail.Subject = 'Auto Email with BMP Attachments'
mail.Body = 'Please find the attached BMP images.'

# Attach all BMP files to the email
for bmp_file in bmp_files:
    attachment_path = os.path.join(folder_path, bmp_file)
    mail.Attachments.Add(attachment_path)

# Send the email
mail.Send()

print("Email sent successfully with BMP attachments.")


# In[15]:


import xlwings as xw

# Define the file path
file_path = 'C:/Users/phong/OneDrive/Desktop/auto_email/auto_email.xlsx'

# Open the workbook and bring it to the foreground
app = xw.App(visible=True)
wb = xw.Book(file_path)

# Bring the workbook to the foreground
app.activate(steal_focus=True)

# Refresh all data connections in the workbook
wb.api.RefreshAll()

# Optional: Save and close the workbook
# wb.save()
# wb.close()
# app.quit()


# In[8]:


### paste the content into the email body.

import os
import win32com.client as win32

# Define the folder path
folder_path = 'C:/Users/phong/OneDrive/Desktop/auto_email'

# Get all BMP files in the folder
bmp_files = [f for f in os.listdir(folder_path) if f.endswith('.bmp')]

# Create an Outlook application instance
outlook = win32.Dispatch('outlook.application')

# Create a new mail item
mail = outlook.CreateItem(0)

# Define the recipient, subject, and body of the email
mail.To = 'phongnthai@gmail.com'
mail.Subject = 'Auto Email with BMP Embedded Images'
mail.BodyFormat = 2  # Set the body format to HTML

# Construct the email body with HTML
body_html = '<html><body>'
for idx, bmp_file in enumerate(bmp_files):
    attachment_path = os.path.join(folder_path, bmp_file)
    # Attach the image and get the Content ID (CID)
    attachment = mail.Attachments.Add(attachment_path)
    cid = f'image{idx + 1}'
    attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001E", cid)
    # Embed the image using CID
    body_html += f'<p><img src="cid:{cid}" alt="{bmp_file}"></p>'
body_html += '</body></html>'

# Set the HTMLBody property of the mail item
mail.HTMLBody = body_html

# Send the email
mail.Send()

print("Email sent successfully with BMP embedded images.")


# In[12]:


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

