# File Integrity Monitoring System

A simple Python-based file integrity monitoring project that uses SHA-256 hashing to detect changes in a file.

I built this project to understand how file integrity can be checked using cryptographic hashes and to get practical experience with a basic security monitoring concept.

## What this project does

The program:

- Calculates a SHA-256 hash for a file
- Creates a baseline hash automatically on the first run
- Compares the current file hash with the saved baseline
- Detects when a file has been modified
- Shows the time of each integrity check
- Records integrity check results in a log file
- Handles common file access errors

## Technologies Used

- Python 3
- SHA-256
- Python hashlib
- File handling
- Git
- GitHub
- VS Code

## Project Structure

```text
File-Integrity-Monitor/
├── integrity_monitor.py
├── .gitignore
├── test.txt
├── baseline_hash.txt
└── integrity_log.txt
```

The `test.txt`, `baseline_hash.txt`, and `integrity_log.txt` files are used during local testing and are ignored by Git.

## How It Works

The project uses SHA-256 to create a fixed-length hash from the contents of a file.

The basic process is:

```text
File
  ↓
SHA-256 Hash
  ↓
Create Baseline
  ↓
Calculate Hash Again
  ↓
Compare Hashes
  ↓
Same → No Change
Different → File Modified
```

### First Run

When the program is run for the first time, it calculates the SHA-256 hash and saves it as the baseline.

Example:

```text
Baseline created successfully.
```

### Later Checks

When the program runs again, it calculates a new hash and compares it with the saved baseline.

If both hashes are the same:

```text
[+] File integrity verified. No changes detected.
```

If the hashes are different:

```text
[!] WARNING: File has been modified!
```

## Running the Project

Open a terminal inside the project folder and run:

```bash
python integrity_monitor.py
```

When prompted, enter the file you want to monitor:

```text
Enter file path: test.txt
```

The program will then calculate and compare the file's SHA-256 hash.

## Logging

The program records each check in:

```text
integrity_log.txt
```

Example log entries:

```text
2026-10-06 16:50:12 | NO CHANGE | test.txt
2026-10-06 16:52:30 | MODIFIED | test.txt
```

This makes it possible to see when an integrity check was performed and what the result was.

## Error Handling

The program handles common problems such as:

- File not found
- Permission denied
- Other operating system file access errors

Instead of immediately crashing, it displays a useful error message.

## Testing

I tested the project using a local `test.txt` file.

The main tests were:

1. Run the program for the first time and create the baseline.
2. Run it again without changing the file.
3. Modify the file and run the program again.
4. Confirm that the program detects the modification.
5. Check that the result is written to the integrity log.

The project correctly detected the modified test file during testing.

## What I Learned

While building this project, I learned:

- How SHA-256 hashing works at a basic practical level
- How Python's `hashlib` module is used
- How file contents can be converted into a hash
- Why hashes are useful for detecting changes
- How to create and compare a baseline
- How to work with files in Python
- How to record security-related events in a log
- How basic file integrity monitoring works
- How to handle file access errors

## Limitations

This is a basic learning project, so it has some limitations:

- It monitors one file at a time
- The baseline is stored locally
- It does not continuously monitor a directory
- It does not send email or other alerts
- The baseline file itself needs to be protected from unauthorized changes
- It does not use a database for storing monitoring information

## Future Improvements

Some improvements I could add later:

- Monitor multiple files or an entire directory
- Run checks automatically at regular intervals
- Add email or desktop notifications
- Store monitoring data in a database
- Add a command-line interface
- Protect the baseline information more securely
- Add a simple dashboard for monitoring results

## Ethical Use

This project is intended for educational purposes and authorized security monitoring.

It should be used on files and systems that you own or have permission to monitor.

## Author

**Bhuvaneshwar Mushke**

B.Tech in Computer Science and Engineering (Cyber Security)

This project is part of my practical cybersecurity learning and portfolio.
