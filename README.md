# Scape & Summarize

## Functionality

- Scrap some form of textual media (audio transcripts can work)
- Obtain the following metrics using [LLaMA](https://github.com/facebookresearch/llama)
  - Summary
  - Read time
  - Difficulty
- Return the resulting scraped information and derived information for use in a consumer interface

## Setup





## How it works

- Flask HTTP server receives a request for textual media (and derived information)
- Either [Selenium](https://www.selenium.dev) or [requests](https://requests.readthedocs.io/en/latest/) gathers the following from a multitude of articles:
  - Title
  - Author
  - Date
  - Image
  - Content (body of text)
- This 'scrapped data' is then sent to the LLaMA model (and potentially other decision makers) to gather the following 'derived data'
  - Summary
  - Read time
  - Difficulty
- The scrapped & derived data is then sent through the HTTP response body



