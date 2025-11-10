from collections import defaultdict


def average_rating_report(rows):
    brand_ratings = defaultdict(list)
    
    for row in rows:
        brand = row.get("brand", "").strip()
        try:
            rating = float(row.get("rating", 0))
        except ValueError:
            continue
        if brand:
            brand_ratings[brand].append(rating)

    report_data = []
    for brand, ratings in brand_ratings.items():
        avg = sum(ratings) / len(ratings)
        report_data.append((brand, round(avg, 2)))

    report_data.sort(key=lambda x: x[1], reverse=True)
    return report_data
