import requests
import os
from dotenv import load_dotenv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet

load_dotenv()

application_id = os.environ.get("APPLICATION_ID")
access_key = os.environ.get("ACCESS_KEY")
secret_key = os.environ.get("SECRET_KEY")


def unsplash_image_search(search_term):
    client_id = access_key
    url = f"https://api.unsplash.com/search/photos?page=1&orientation=landscape&query={search_term}&client_id={client_id}"

    response = requests.get(url)
    if response.status_code == 200:
        photos = response.json()['results']
        if photos:
            first_photo = photos[0]
            #print(first_photo)  # Print details of the first photo

            first_photo_url = first_photo['urls']['regular']  # URL of the first image
            print(first_photo_url)

            photographer = first_photo['user']
            credit_text = f"Photo by <a href=\"https://unsplash.com/@{photographer['username']}?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText\">{photographer['name']}</a> on <a href=\"https://unsplash.com/photos/{first_photo['id']}?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText\">Unsplash</a>"
            print(credit_text)
            return [first_photo_url, credit_text]
        else:
            print("No images found for the search term.")
    else:
        print("Failed to fetch images:", response.status_code)



def title_to_query(title):
    # Install NLTK and download necessary datasets
    nltk.download('punkt')
    nltk.download('stopwords')
    # Tokenize the title
    tokens = word_tokenize(title)

    # Custom stop words - focusing on removing only the most common words
    custom_stopwords = set(stopwords.words('english')) - {'video', 'ad', 'campaign', 'admocker'}

    # Extracting key words - Only keep words not in custom stopwords
    key_words = [word for word in tokens if word.lower() not in custom_stopwords]

    # Create search query - Joining the key words to form a query
    query = ' '.join(key_words)
    return query



