import sqlite3

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT UNIQUE NOT NULL
)
""")

cursor.execute("INSERT OR IGNORE INTO contacts (name, phone, email) VALUES (?, ?, ?)", ("Tyler Durden", "+380768213710", "bobthepenis@gmail.com"))
cursor.execute("INSERT OR IGNORE INTO contacts (name, phone, email) VALUES (?, ?, ?)", ("Morgan Freeman son", "+380689159589", "tylerthekutas@gmail.com"))
cursor.execute("INSERT OR IGNORE INTO contacts (name, phone, email) VALUES (?, ?, ?)", ("Kim Cyciushki", "+380983999896", "ashabtamaev@icloud.com"))
conn.commit()

def list_contacts():
    cursor.execute("SELECT * FROM contacts")
    return cursor.fetchall()

def find_by_name(substring):
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + substring + '%',))
    return cursor.fetchall()

print("All contacts:")
printcontacts = list_contacts()
for contact in printcontacts:
    print(contact)

print("\nSearching for contacts with 'Tyler' in their name:")
search_results = find_by_name("Tyler")
for contact in search_results:
    print(contact)

conn.close()

