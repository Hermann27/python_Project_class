#!/usr/bin/env python3
import sqlite3
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import legal
from datetime import datetime  # Import the datetime module

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Specify the columns you want to retrieve
selected_columns = ["name", "Departments", "Location_Area", "Description", "Recommendation_step","situation"] 

# Construct the SQL query with the selected columns
# We can use the JOIN statement to select data from multiple tables if needed

# Retrieve data based on a field condition
cursor.execute(f"SELECT {', '.join(selected_columns)} FROM myapp_incident WHERE Type_of_near_miss = ?",
               ('Safety Concern',))  # Replace with your condition

# Fetch the data
data = cursor.fetchall()

# Close the database connection
conn.close()

# Get the current date and time
current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
current_directory = os.getcwd()
# Define the directory where you want to save the report
save_directory =f"{current_directory}/Safety_Report/"  # Replace with your desired directory

# Create the full file path including the directory and the date in the file name
pdf_file_path = f"{save_directory}Safety_report_{current_date}.pdf"

# Create a PDF document
doc = SimpleDocTemplate(pdf_file_path, pagesize=legal)
elements = []

# Define styles for the cover page
styles = getSampleStyleSheet()
title_style = styles["Title"]
normal_style = styles["Normal"]
date_report= datetime.now().strftime("%m-%d-%Y Generted at : %H:%M:%S")
# Add a cover page
elements.append(Paragraph("WEEKLY SAFETY REPORT CONCERN ONLY", title_style))
elements.append(Spacer(1, 12))
elements.append(Paragraph("Author: Hermann", normal_style))
elements.append(Spacer(1, 12))
elements.append(Paragraph(f"Date: {date_report}", normal_style))
elements.append(Spacer(1, 36))  # Space between cover page and table

# Define the style for the table
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), (0, 0.7, 0)),  # Header row background color (Green)
    ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),  # Header row text color (White)
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center alignment for all cells
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Font name
    ('FONTSIZE', (0, 0), (-1, -1), 12),  # Font size
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header row padding
    ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),  # Data row background color
    ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Add cell borders
])

# Create a new list to store modified data
modified_data = [["Report by ", "Departments", "Location Area", "Description", "Recommendation Step","Inspection"]] 

# Handle text overflow by allowing text to wrap and storing it in the modified_data list
for row in data:
    modified_row = []
    for cell in row:
        modified_row.append(Paragraph(cell, style=getSampleStyleSheet()['Normal']))
    modified_data.append(modified_row)

table = Table(modified_data)
table.setStyle(style)
# Add the table to the PDF document
elements.append(table)

# Build the PDF document
doc.build(elements)