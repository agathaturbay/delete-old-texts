import re
import datetime

""" This function was created to erase messages previous to a specific date. 
To change the date you can change line 9 and put the year, month and day you desire, in this order
As the format from exported Whatsapp messages in my country is [dd/mm/yyyy] that's what I'm using.
Also, the function verifies if the message is a new message or the same message in a different line to avoid code breaks."""
def remove_old_texts(txt_file):
  limit_date = datetime.datetime(yyyy, m, dd)
  new_lines = []

  with open(txt_file, "r", encoding='cp437') as f:
    for line in f:
      if line[:21].strip().startswith('['):
        try:
          line_date = datetime.datetime.strptime(line[:21], "[%d/%m/%Y %H:%M:%S]")
          if line_date >= limit_date:
            new_lines.append(line)
        except ValueError:
          pass  

  with open(txt_file, "w", encoding='cp437') as f:
    f.writelines(new_lines)


""" This function removes messages from a specific user. To erase all the messages from this user 
you can change line 33 and add the user name"""
def remove_user_messages(txt_file):
    new_lines = []

    with open(txt_file, "r", encoding='cp437') as f:
        for line in f:
            if not re.search(r"User ", line):
                new_lines.append(line)

    with open(txt_file, "w", encoding='cp437') as f:
        f.writelines(new_lines)


""" This function removes hidden media. 
Again, in my country we use "imagem ocultada" for hidden images, "áudio ocultado" for hidden audios
 and "figurinha omitida" for hidden stickers"""
def remove_hidden_media(txt_file):
    new_lines = []

    with open(txt_file, "r", encoding='cp437') as f:
        for line in f:
            if "imagem ocultada" not in line.lower() and r"áudio ocultado" not in line.lower() and "figurinha omitida" not in line.lower():
                new_lines.append(line)

    with open(txt_file, "w", encoding='cp437') as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    remove_old_texts("txt_file.txt")
    remove_user_messages("txt_file.txt")
    remove_hidden_media("txt_file.txt")