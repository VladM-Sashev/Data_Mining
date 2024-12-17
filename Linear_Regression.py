 Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Loading  the dataset
file_path = r'C:\Users\Vladimir Merdzhanov\Desktop\Data_Mining\Cleaned_Dataset.xlsx'
df = pd.read_excel(file_path)

# Defining the predictor variables( Revenue and Cost) and the responce variable (Profit)
X = df[['Revenue(£)', 'Cost(£)']]
y = df['Profit(£)']

# Dividing the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction and evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Model coefficients
print(f'Coefficients: {model.coef_}')
print(f'Intercept: {model.intercept_}')

# Plotting
plt.figure(figsize=(12, 6))

# Comparing actual and predicted profits
plt.subplot(1, 2, 1)
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
plt.xlabel('Actual Profit(£)')
plt.ylabel('Predicted Profit(£)')
plt.title('Actual vs Predicted Profit')

# Residual plot
plt.subplot(1, 2, 2)
sns.residplot(x=y_test, y=y_pred, lowess=True, color="g")
plt.xlabel('Actual Profit(£)')
plt.ylabel('Residuals')
plt.title('Residual Plot')

plt.tight_layout()
plt.show()

# Histogram
residuals = y_test - y_pred
plt.figure(figsize=(6, 4))
sns.histplot(residuals, kde=True, color="blue")
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Histogram of Residuals')
plt.show()
