import json
import os
import requests
import img2pdf

def create_directory(directory):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_data():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    base_url = 'https://recordpower.co.uk/flip/Winter2020/files/mobile/'
    output_dir = 'img'

    # Create the output directory
    create_directory(output_dir)

    link_list = []
    for i in range(1, 48):
        url = f'{base_url}{i}.jpg'
        try:
            req = requests.get(url=url, headers=headers)
            response = req.content

            filename = os.path.join(output_dir, f'{i}.jpg')
            with open(filename, 'wb') as file:
                file.write(response)
            link_list.append(filename)
            print(f'Downloaded {filename}')
        except Exception as e:
            print(f'Error downloading {url}: {str(e)}')

    pdf_filename = os.path.join(output_dir, 'result.pdf')
    try:
        with open(pdf_filename, 'wb') as file:
            file.write(img2pdf.convert(link_list))
        print(f'PDF created successfully: {pdf_filename}')
    except Exception as e:
        print(f'Error creating PDF: {str(e)}')

def main():
    get_data()

if __name__ == '__main__':
    main()
