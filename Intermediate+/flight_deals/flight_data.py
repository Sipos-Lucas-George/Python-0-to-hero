class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, airline, out_date,
                 return_date, stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.airline = airline
        self.out_date = out_date
        self.return_date = return_date

        self.stop_overs = stop_overs
        self.via_city = via_city

    def __str__(self):
        return (f"Price: {self.price}€\n"
                f"From: {self.origin_city}\n"
                f"From Airport: {self.origin_airport}\n"
                f"To: {self.destination_city}\n"
                f"To Airport: {self.destination_airport}\n"
                f"Airline: {self.airline}\n"
                f"Out Date: {self.out_date}\n"
                f"Return Date: {self.return_date}\n") + ("" if self.stop_overs == 0 else
                                                         f"Stop Over: {self.stop_overs}\n"
                                                         f"Via City: {self.via_city}\n")
