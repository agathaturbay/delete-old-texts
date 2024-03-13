# delete-old-texts
Description:

This Python script effectively removes messages older than a specified date from WhatsApp conversations exported as TXT files. It empowers users to manage storage space and maintain focus on recent conversations.

# Key Features:

Clear and concise code structure for easy understanding and modification.
Customizable date threshold for flexible control over message removal.
Preserves conversation structure by retaining line breaks and formatting.
Explicit error handling ensuring a robust and reliable process.
Compatible with exported WhatsApp chat files in the specified format.
Usage:

Install Python (if not already installed).

Save the script as a .py file (e.g., "remove_old_whatsapp_texts.py").

Run the script from the command line, specifying the TXT file as an argument:

Bash
python remove_old_whatsapp_texts.py your_chat_file.txt

# Customization:

Adjust the date threshold within the remove_old_texts function:**

Python
limit_date = datetime.datetime(2023, 3, 11)  # Change this date as needed

# Compatibility:

Assumes WhatsApp export format: Lines starting with timestamps enclosed in square brackets (e.g., "[21/02/2024 15:47:22]").
Encoding: Utilizes cp437 encoding, which might need adjustments for different languages or character sets.
