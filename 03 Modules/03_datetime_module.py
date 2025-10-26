print("=== Python Modules: The datetime Module ===\n")

print("1️⃣  The datetime module helps work with dates and times — creating, formatting, and performing calculations.\n")

print("🔎  Importing datetime")
print("import datetime\n")

import datetime

print("🕐  Getting the current date and time")
now = datetime.datetime.now()
print("datetime.datetime.now() =", now, "\n")

print("📅  Getting only date or time")
print("➡️  Current date =", now.date())
print("➡️  Current time =", now.time(), "\n")

print("🗓️  Creating specific dates and times")
specific_date = datetime.date(2025, 10, 26)
specific_time = datetime.time(14, 30, 45)
print("➡️  datetime.date(2025, 10, 26) =", specific_date)
print("➡️  datetime.time(14, 30, 45) =", specific_time)
custom_datetime = datetime.datetime(2025, 10, 26, 14, 30, 45)
print("➡️  datetime.datetime(2025, 10, 26, 14, 30, 45) =", custom_datetime, "\n")

print("🧮  Date arithmetic using timedelta")
today = datetime.date.today()
future = today + datetime.timedelta(days=7)
past = today - datetime.timedelta(days=30)
print("➡️  Today's date =", today)
print("➡️  7 days later =", future)
print("➡️  30 days ago =", past, "\n")

print("🔢  Getting date components")
print("➡️  Year =", today.year)
print("➡️  Month =", today.month)
print("➡️  Day =", today.day)
print("➡️  Weekday (0=Monday, 6=Sunday) =", today.weekday(), "\n")

print("🎨  Formatting dates and times (strftime)")
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("➡️  now.strftime('%Y-%m-%d %H:%M:%S') =", formatted)
print("➡️  Example formats:")
print("\t%Y = Year  (e.g., 2025)")
print("\t%m = Month (01-12)")
print("\t%d = Day   (01-31)")
print("\t%H = Hour  (00-23)")
print("\t%M = Minute")
print("\t%S = Second")
print("\t%A = Weekday name")
print("\t%B = Month name\n")

print("📖  Parsing string dates into datetime objects (strptime)")
date_string = "2025-10-26 15:45:30"
parsed = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("➡️  datetime.strptime('2025-10-26 15:45:30', '%Y-%m-%d %H:%M:%S') =", parsed, "\n")

print("🌍  Working with UTC and time zones")
print("➡️  datetime.datetime.utcnow() gives current UTC time =", datetime.datetime.utcnow(), "\n")

print("✅  End of datetime module note — covers creation, arithmetic, formatting, and parsing of dates & times.")
