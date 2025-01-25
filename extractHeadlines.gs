function processUrlsFromSheet() {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var urls = sheet.getRange("C7:C").getValues(); // Get URLs from column C starting at row 7
    var headlines = [];

    // Loop through the URLs to extract the headlines
    for (var i = 0; i < urls.length; i++) {
        var url = urls[i][0]; // Get URL from the current row in column C
        var headline = ''; // Default value
        if (url) {
            headline = extractHeadline(url); // Extract headline
        }
        // Ensure headline is a string and push it to the headlines array
        headlines.push([String(headline)]);
    }

    // Write the headlines to the corresponding rows in column L
    sheet.getRange(7, 12, headlines.length, 1).setValues(headlines); // Column L is column 12
}

// Add a custom menu to the Google Sheet
function onOpen() {
    var ui = SpreadsheetApp.getUi();
    ui.createMenu('Custom Tools') // Menu name
        .addItem('Extract Headlines', 'processUrlsFromSheet') // Menu item and function to call
        .addToUi();
}
