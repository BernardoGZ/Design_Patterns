from patterns import csv_utils, web_report, print_report

CSV_FILE = "taxi-data.csv"


def main():
    rides = csv_utils.parse_file(CSV_FILE)
    html_report = web_report.create_content(rides)
    web_report.create_file(html_report)
    print_report.create_file(print_report.create_content(rides))



if __name__ == '__main__':
    main()
