---
trigger: model_decision
description: Only if you want to download material from AnyFlip for any reason
---

# Anyflip Download Instructions

To download reference materials and RPG books hosted on Anyflip, an `anyflip-downloader` CLI tool has been installed on this system.

## Setup
The tool is globally available in your PowerShell environment. 
A helper script is also available at `Inspiration/Download_From_Anyflip.ps1` for ease of use.

## How to use (Helper Script)
1. Open PowerShell and navigate to your `Inspiration` folder.
2. Run the helper script with the target URL and an optional Title:
   ```powershell
   .\Download_From_Anyflip.ps1 -Url "https://anyflip.com/xxxxx/yyyy" -Title "Book_Name"
   ```
3. The PDF will be generated in the `Inspiration` folder.

## How to use (Direct CLI)
If you prefer to use the CLI from anywhere on your PC:
```powershell
anyflip-downloader "https://anyflip.com/xxxxx/yyyy"
```
Or to specify a custom title:
```powershell
anyflip-downloader -title "Book_Name" "https://anyflip.com/xxxxx/yyyy"
```

## Troubleshooting
- If a download gets stuck or returns `403 Forbidden`, the specific book or its images might have restricted access blocking programmatic downloads.
- Temporary folders (e.g., `osr-source-1`) might be left behind if a download fails. You can safely delete these.
