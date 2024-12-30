
import scrapy
from urllib.parse import urljoin

class NamesSpider(scrapy.Spider):
    name = 'names'
    start_urls = ['https://www.nepaliname.com/']
    
    def parse(self, response):
        # Create base URL for alphabet pages
        base_url = "https://www.nepaliname.com/newarinames#Girl"
        
        # Define all alphabets in order
        alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        # Create URLs for each alphabet in order
        for alphabet in alphabets:
            url = urljoin(base_url, f"{alphabet}-Girl")
            yield scrapy.Request(
                url,
                callback=self.parse_names_page,
                meta={'alphabet': alphabet}  # Pass alphabet information
            )
    
    def parse_names_page(self, response):
        # Get current alphabet from meta
        current_alphabet = response.meta['alphabet']
        
        # Extract names and descriptions
        rows = response.css('table.baby-names-contains tr')
        for row in rows:
            name = row.css('td[rel="tooltip"] a::text').get()
            description = row.css('td.hidden-xs::text').get()
            
            if name and description:  # Only yield if both name and description exist
                yield {
                    'alphabet': current_alphabet,
                    'name': name.strip(),
                    'description': description.strip()
                }