import os
import requests
from zipfile import ZipFile
from io import BytesIO

def download_fontawesome():
    # Create directories if they don't exist
    os.makedirs('static/vendor/fontawesome/css', exist_ok=True)
    os.makedirs('static/vendor/fontawesome/webfonts', exist_ok=True)

    # Download Font Awesome
    url = 'https://use.fontawesome.com/releases/v6.4.2/fontawesome-free-6.4.2-web.zip'
    response = requests.get(url)
    
    if response.status_code == 200:
        # Extract the zip file
        with ZipFile(BytesIO(response.content)) as zip_file:
            # Extract CSS files
            css_files = [f for f in zip_file.namelist() if f.endswith('.css') and '/css/' in f]
            for css_file in css_files:
                filename = os.path.basename(css_file)
                with zip_file.open(css_file) as source, open(f'static/vendor/fontawesome/css/{filename}', 'wb') as target:
                    target.write(source.read())
            
            # Extract webfonts
            webfonts = [f for f in zip_file.namelist() if '/webfonts/' in f]
            for font in webfonts:
                filename = os.path.basename(font)
                if filename:  # Skip directory entries
                    with zip_file.open(font) as source, open(f'static/vendor/fontawesome/webfonts/{filename}', 'wb') as target:
                        target.write(source.read())
        
        print("Font Awesome files downloaded and extracted successfully!")
    else:
        print("Failed to download Font Awesome")

if __name__ == '__main__':
    download_fontawesome() 