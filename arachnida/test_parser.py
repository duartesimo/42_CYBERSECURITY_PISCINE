from html.parser import HTMLParser

images = []

class ImageParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if (tag == 'img'):
            for name, value in attrs:
                if (name == 'src'):
                    images.append(value)

html = """
<h1>Hello World</h1>
<img src="cat.jpg" alt="A cat">
<a href="about.html">About us</a>
<img src="/images/dog.png">
"""

parser = ImageParser()
parser.feed(html)

print(images)
