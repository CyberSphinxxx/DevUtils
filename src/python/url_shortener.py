import hashlib
import sys

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten(self, url):
        """
        Generates a short hash for a URL.
        """
        hash_object = hashlib.md5(url.encode())
        short_hash = hash_object.hexdigest()[:6]
        self.url_map[short_hash] = url
        return f"http://short.url/{short_hash}"

    def retrieve(self, short_hash):
        """
        Retrieves the original URL from a hash.
        """
        return self.url_map.get(short_hash, "URL not found")

if __name__ == "__main__":
    shortener = URLShortener()
    if len(sys.argv) > 1:
        url = sys.argv[1]
        short = shortener.shorten(url)
        print(f"Original: {url}")
        print(f"Shortened: {short}")
    else:
        print("Usage: python url_shortener.py <url>")
