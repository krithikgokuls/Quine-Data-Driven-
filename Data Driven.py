# Python code using Taipy to create a simple data-driven web application

from taipy import App, Page, Chart
import pandas as pd

# Load dataset
data = pd.read_csv('dataset.csv')

# Define application
app = App()

# Define page
page = Page()

# Add chart to page
chart = Chart(data, type='line', x='Date', y='Value')
page.add_chart(chart)

# Add page to app
app.add_page(page)

# Run application
app.run()
