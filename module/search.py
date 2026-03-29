from module.storage import fetch_all

def search_data(keyword):
    data = fetch_all()
    results = []

    for row in data:
        if keyword.lower() in row[2].lower():
            results.append(row)

    return results
