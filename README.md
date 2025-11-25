Simple Mood Tracker:
A lightweight and user-friendly desktop application built with Python and Tkinter that allows users to track their daily moods.  
The app stores each day's mood in a local JSON file and provides options to view the current day's mood or the full mood history.

Overview:
The **Simple Mood Tracker** is designed to help users quickly log how they feel each day.  
With a clean interface and easy-to-use controls, it is ideal for beginners, students, and anyone wanting a simple daily habit tool.
The application uses a dropdown menu for mood selection and saves the entry with the current date.  
It also allows viewing of today's mood or all previously logged moods.

Features:
- Select and log your mood for the current day.
- Automatically saves entries with the date.
- View today's logged mood instantly.
-  View all previously stored moods in a clear list.
- Data stored locally in a JSON file (`simple_moods.json`).
- Simple and clean Tkinter GUI.
  
Technologies / Tools Used:
- **Python 3**
- **Tkinter** (GUI Framework)
- **JSON** (Local data storage)
- **datetime** (Handling dates)
- 
 Steps to Install & Run the Project:
1.download the source files manually.

2. Ensure Python is Installed
Check your Python version:
python --version
Python 3.7+ is recommended.

3. Run the Application
Navigate to the project folder and run:
python mood_tracker.py
The GUI window will open.

Instructions for Testing:
Open the app.
Select a mood from the dropdown list.
Click "Log Mood" to save it.
Click "Show Today's Mood" to verify your saved mood.
Click "Show All Moods" to view complete history.
Check simple_moods.json to ensure moods are stored correctly
