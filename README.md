# News Headline Extraction
An automated news aggregation tool that utilizes Javascript to scrape headlines from an array of news websites on Google Sheets to efficiently collect and organize headlines from news sources.

## How to use
### Setup
1. Open Google Sheets:
* Open the sheet where you want to process URLs and extract headlines.

2. Access Apps Script:
* Go to Extensions > Apps Script.

3. Paste the Script:
* Delete any default code and paste the provided script.

4. Save the Script:
* Click the Save icon, name it (e.g., Headline Extractor).

5. Authorize the Script:
* Click the Run button ▶️ for the onOpen function.
* Follow the prompts to grant permissions.

#### Using the Script
6. Return to Google Sheets:
* Close the Apps Script editor.
* A new Custom Tools menu will appear in the toolbar.

7. Prepare Your Data:
* List URLs in column C, starting from row 7 (e.g., C7, C8).
* Leave column L (headlines) empty.

8. Run the Script:
* Click Custom Tools > Extract Headlines.

9. View Results:
* Extracted headlines from URLs in column C will appear in column L in the same rows.

#### Notes
Invalid URLs or missing headlines will result in blank cells in column L.
You can re-run the script anytime for updated data.
