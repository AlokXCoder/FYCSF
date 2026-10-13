import pandas as pd

df = pd.DataFrame({
    'post' : ["Good Product", "Bad Service", "Good Product", None],
    'likes' : ["10", "5", "10", "3"]
})
print(df.info())

df = df.drop_duplicates()
df['post'] = df["post"].fillna("Unknown")
df["likes"] = pd.to_numeric(df["likes"], errors="coerce")
df["likes"] = df["likes"].fillna(0)
df.to_csv("processed_data.csv", index=False)
print(df)
print("Processed File Saved Successfully.")
