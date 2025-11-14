import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    "Category": ['Electrinocis', 'clothing', 'Groceries', 'Toys', 'Furniture'],
    "Revenue": [55000, 32000, 21000, 15000, 40000],
    "Profit": [12000, 7000, 5000, 2000, 9000],
    "Quantity": [120, 230, 300, 150, 100],
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.plot(df['Category'], df['Revenue'], marker='o')          # optional line
sns.barplot(x='Category', y='Revenue', data=df)             # bar plot
plt.title('Seaborn bar plot - Revenue by Category')
plt.tight_layout()
plt.show()   # <--- call the function, don't print it




#  Histogram 
plt.figure(figsize = (6,4))
plt.hist(data["Profit"] , bins =10, color = "orange")
plt.title("Histogram")
plt.xlabel("Revenue")
plt.ylabel(plt.show())


# seaborn version

sns.boxplot(x ='Revenue' , data = data)
plt.title("seaborn box plot - Revenue Distribution")
plt.tight_layout()
print(plt.show())