import requests
from bs4 import BeautifulSoup
import json

def fetch_news_titles(url):
    """
    Fetches news article titles from a given URL.

    Args:
        url (str): The target news website URL.

    Returns:
        list: A list of article titles.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Ensure the correct encoding is used for proper text rendering
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')

        script_tag = soup.find('script', type='application/ld+json')

        if script_tag:
            # Parse the JSON-LD data
            json_data = json.loads(script_tag.string)

            # Extracting the headline
            headline = json_data.get('@graph', [])[0].get('headline', 'No headline found')

            return [headline]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

def main():
    """Main function to extract news titles from multiple websites."""
    # Define the target URLs
    urls = [
        "https://www.tamilmurasu.com.sg/singapore/taxi-crashes-chinese-temple",
        "https://www.8world.com/singapore/man-jailed-for-running-over-station-inspector-foot-with-red-porche-2680806",
        "https://www.zaobao.com.sg/news/singapore/story20250117-5748860",
        "https://www.zaobao.com.sg/realtime/singapore/story20250117-5748894",
        "https://berita.mediacorp.sg/singapura/ruang-seni-baharu-di-kampong-jawa-903296",
        "https://www.beritaharian.sg/singapura/saf-ada-sistem-saring-kesan-anggota-yang-mungkin-timbulkan-ancaman"
    ]

    for url in urls:
        print(f"Fetching titles from {url}...")
        titles = fetch_news_titles(url)

        if titles:
            print(f"Found {len(titles)} titles:")
            for title in titles:
                print(f"{title}")
        else:
            print("No titles found.")

        print("\n")

if __name__ == "__main__":
    main()