import requests
from openai import OpenAI
from dotenv import load_dotenv
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup
import re
from unsplash_image import title_to_query, unsplash_image_search


load_dotenv()

# your environment variables
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)
sitemap_url = os.environ.get("SITEMAP")
template = os.environ.get("TEMPLATE")

def write_blog(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        #model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are an AI assistant with expertise in digital marketing, SEO, and content creation. Your task is to write engaging and SEO-optimized blog posts for Ad Mocker, a website offering a tool for previewing paid ad placements. The content should appeal to users interested in online advertising, ad design, and marketing technology. Ensure the blog posts are unique, helpful for daily task for readers, informative, and designed to enhance organic traffic for the website. Avoid topics that are already covered in existing blog posts."},

            {"role": "user", "content": prompt }
        ]
    )

    message = completion.choices[0].message
    response = message.content
    return response


def fetch_urls_from_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    root = ET.fromstring(response.content)
    return [url.text for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc') if '/blog/' in url.text and not url.text.rstrip('/') == 'https://admocker.com/blog']


def fetch_h1_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        h1_tag = soup.find('h1')
        return h1_tag.text if h1_tag else ''
    except requests.RequestException:
        return 'Failed to Fetch'


def generate_prompt_with_urls(urls):
    prompt = "Please generate a blog post following the provided guidelines. The post should be informative and relevant to users interested in online advertising and ad design. Avoid repeating topics covered in existing blog posts. The content should fit into the provided HTML template and include a catchy title, introduction, main content with subtitles, and a conclusion. Provide a compelling image link and alt text appropriate for the topic. Fill in the content within this HTML template:" + template + ". Return just the html code. Blog post word count should be long at least 1000 words. Exclude the following blog post titles:"
    prompt += ", ".join(urls)
    return prompt


def slugify(title):
    title = title.lower()
    return re.sub(r'\W+', '-', title)

def save_as_php(content, slug):
    filename = f"{slug}.php"
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Blog saved as {filename}")



urls = fetch_urls_from_sitemap(sitemap_url)
h1_texts = [fetch_h1_from_url(url) for url in urls]

# Generate a prompt with the fetched URLs
prompt = generate_prompt_with_urls(h1_texts)

blog_html = write_blog(prompt)

# print(blog_html)

# Extract title and convert to slug
title_match = re.search(r'<h1>(.*?)</h1>', blog_html)
if title_match:
    title = title_match.group(1)
    slug = slugify(title)
    
    search_query = title_to_query(title)
    unsplash_image = unsplash_image_search(search_query)
    unsplash_image_url = unsplash_image[0]
    unsplash_image_credit = unsplash_image[1]

    blog_html = re.sub(r"<img class=['\"]blog-image['\"] src=['\"](.*?)['\"]", f"<img class='blog-image' src='{unsplash_image_url}'", blog_html)
    blog_html = re.sub(r"<p class=['\"]small-caption['\"]>(.*?)</p>", f"<p class='small-caption'>{unsplash_image_credit}</p>", blog_html)




    save_as_php(blog_html, slug)
else:
    print("No title found in the blog content")





