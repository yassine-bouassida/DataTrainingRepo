# Pandas Study Guide

## Table of Contents

1. [Introduction to Pandas](#introduction-to-pandas)
2. [Data Structures](#data-structures)
3. [Data Input/Output](#data-inputoutput)
4. [Data Selection and Indexing](#data-selection-and-indexing)
5. [Data Cleaning](#data-cleaning)
6. [Data Analysis](#data-analysis)
7. [Data Aggregation](#data-aggregation)
8. [Combining DataFrames](#combining-dataframes)
9. [Data Visualization with Matplotlib](#data-visualization-with-matplotlib)

---

## Introduction to Pandas

Pandas is a powerful Python library for data manipulation and analysis. It provides data structures and functions needed to work with structured data.

### Importing Pandas

```python
import pandas as pd
import numpy as np  # Often used together with pandas
```

---

## Data Structures

### Series

One-dimensional labeled array

```python
# Creating a Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Series operations
s.values    # Get values as numpy array
s.index     # Get index
s.describe() # Summary statistics
```

### DataFrame

Two-dimensional labeled data structure (like a spreadsheet or SQL table)

```python
# Creating DataFrames
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
})

# From lists
data = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

# Basic attributes
df.shape     # (rows, columns)
df.columns   # Column names
df.index     # Row indices
df.dtypes    # Data types of each column
df.info()    # Concise summary
df.head(n)   # First n rows
df.tail(n)   # Last n rows
```

---

## Data Input/Output

### Reading Data

```python
# CSV files
df = pd.read_csv('filename.csv')

# Excel files
df = pd.read_excel('filename.xlsx', sheet_name='Sheet1')

# From URLs
df = pd.read_csv('https://url.com/data.csv')

# Other formats
pd.read_json()    # JSON
pd.read_sql()     # SQL databases
pd.read_html()    # HTML tables
```

### Writing Data

```python
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
df.to_json('output.json')
```

---

## Data Selection and Indexing

### Column Selection

```python
# Single column (returns Series)
df['column_name']
df.column_name    # Not recommended if column names have spaces

# Multiple columns (returns DataFrame)
df[['col1', 'col2']]
```

### Row Selection

```python
# By index position
df.iloc[0]        # First row
df.iloc[0:5]      # Rows 0-4
df.iloc[[0, 2, 4]] # Specific rows

# By index label
df.loc['label']   # Row with specific index
df.loc['a':'c']   # Range of rows by label

# Boolean indexing
df[df['Age'] > 30]                    # Rows where Age > 30
df[(df['Age'] > 25) & (df['City'] == 'London')]  # Multiple conditions
```

### Setting Index

```python
df.set_index('column_name', inplace=True)  # Set column as index
df.reset_index(inplace=True)               # Reset to default index
```

---

## Data Cleaning

### Handling Missing Data

```python
# Detect missing values
df.isnull()       # Boolean DataFrame showing missing values
df.isnull().sum() # Count of missing values per column

# Handling missing values
df.dropna()              # Drop rows with any missing values
df.dropna(axis=1)        # Drop columns with any missing values
df.dropna(subset=['col']) # Drop rows missing specific column
df.fillna(value)         # Fill missing values
df.fillna(method='ffill') # Forward fill
df.fillna(df.mean())     # Fill with column mean
```

### Data Type Conversion

```python
df['column'] = df['column'].astype('int')
df['date_col'] = pd.to_datetime(df['date_col'])
```

### Removing Duplicates

```python
df.drop_duplicates()                    # Remove duplicate rows
df.drop_duplicates(subset=['col1', 'col2']) # Remove duplicates based on specific columns
```

### String Operations

```python
df['text_col'].str.upper()              # Convert to uppercase
df['text_col'].str.lower()              # Convert to lowercase
df['text_col'].str.contains('pattern')  # Check for substring
df['text_col'].str.replace('old', 'new') # Replace substring
```

---

## Data Analysis

### Descriptive Statistics

```python
df.describe()           # Summary statistics for numerical columns
df.mean()               # Mean of each column
df.median()             # Median
df.std()                # Standard deviation
df.min(), df.max()      # Minimum and maximum
df.count()              # Count non-null values
df.corr()               # Correlation matrix
```

### Sorting

```python
df.sort_values('column_name')                    # Sort by column
df.sort_values('col', ascending=False)          # Descending order
df.sort_values(['col1', 'col2'])                # Sort by multiple columns
```

### Adding/Removing Columns

```python
# Add new column
df['new_col'] = df['col1'] + df['col2']
df['constant_col'] = 100

# Remove columns
df.drop('column_name', axis=1, inplace=True)
df.drop(['col1', 'col2'], axis=1, inplace=True)
```

### Applying Functions

```python
# Apply function to each element
df['col'].apply(lambda x: x * 2)

# Apply function to each row
df.apply(lambda row: row['col1'] + row['col2'], axis=1)

# Vectorized operations (preferred for performance)
df['col1'] + df['col2']
```

---

## Data Aggregation

### GroupBy Operations

```python
# Basic grouping
grouped = df.groupby('column_name')
grouped = df.groupby(['col1', 'col2'])  # Multiple columns

# Aggregation methods
grouped.mean()
grouped.sum()
grouped.count()
grouped.size()          # Count including NaN values

# Multiple aggregations
grouped.agg({
    'col1': 'mean',
    'col2': ['min', 'max', 'count']
})

# Custom aggregation
grouped.agg({'col': lambda x: x.max() - x.min()})
```

### Pivot Tables

```python
pd.pivot_table(df, 
               values='value_col',
               index='row_category',
               columns='col_category',
               aggfunc='mean')
```

---

## Combining DataFrames

### Concatenation

```python
pd.concat([df1, df2])                    # Stack vertically
pd.concat([df1, df2], axis=1)           # Stack horizontally
```

### Merging (SQL-like joins)

```python
# Different types of joins
pd.merge(left, right, on='key_column')
pd.merge(left, right, on='key', how='inner')   # Default
pd.merge(left, right, on='key', how='left')
pd.merge(left, right, on='key', how='right')
pd.merge(left, right, on='key', how='outer')
```

### Joining

```python
# Join on index
df1.join(df2, how='left')
```

---

## Data Visualization with Matplotlib

### Introduction to Matplotlib

Matplotlib is Python's primary plotting library for creating static, interactive, and animated visualizations.

```python
import matplotlib.pyplot as plt

# Basic setup for Jupyter notebooks
%matplotlib inline

# Style options (built-in matplotlib styles)
plt.style.available  # View available styles
plt.style.use('ggplot')  # or 'classic', 'bmh', 'dark_background', etc.
```

### Basic Plot Types

#### Line Plots

```python
# From pandas Series
plt.figure(figsize=(10, 6))
plt.plot(df['x_column'], df['y_column'])
plt.title('Line Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.grid(True)
plt.show()

# Multiple lines
plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['y1'], label='Series 1')
plt.plot(df['x'], df['y2'], label='Series 2')
plt.plot(df['x'], df['y3'], label='Series 3')
plt.title('Multiple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

#### Bar Plots

```python
# Vertical bar plot
categories = df['category_column'].value_counts().index
counts = df['category_column'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(categories, counts)
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.show()

# Horizontal bar plot
plt.figure(figsize=(10, 6))
plt.barh(categories, counts)
plt.title('Horizontal Bar Plot')
plt.xlabel('Count')
plt.ylabel('Categories')
plt.show()

# Grouped bar plot
x = np.arange(len(df['category']))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, df['value1'], width, label='Value 1')
plt.bar(x + width/2, df['value2'], width, label='Value 2')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Grouped Bar Plot')
plt.xticks(x, df['category'])
plt.legend()
plt.show()
```

#### Histograms

```python
# Single histogram
plt.figure(figsize=(10, 6))
plt.hist(df['numeric_column'], bins=20, edgecolor='black', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()

# Multiple histograms
plt.figure(figsize=(10, 6))
plt.hist(df['col1'], bins=20, alpha=0.5, label='Column 1')
plt.hist(df['col2'], bins=20, alpha=0.5, label='Column 2')
plt.title('Multiple Histograms')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

#### Box Plots

```python
# Single box plot
plt.figure(figsize=(8, 6))
plt.boxplot(df['numeric_column'])
plt.title('Box Plot')
plt.ylabel('Values')
plt.grid(True, alpha=0.3)
plt.show()

# Multiple box plots
plt.figure(figsize=(10, 6))
plt.boxplot([df['col1'], df['col2'], df['col3']], 
            labels=['Column 1', 'Column 2', 'Column 3'])
plt.title('Multiple Box Plots')
plt.ylabel('Values')
plt.grid(True, alpha=0.3)
plt.show()
```

#### Scatter Plots

```python
# Basic scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['col1'], df['col2'])
plt.title('Scatter Plot')
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.grid(True, alpha=0.3)
plt.show()

# With color coding and size
colors = np.where(df['category'] == 'A', 'red', 'blue')
sizes = df['value'] * 10  # Scale sizes for visibility

plt.figure(figsize=(10, 6))
plt.scatter(df['col1'], df['col2'], c=colors, s=sizes, alpha=0.6)
plt.title('Scatter Plot with Color Coding')
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.grid(True, alpha=0.3)
plt.show()
```

#### Pie Charts

```python
plt.figure(figsize=(8, 8))
counts = df['category_column'].value_counts()
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()
```

### Customizing Plots

#### Figure and Axes Objects

```python
# Using plt.subplots() for more control
fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(df['x'], df['y'], color='red', linewidth=2, marker='o')
ax.set_title('Customized Plot', fontsize=16, fontweight='bold')
ax.set_xlabel('X Label', fontsize=12)
ax.set_ylabel('Y Label', fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend(['Data Series'])

# Customize ticks
ax.tick_params(axis='both', which='major', labelsize=10)

plt.tight_layout()
plt.show()
```

#### Multiple Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Plot 1 - Line plot
axes[0, 0].plot(df['x'], df['y1'])
axes[0, 0].set_title('Line Plot')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2 - Histogram
axes[0, 1].hist(df['numeric_col'], bins=20, edgecolor='black', alpha=0.7)
axes[0, 1].set_title('Histogram')
axes[0, 1].grid(True, alpha=0.3)

# Plot 3 - Scatter plot
axes[1, 0].scatter(df['col1'], df['col2'])
axes[1, 0].set_title('Scatter Plot')
axes[1, 0].grid(True, alpha=0.3)

# Plot 4 - Bar plot
categories = df['category'].value_counts().index[:5]
counts = df['category'].value_counts().values[:5]
axes[1, 1].bar(categories, counts)
axes[1, 1].set_title('Bar Plot')
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

#### Advanced Customization

```python
# Create a professional-looking plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data
line = ax.plot(df['date'], df['value'], 
               color='#2E86AB', 
               linewidth=2.5, 
               marker='o',
               markersize=4,
               markerfacecolor='#F24236',
               markeredgecolor='black',
               markeredgewidth=0.5,
               label='Values')

# Customize appearance
ax.set_title('Time Series Data Analysis', 
             fontsize=16, 
             fontweight='bold', 
             pad=20)
ax.set_xlabel('Date', fontsize=12, fontweight='bold')
ax.set_ylabel('Value', fontsize=12, fontweight='bold')

# Customize grid
ax.grid(True, linestyle='--', alpha=0.7)

# Customize spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Customize ticks
ax.tick_params(axis='both', which='major', labelsize=10)

# Add legend
ax.legend(frameon=True, fancybox=True, shadow=True, framealpha=0.9)

# Add annotation
max_idx = df['value'].idxmax()
ax.annotate(f'Peak: {df["value"].max():.1f}', 
            xy=(df['date'][max_idx], df['value'][max_idx]),
            xytext=(df['date'][max_idx], df['value'][max_idx] + 10),
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
            fontsize=10,
            ha='center')

plt.tight_layout()
plt.show()
```

### Pandas Integration Examples

#### Time Series Plotting

```python
# With datetime index
df.set_index('date_column', inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['value_column'])
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Rolling averages
df['rolling_mean'] = df['value'].rolling(window=7).mean()

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['value'], label='Original', alpha=0.7)
plt.plot(df.index, df['rolling_mean'], label='7-Day Moving Average', linewidth=2)
plt.title('Time Series with Moving Average')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

#### Correlation Heatmap (Pure Matplotlib)

```python
# Create correlation matrix
corr_matrix = df.corr()

# Plot heatmap using matplotlib
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(corr_matrix, cmap='coolwarm', aspect='auto')

# Add colorbar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Correlation', rotation=-90, va="bottom")

# Set ticks and labels
ax.set_xticks(np.arange(len(corr_matrix.columns)))
ax.set_yticks(np.arange(len(corr_matrix.columns)))
ax.set_xticklabels(corr_matrix.columns)
ax.set_yticklabels(corr_matrix.columns)

# Rotate x labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add correlation values as text
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                       ha="center", va="center", color="black")

ax.set_title("Correlation Heatmap")
plt.tight_layout()
plt.show()
```

### Saving Plots

```python
# Save as image file
plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['y'])
plt.title('My Plot')
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('my_plot.pdf')  # Vector format
plt.show()
```

### Common Plotting Patterns

```python
# Quick exploratory plots using pure matplotlib
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Create subplots for all numeric columns
fig, axes = plt.subplots(2, len(numeric_cols), figsize=(15, 8))

for i, col in enumerate(numeric_cols):
    # Histogram
    axes[0, i].hist(df[col], bins=20, edgecolor='black', alpha=0.7)
    axes[0, i].set_title(f'Histogram of {col}')
    axes[0, i].set_xlabel(col)
    axes[0, i].set_ylabel('Frequency')
    
    # Box plot
    axes[1, i].boxplot(df[col])
    axes[1, i].set_title(f'Box Plot of {col}')
    axes[1, i].set_ylabel('Values')

plt.tight_layout()
plt.show()
```

### Advanced Plot Types

#### Area Plots

```python
plt.figure(figsize=(10, 6))
plt.fill_between(df['x'], df['y1'], alpha=0.5, label='Series 1')
plt.fill_between(df['x'], df['y2'], alpha=0.5, label='Series 2')
plt.title('Area Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

#### Error Bars

```python
plt.figure(figsize=(10, 6))
plt.errorbar(df['x'], df['y'], yerr=df['error'], 
             fmt='o', capsize=5, capthick=2)
plt.title('Plot with Error Bars')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True, alpha=0.3)
plt.show()
```

---

## Useful Stuff

### Memory Usage

```python
df.memory_usage(deep=True)  # Check memory usage
```

### Display Options

```python
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
```

### Working with Dates

```python
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
```

### Conditional Operations

```python
# np.where for conditional logic
df['new_col'] = np.where(df['col'] > threshold, 'high', 'low')

# Multiple conditions
conditions = [
    df['score'] >= 90,
    df['score'] >= 80,
    df['score'] >= 70
]
choices = ['A', 'B', 'C']
df['grade'] = np.select(conditions, choices, default='F')
```
