import datetime

def remove_old_texts(txt_file):
  # Here you can set the desired date. The format I'm using is dd/mm/yyyy #
  limit_date = datetime.datetime(2024, 3, 13)
  new_lines = []

  with open(txt_file, "r", encoding='cp437') as f:
    for line in f:
      """ Whatsapp exported texts have the format [dd/mm/yyy HH:MM:SS] so I'm adapting the script to work with that. 
      Besides that, the verification is needed to make sure that you're only filtering new messages, while ignoring 
      the messages that are written over multiple lines and use enter or '\n' """
      if line[:21].strip().startswith('['):
        try:
          line_date = datetime.datetime.strptime(line[:21], "[%d/%m/%Y %H:%M:%S]")
          if line_date >= limit_date:
            new_lines.append(line)
        except ValueError:
          pass  

  with open(txt_file, "w", encoding='cp437') as f:
    f.writelines(new_lines)


if __name__ == "__main__":
  remove_old_texts("txt_file.txt")
