import os
import pandas as pd
from datetime import datetime
import math

class DataDiggestor:
	def _get_list_of_humidities(self, df: pd.DataFrame):
		humidities = []
		columns = list(df.columns)
		for col in columns:
				current_line = (df[df[col] == '-']).reset_index(drop=True)
				if (len(current_line) != 0): 
					idx = columns.index(col) + 2
					if (idx > len(columns) - 1): continue
					humidities.append(float(current_line.iloc[0, idx]))
				else:
					current_line = (df[df[col].str.contains('\*') == True]).reset_index(drop=True)
					if (len(current_line) == 0): continue
					value = current_line.iloc[0, columns.index(col)]
					humidity = float(value.replace(' ', '')[9:])
					humidities.append(humidity)			

		return humidities

	def _get_humidity_levels(self, df: pd.DataFrame):
		humidities = self._get_list_of_humidities(df)
		h_len = len(humidities)
		if (h_len > 0):
			total = math.fsum(humidities)
			return round(total/h_len, 6)

	def _get_time_in_seconds(self, time_object: datetime):
		return time_object.hour * 3600 + time_object.minute * 60 + time_object.second + time_object.microsecond / 1e6

	def _convert_time_column_to_relative_seconds(self, df:pd.DataFrame, time_column_name='Time'):
		time_col = df[time_column_name].copy()
		for i, time in enumerate(time_col):
			try: time_obj = datetime.strptime(str(time), '%Y-%m-%d %H:%M:%S.%f')
			except:	time_obj = datetime.strptime(str(time), '%Y-%m-%d %H:%M:%S')
			time_col[i] = float(self._get_time_in_seconds(time_obj))
		time_col = time_col - time_col.min()
		response = df.copy()
		response[time_column_name] = pd.to_numeric(time_col)
		return response

	def _get_closest_line(self, target_in_seconds:float, df:pd.DataFrame, time_in_seconds_column_name='Time'):
		abs_diff = abs(df[time_in_seconds_column_name] - target_in_seconds)
		min_index = abs_diff.idxmin()
		return min_index

	def diggest_files_into_single_dataframe(self, data_path:str):
		data_df = pd.DataFrame()
		final_df = pd.DataFrame()

		for filename in os.listdir(data_path):
			f = os.path.join(data_path, filename)
			if os.path.isfile(f):
				essay_number = f.split('\\')[1].split('E')[1][0:2]
				if (filename.startswith('E')):
					df = pd.read_excel(f)
					df = self._convert_time_column_to_relative_seconds(df)
					data_df = df.copy()

				if (filename.startswith('U')):
					time = int(filename[5:filename.find('_min')]) * 60
					closest_line = self._get_closest_line(time, data_df)

					df = pd.read_excel(f, dtype=str)
					humidity = self._get_humidity_levels(df)

					line = dict(data_df.loc[closest_line])
					line['Umidade Produto [%]'] = humidity
					line['Ensaio'] = int(essay_number)

					final_df = pd.concat([final_df, pd.DataFrame([line])], ignore_index=True)

		return final_df