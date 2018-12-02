def csv_to_string():
    """
    Converts CSV file to strings for the rest API.

    :return: danger csv file and recent csv file as strings
    """
    with open("frontend_files\\danger_zones.csv") as f:
        danger_string = f.read() + "\n"

    with open("frontend_files\\recent_severe_crimes.csv") as f:
        recent_string = f.read() + "\n"

    return danger_string, recent_string