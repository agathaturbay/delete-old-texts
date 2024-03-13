import pandas as pd

def txt_to_csv(txt_file_path, csv_file_path):
  data = []
  with open(txt_file_path, encoding="utf-8") as f:
      for line in f:
          date, text = line.strip().split(" : ", 1)
          date = date[1:11]

          data.append({"date": date, "text": text, "sentiment": "", "related": ""})

  df = pd.DataFrame(data)

  df.to_csv(csv_file_path, index=False)

  print(f"Text file converted to CSV: {csv_file_path}")

txt_file_path = "txt_file.txt" 
csv_file_path = "output.csv"

txt_to_csv(txt_file_path, csv_file_path)
