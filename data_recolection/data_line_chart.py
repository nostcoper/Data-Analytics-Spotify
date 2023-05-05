def trigger_popularity_list(tracks: dict) -> list:
    names = []
    popularity = []
    items = tracks['items'] 
    for item in items:
        names.append(item['name'])
        popularity.append(item['popularity'])
    return names, popularity
