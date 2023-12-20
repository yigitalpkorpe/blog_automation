# Automated Blog Post Generator

## Overview
This Python script automates the creation of SEO-optimized blog posts for digital marketing and advertising topics. It leverages OpenAI's GPT models, extracts blog topics from a sitemap, and fetches relevant images from Unsplash. For a detailed blog post about this project, visit [https://about.yigitalpkorpe.com/projects/blog-automation.html](https://about.yigitalpkorpe.com/projects/blog-automation.html)

If you have any questions or inquiries about this project, feel free to email me at yigitalp@yigitalpkorpe.com

## Features
- **OpenAI Integration**: Uses OpenAI's API to generate blog content.
- **Sitemap Parsing**: Fetches URLs from a specified sitemap for content ideas.
- **Image Retrieval**: Implements Unsplash API for fetching relevant images.
- **Content Formatting**: Converts generated content to HTML format for blog posts.
- **Unique Slug Creation**: Generates SEO-friendly URLs for each post.

## Requirements
- Python 3.x
- `requests`
- `bs4` (BeautifulSoup)
- `nltk`
- OpenAI and Unsplash API keys

## Setup
1. Clone the repository.
2. Install required Python packages: `pip install requests bs4 nltk`.
3. Set up your `.env` file with your OpenAI API key, Unsplash access key, and sitemap URL.

## Usage
1. Run the script to fetch existing blog URLs from the sitemap.
2. Generate blog post content using the OpenAI API.
3. Fetch a relevant image from Unsplash based on the post title.
4. Format the content into an HTML template and save as a PHP file.

## Contribution
Feel free to fork this project and contribute. If you find any bugs or have suggestions, please open an issue or submit a pull request.


## Acknowledgments
- This project uses OpenAI's GPT models for content generation.
- Images are sourced from Unsplash.
