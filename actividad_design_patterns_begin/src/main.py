from patterns import csv_utils, web_report, print_report, simple_factory

CSV_FILE = "taxi-data.csv"

def main():
    rides = csv_utils.parse_file(CSV_FILE)
    simple_factory.get_product("text", rides)
    simple_factory.get_product("web", rides)

if __name__ == '__main__':
    main()
