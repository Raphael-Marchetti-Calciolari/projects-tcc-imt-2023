import csv
import json

class DataImporter:
    def __init__(self, csv_data_path:str, write_out_json_data=False) -> None:
        self.path = csv_data_path
        self.json_data = self.__read_data(self.path, write_out_json_data)
        print(json.dumps(self.json_data, indent=4, ensure_ascii=True))

    def __read_data(self, csv_path:str, write_out):
        with open(csv_path, encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            headers = next(reader)
            headers = [
                header
                .replace("\u00baC", "Celsius")
                .replace(" ", "_")
                .replace("[", "")
                .replace("]", "")
                for header in headers
            ]
            data = [dict(zip(headers, row)) for row in reader]
        if (write_out):
            with open('./data.json', 'w') as outfile:
                json.dump(data, outfile)
        return json.dumps(data)

path = '../data/Dados-tratados/Ensaio_01_data_1308.csv'
DataImporter(path, True)