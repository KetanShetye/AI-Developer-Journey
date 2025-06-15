# Efficient file I/O
# critical for working with large datasets in Pandas
# Let’s cover how to handle big files using chunksize and faster formats like Parquet.

# 🚀 Efficient File I/O in Pandas
# 🔹 1. Reading Large Files with chunksize
# Instead of loading the entire file into memory, you can read it in chunks:
# chunk_iter = pd.read_csv('large_file.csv', chunksize=100000)

# for chunk in chunk_iter:
#     # Process chunk
#     print(chunk.shape)
# ✅ Useful when files are too large to fit in RAM
# ✅ Each chunk is a regular DataFrame

# ➕ You can also aggregate on-the-fly:
# total = 0
# for chunk in pd.read_csv('large_file.csv', chunksize=100000):
#     total += chunk['amount'].sum()

# 🔹 2. Use Parquet for Speed and Compression
# ✅ Why Parquet?
# | Feature      | Parquet                 | CSV                      |
# | ------------ | ----------------------- | ------------------------ |
# | Speed        | Fast (binary format)    | Slower (text format)     |
# | Compression  | Built-in (snappy, gzip) | Needs manual compression |
# | Schema-aware | Yes                     | No                       |
# | File size    | Smaller                 | Larger                   |

# 🛠 Writing to Parquet:
# df.to_parquet("data.parquet", index=False)
# 🛠 Reading Parquet:
# df = pd.read_parquet("data.parquet")

# 🧪 Requires: pyarrow or fastparquet:
# pip install pyarrow
# # or
# pip install fastparquet

# 🧠 Pro Tips
# | Task                           | Method                           |
# | ------------------------------ | -------------------------------- |
# | Read only selected columns     | `usecols=[...]` in `read_csv`    |
# | Read in chunks                 | `chunksize=...` in `read_csv`    |
# | Convert CSV to Parquet         | `df.to_parquet()`                |
# | Use compression with Parquet   | `compression='snappy'` (default) |
# | Read compressed CSV (gzip/zip) | `read_csv('file.csv.gz')`        |

# ✅ Summary
# chunksize = read large CSVs piece-by-piece
# Parquet = best format for big datasets (faster + smaller)
# Combine both for scalable data pipelines