# Create a Factory method for Reports generation

from patterns import print_report, web_report


def get_product(report_type: str, rides):
    if report_type == "web":
        web_report.create_file(web_report.create_content(rides))
    elif report_type == "text":
        print_report.create_file(print_report.create_content(rides))
    else:
        raise Exception("Report type unknown")