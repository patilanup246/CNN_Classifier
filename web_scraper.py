import config

from google_images_download import google_images_download
import os


### WEB SCRAPE ###

# Search Terms
keywords_a = ",".join(config.search_terms_a)
keywords_b = ",".join(config.search_terms_b)

# Instantiate Class
response = google_images_download.googleimagesdownload()

# Define Output Directory
output_dir_a = os.path.join(config.data_path, config.search_terms_a[0])
output_dir_b = os.path.join(config.data_path, config.search_terms_b[0])

# Insert Variables into Arguments
arguments_a = {"keywords": keywords_a,
               "limit": config.scrape_limit,
               "format": config.file_format,
               "output_directory": output_dir_a,
               "no_directory": True,
               "no_numbering": True}
arguments_b = {"keywords": keywords_b,
               "limit": config.scrape_limit,
               "format": config.file_format,
               "output_directory": output_dir_b,
               "no_directory": True,
               "no_numbering": True}

# Execute Web Scrape
response.download(arguments_a)
response.download(arguments_b)
