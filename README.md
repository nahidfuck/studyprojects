# studyprojects

A collection of small, focused Python mini-projects for learning and practicing file I/O and simple data storage patterns (JSON and SQLite).

## What this repo contains

This repository groups short example scripts and sample data used while learning about working with files and lightweight data stores in Python.

Top-level layout

- `workWithFiles/` — Examples showing working with JSON files and a simple contact manager.
	- `contacts.json` — sample contacts data used by the examples.
	- `fileswork2.0.py` — a script demonstrating reading and writing files (JSON operations, etc.).
	- `contactmaanager/` — a small contact-manager module/collection.
		- `contacts.json` — sample contacts for the manager.
		- `managercontact.py` — a script implementing simple contact management functionality.

- `sqlite/` — examples using SQLite for storing contacts.
	- `contactsdata.py` — a script demonstrating SQLite usage for contact storage and retrieval.

## Requirements

- Python 3.8+ (should work on 3.8, 3.9, 3.10 and later).
- No external packages are required unless an example script documents otherwise — the included scripts use the Python standard library.

## How to run the example scripts (Windows PowerShell)

Open a PowerShell prompt in the root of this repository and run the scripts directly with Python. Example commands:

```powershell
python .\workWithFiles\fileswork2.0.py
python .\workWithFiles\contactmaanager\managercontact.py
python .\sqlite\contactsdata.py
```

Notes:

- The scripts operate on the sample JSON files in `workWithFiles/` and the `sqlite/contactsdata.py` script works with a local SQLite database file (if created by the script).
- If a script prints usage or has command-line options, run it with `-h` or inspect the top of the file for a brief header describing usage.

## Inspecting / Editing Data

- The files `workWithFiles/contacts.json` and `workWithFiles/contactmaanager/contacts.json` are plain JSON — you can open them in a text editor to view or edit sample data.
- If you want to persist changes made by the SQLite example, check the script to see which database filename it creates/uses (commonly a `.db` or `.sqlite` file in the same folder).


---

If you'd like, I can also:

- add short per-script usage sections in this README (I can open each file and extract a short description),
- create a minimal `requirements.txt` or `pyproject.toml` if you plan to add dependencies, or
- add simple tests for one of the examples.

Tell me which of those you'd like next and I will update the repo.
