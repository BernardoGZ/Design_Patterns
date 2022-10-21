# from patterns.csv_utils import Ride #SOLID Bad practice


def create_content(rides):
    builder = [_create_headers("Taxi Report"), _create_table_headers()]
    for ride in rides:
        builder.append(_add_ride(ride))

    return "".join(builder)


def create_file(content: str):
    with open("financial-report.txt", "w") as file:
        file.write(content)


def _create_headers(title: str):
    return f"{title}"


def _create_table_headers():
    return """
\nTaxiID \t\tPickup time \t\t\tDropoff time \t\t\tPassenger count \t\tTrip Distance \t\tTotal amount
    """


def _add_ride(ride):
    return "".join([
        "\n",
        f"{ride.taxi_id}\t",
        f"\t{ride.pick_up_time.isoformat()}\t",
        f"\t{ride.drop_of_time.isoformat()}\t",
        f"\t{ride.passenger_count}\t",
        f"\t{ride.trip_distance}\t",
        f"\t{_format_amount(ride.tolls_amount)}\t",
        "\n"
    ])


def _format_amount(amount):
    if amount < 0:
        return f"({amount})"
    return str(amount)