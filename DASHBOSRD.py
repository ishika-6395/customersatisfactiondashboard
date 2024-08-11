import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Connect to MySQL database
conn = mysql.connector.connect(
 host='localhost',
 user='root',
 password='root',
 database='customer_satisfaction'
)
# Fetch data from MySQL
query = """
SELECT c.name, r.question, r.rating
FROM Customers c
JOIN Surveys s ON c.customer_id = s.customer_id
JOIN Responses r ON s.survey_id = r.survey_id
"""
df = pd.read_sql(query, conn)
# Close the connection
conn.close()
# Data visualization
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='question', hue='rating')
plt.title('Customer Satisfaction Survey Results')
plt.xlabel('Question')
plt.ylabel('Count')
plt.legend(title='Rating')
plt.show()
