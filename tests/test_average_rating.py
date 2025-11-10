from reports.average_rating import average_rating_report 

def test_average_rating_report_basic():
    rows = [
        {"brand": "apple", "rating": "4.9"},
        {"brand": "samsung", "rating": "4.8"},
        {"brand": "apple", "rating": "5.0"},  
    ]
    result = average_rating_report(rows)
    assert result[0][0] == "apple"           
    assert round(result[0][1], 2) == 4.95    

def test_average_rating_report_handles_invalid():
    rows = [
        {"brand": "apple", "rating": "4.9"},
        {"brand": "apple", "rating": "invalid"},  
    ]
    result = average_rating_report(rows)
    assert result == [("apple", 4.9)]  
