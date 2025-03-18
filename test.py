from google import genai
from google.genai import types
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os


def get_website_content(url:str)->dict[str, str | list | int ]:
    """
    Takes a website URL as input and returns all the content from the website.

    Args:
        url (str): The URL of the website to scrape

    Returns:
        dict: A dictionary containing the title, text content, and links from the website
    """
    try:
        # Validate URL
        if not urlparse(url).scheme:
            url = 'https://' + url

        # Send GET request to the URL
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title
        title = soup.title.string if soup.title else "No title found"

        # Extract text content (excluding script and style elements)
        for script in soup(["script", "style"]):
            script.decompose()
        text_content = soup.get_text(separator='\n', strip=True)

        # Extract all links
        links = [a.get('href') for a in soup.find_all('a', href=True)]

        return {
            'title': title,
            'text_content': text_content,
            'links': links,
            'status_code': response.status_code
        }

    except requests.RequestException as e:
        return {
            'error': f"Error fetching the website: {str(e)}",
            'status_code': getattr(e.response, 'status_code', None)
        }



class Reporter:
    def __init__(self):
        self.reporter = genai.Client(api_key="AIzaSyCGRagRWD_XWzdlR6ZGgJfyeKZM6agwMw4")
        self.reporter_config = types.GenerateContentConfig(tools=[get_website_content])

    def research(self):
        prompt = """
        imagine you are a news reporter from a top organization. Your goal is to do a research using the below urls.
        then return a detailed report containg all the  headlines and the news.

        Urls of the websites :
        1.https://www.bbc.com/
        2.https://www.thehindu.com/news/
        3.https://timesofindia.indiatimes.com/
        4.https://edition.cnn.com/
        5.https://www.wired.com/
        6.https://techcrunch.com/
        """
        print("Starting the Research...")
        response = self.reporter.models.generate_content(
            model="gemini-2.0-flash", config=self.reporter_config, contents=f"{prompt}"
        )
        headlines = response.text
        print("Research Completed...")
        return headlines


class Organizer:
    def __init__(self):
        self.Organizer = genai.Client(api_key="AIzaSyCGRagRWD_XWzdlR6ZGgJfyeKZM6agwMw4")

    def Work(self, content):
        prompt = f"""
        You are an experienced website developer with a strong sense of design.
        Using the news provided below create a beautiful and visually apealling website.
        give it a good layout and use colors effectively.
        Also do not add any unessacarry broken links just keep it an infomrationsal site. 
       
        Be fully responsive for different screen sizes.
        
        Headlines: {content}
        
        Use the Full content do not leave anything please.
        Return just the code no explanations.
        Also what you will return will be the final site so do not add somthing incomeplete.
        🚨 Return only the complete website code (HTML, CSS, and JavaScript if needed).**
        """

        print("Got the Content. Analyzing..")

        response = self.Organizer.models.generate_content(
            model="gemini-2.0-flash", contents=f"{prompt}"
        )

        html = response.text
        html = html.replace("html", "", 1)
        html = html.replace("```", "")

        # Ensure static directory exists
        os.makedirs('static', exist_ok=True)
        
        # Save the file in the static directory
        with open("static/Final.html", 'w') as file:
            file.write(html)

        print("Completed")



#Employes
Ajay = Reporter()
Kenny = Organizer()


if __name__ == "__main__":
    #Workflow
    content = Ajay.research()
    print(content)
    Kenny.Work(content)





