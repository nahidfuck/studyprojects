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

def find_by_name(substring):
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + substring + '%',))
    return cursor.fetchall()

def update_phone(email, new_phone):
    cursor.execute(
    "UPDATE contacts SET phone = ? WHERE email = ?",
    (new_phone, email)
    )
    conn.commit()

def delete_contact(email):
    cursor.execute("DELETE FROM contacts WHERE email = ?", (email,))
    conn.commit()

def search_by_email_domain(domain):
    cursor.execute("SELECT * FROM contacts WHERE email LIKE ?", ('%@' + domain + "%",))
    return cursor.fetchall()

cursor.execute("SELECT * FROM contacts ORDER BY name ASC")
print(cursor.fetchall())
cursor.execute("SELECT * FROM contacts ORDER BY name DESC")
print(cursor.fetchall())
cursor.execute("SELECT * FROM contacts ORDER BY id DESC")
print(cursor.fetchall())

print("\nBefore update:")
print(cursor.execute("SELECT * FROM contacts").fetchall())

update_phone("tylerthekutas@gmail.com", "+111111111111")

delete_contact("ashabtamaev@icloud.com")

print("\nSearch by domain 'gmail':")
print(search_by_email_domain("gmail"))

conn.close()
