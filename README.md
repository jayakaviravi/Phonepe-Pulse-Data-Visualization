# Phonepe-Pulse-Data-Visualization
### Introduction

PhonePe is a popular digital payments and financial services platform in India. It enables users to make seamless transactions using their smartphones, including payments, money transfers, bill payments, and online shopping. With its user-friendly interface and wide acceptance, PhonePe has become a convenient and widely used platform for digital transactions in India.

 **Skills take away From This Project**

 1. Github Cloning
 2. Python
 3. Pandas
 4. MySQL
 5. mysql-connector-python,
 6. Streamlit
 7. Plotly

 **Domain**
 - Fintech
 ### Problem statement

 The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics.
 The goal is to extract this data and process it to obtain insights and information that can be  visualized in a user-friendly manner.

The solution must include the following steps:
1. Extract data from the Phonepe pulse Github repository through scripting and clone it..
2. Transform the data into a suitable format and perform any necessary cleaning and pre-processing steps.
3. Insert the transformed data into a MySQL database for efficient storage and retrieval.
4. Create a live geo visualization dashboard using Streamlit and Plotly in Python to display the data in an interactive and visually appealing manner.
5. Fetch the data from the MySQL database to display in the dashboard.
6. Provide at least 10 different dropdown options for users to select different facts and figures to display on the dashboard.

The solution must be secure, efficient, and user-friendly. The dashboard must be easily accessible and provide valuable insights and information about the data in the Phonepe pulse Github repository.

###  Requirement Libraries to Install
-  pip install mysql-connector-python
-  pip streamlit
-  pip install streamlit-option-menu
-  pip install plotly_ express
-  pip install pandas
-  pip install os

### Approach

### Data Extraction:
Clone the Phonepe pulse Github repository using scripting. This can be done using Git commands or a Git library in a programming language like Python. Store the cloned repository in a local directory.

### Data Transformation:
Use a scripting language like Python and import libraries such as Pandas to manipulate and preprocess the data. Read the required files (e.g., CSV, JSON) from the cloned repository into a Pandas DataFrame. Perform data cleaning tasks such as handling missing values, removing duplicates, and correcting inconsistencies. Transform the data into a suitable format for analysis and visualization.

### Database Insertion:
Install the MySQL database server and create a new database to store the Phonepe pulse data. Use the "mysql-connector-python" library in Python to connect to the MySQL database. Create a table schema that matches the structure of the transformed data. Insert the transformed data into the MySQL database using SQL commands.

### Dashboard Creation:
Install Streamlit and Plotly libraries in Python. Use Streamlit to create a user-friendly interface for the dashboard. Utilize Plotly's geospatial mapping functions to display the data on a map. Design the dashboard with interactive features such as dropdown menus for users to select different facts and figures. Use appropriate Plotly charts and visualizations to present the insights derived from the data.

### Data Retrieval:
Use the "mysql-connector-python" library to connect to the MySQL database. Fetch the required data from the database into a Pandas DataFrame. Update the dashboard dynamically with the latest data by incorporating the retrieved data into the Streamlit and Plotly components.

### Deployment:
Ensure the solution is secure, efficient, and user-friendly. Test the solution thoroughly and deploy the dashboard publicly, making it accessible to users.

