from bing_image_downloader.downloader import download

queries=[
        'Adzuki Beans', 'Black Gram', 'Chickpeas', 'Dew Bean', 'Green Chickpeas', 'Green Gram',
        'Pinto Beans', 'Red Kidney Beans', 'Red Lentils', 'Split & Skinned Black Gram', 'Split Black Gram',
        'Split Green Gram', 'White Kidney Beans', 'Yellow Lentils'
        ]

for query in queries:
    download(query.lower()+' images', limit=1000,
                        adult_filter_off=True, force_replace=False)
