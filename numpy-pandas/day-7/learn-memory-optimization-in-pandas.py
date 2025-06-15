# ✅ Memory Optimization in Pandas
# Large datasets can consume a lot of memory, and Pandas doesn’t always choose the most efficient data types by default. 
# Here's how you can reduce memory usage significantly using smart data type conversions.

# 📏 Step 1: Check Initial Memory Usage
# print(df.info(memory_usage='deep'))
# print(df.memory_usage(deep=True))  # More detailed

# 💡 Key Optimization Techniques
# 🔹 1. Convert float64 → float32 or float16 (if needed)
# df['amount'] = df['amount'].astype('float32')
# Use float32 when high precision is not critical (e.g., sensor data, ML).

# 🔹 2. Convert int64 → int32, int16, or int8
# df['count'] = df['count'].astype('int16')
# | Type  | Range                 |
# | ----- | --------------------- |
# | int8  | -128 to 127           |
# | int16 | -32,768 to 32,767     |
# | int32 | -2.1 billion to +2.1B |
# Match the column range to the smallest possible type.

# 🔹 3. Convert object → category (for repeated strings)
# df['gender'] = df['gender'].astype('category')
# Useful for columns with repeated values, e.g., states, genders, yes/no.

# 🔹 4. Parse date columns efficiently
# df['date'] = pd.to_datetime(df['date'], errors='coerce')
# Reduces memory and makes date operations much faster.

# 🔹 5. Use low_memory=True while reading CSVs
# df = pd.read_csv("file.csv", low_memory=True)
# Helps prevent dtype inference issues on large files.

# 🧪 Bonus: Auto Optimize Dtypes (Function)
def optimize_dtypes(df):
    for col in df.columns:
        col_type = df[col].dtype
        
        if col_type == 'object':
            num_unique = df[col].nunique()
            num_total = len(df[col])
            if num_unique / num_total < 0.5:
                df[col] = df[col].astype('category')
                
        elif col_type == 'int64':
            if df[col].max() < 128:
                df[col] = df[col].astype('int8')
            elif df[col].max() < 32768:
                df[col] = df[col].astype('int16')
            elif df[col].max() < 2147483648:
                df[col] = df[col].astype('int32')
        
        elif col_type == 'float64':
            df[col] = df[col].astype('float32')
    
    return df

# 📉 Measure Again
# print(df.info(memory_usage='deep'))
# Compare before and after optimization to confirm memory savings.