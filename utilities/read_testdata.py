import json

class Read_testdata:
    # Class to read test data from a JSON file.

    @staticmethod
    def load_data():
        # Loads the JSON file into a dictionary.
        with open("C:/PythonProject2/test_data/testdata.json", "r") as file:
            return json.load(file)

    # READING THE TEST DATAS FOR HOME PAGE
    @staticmethod
    def get_home_page_data():
        # Fetches all data for the home page.
        data = Read_testdata.load_data()
        return data.get("home_page", {})

    @staticmethod
    def get_value(key):
        # Fetches a specific key value from home page data.
        return Read_testdata.get_home_page_data().get(key, "")
