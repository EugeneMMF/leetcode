import base64
import uuid
import re

class Codec:
    def __init__(self):
        self.map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        end = re.match(r"^[^/]+://[^/]+/(.*)$", longUrl).group(1)
        start = longUrl[:len(longUrl)-len(end)]
        replacement = uuid.uuid4().hex
        self.map[replacement] = longUrl
        return start + replacement


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        end = re.match(r"^[^/]+://[^/]+/(.*)$", shortUrl).group(1)
        return self.map.get(end, shortUrl)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))