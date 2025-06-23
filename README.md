# IP Allow List Manager (Python)

This project demonstrates a simple Python automation script to manage a list of approved IP addresses for secure network access.

## Project Summary

This script simulates how a security analyst might maintain and update an IP allow list by:
- Reading IPs from a file
- Comparing them to a list of IPs to remove
- Updating the file with only the approved IPs

## Files

| File               | Description                                  |
|--------------------|----------------------------------------------|
| `ip_allowlist_manager.py` | Main Python script                      |
| `allow_list.txt`          | Sample list of allowed IPs              |
| `remove_list.txt`         | Sample list of IPs to remove            |

## Key Concepts

- File handling (`open`, `read`, `write`)
- List manipulation in Python
- Automation logic for cybersecurity operations

## How to Use

1. Update `allow_list.txt` with IPs you want to keep (space-separated or one per line).
2. Update `remove_list` in the script with the IPs you want to remove.
3. Run the script:

```bash
python ip_allowlist_manager.py
```

---

## Career Focus

I’m pursuing opportunities in:
- Security Operations Center (SOC) Analysis
- Threat Detection & Response
- Entry-Level Cybersecurity Support Roles

If you're hiring or collaborating on early-career cyber roles, feel free to connect!

---

**Let’s connect**: [LinkedIn](https://www.linkedin.com/in/corinnediorio2015) | **Certifications**: Google Cybersecurity | Studying: CompTIA Security+

You’ll see the updated allow list printed in your terminal, and the file will be overwritten with the new data.

---

*This project was created as part of a cybersecurity course to demonstrate practical Python file I/O and automation techniques.*
