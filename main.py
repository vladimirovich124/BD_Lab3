from mrjob.job import MRJob
from mrjob.step import MRStep

def get_airline_name(airline_code):
    airline_names = {
        "UA": "United Air Lines Inc.",
        "AA": "American Airlines Inc.",
        "US": "US Airways Inc.",
        "F9": "Frontier Airlines Inc.",
        "B6": "JetBlue Airways",
        "OO": "Skywest Airlines Inc.",
        "AS": "Alaska Airlines Inc.",
        "NK": "Spirit Air Lines",
        "WN": "Southwest Airlines Co.",
        "DL": "Delta Air Lines Inc.",
        "EV": "Atlantic Southeast Airlines",
        "HA": "Hawaiian Airlines Inc.",
        "MQ": "American Eagle Airlines Inc.",
        "VX": "Virgin America",
    }

    return airline_names.get(airline_code, "Unknown Airline")


class FlightDelayAnalysis(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        if len(fields) >= 12:
            airline_code = fields[4]
            departure_delay = fields[11]
            if departure_delay:
                try:
                    departure_delay = float(departure_delay)
                    absolute_delay = abs(departure_delay)
                    airline_name = get_airline_name(airline_code)
                    yield airline_code, (airline_name, absolute_delay)
                except ValueError:
                    pass

    def reducer_init(self):
        self.airline_stats = {}

    def reducer(self, airline_code, delay_values):
        total_delay = 0
        count = 0
        airline_name = None

        for name, delay in delay_values:
            airline_name = name
            total_delay += delay
            count += 1
        average_delay = total_delay / count
        self.airline_stats[airline_code] = (airline_name, average_delay)

    def reducer_final(self):
        top_airlines = sorted(self.airline_stats.items(), key=lambda x: x[1][1], reverse=True)[:5]

        print("{:<15} {:<40} {:<15}".format("Airline Code", "Airline Name", "Average Delay"))
        for airline_code, (airline_name, average_delay) in top_airlines:
            print("{:<15} {:<40} {:<15}".format(airline_code, airline_name, average_delay))

    def steps(self):
        return [
            MRStep(mapper=self.mapper),
            MRStep(reducer_init=self.reducer_init, reducer=self.reducer, reducer_final=self.reducer_final)
        ]


if __name__ == '__main__':
    FlightDelayAnalysis.run()
