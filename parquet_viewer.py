import tkinter as tk
from tkinter import filedialog
import pandas as pd
import pyarrow.parquet as pq

# Function to open and display a Parquet file
def open_parquet_file():
    file_path = filedialog.askopenfilename(title="Open Parquet File", filetypes=[("Parquet Files", "*.parquet")])
    if file_path:
        parquet_data = pq.read_table(file_path)
        df = parquet_data.to_pandas()
        text.delete(1.0, tk.END)
        text.insert(tk.END, df.to_string())
        display_file_summary(df)

# Function to display a summary of the loaded file
def display_file_summary(df):
    summary_text.config(state=tk.NORMAL)
    summary_text.delete(1.0, tk.END)
    summary_text.insert(tk.END, "File Summary:\n")
    summary_text.insert(tk.END, f"Number of rows: {len(df)}\n")
    summary_text.insert(tk.END, f"Number of columns: {len(df.columns)}\n")
    summary_text.insert(tk.END, f"Index Range: {df.index[0]} - {df.index[-1]}\n")
    summary_text.config(state=tk.DISABLED)

# Create the main application window
app = tk.Tk()
app.title("Parquet File Reader")

# Create a Text widget to display Parquet data
text = tk.Text(app, wrap=tk.NONE)
text.pack(fill=tk.BOTH, expand=True)

# Create a Scrollbar and associate it with the Text widget
scrollbar = tk.Scrollbar(app, command=text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.config(yscrollcommand=scrollbar.set)

# Create an "Open" button to select a Parquet file
open_button = tk.Button(app, text="Open Parquet File", command=open_parquet_file)
open_button.pack()

# Create a Text widget for displaying file summary
summary_text = tk.Text(app, wrap=tk.NONE, height=4, state=tk.DISABLED)
summary_text.pack(fill=tk.BOTH, expand=False)

# Start the main application loop
app.mainloop()

