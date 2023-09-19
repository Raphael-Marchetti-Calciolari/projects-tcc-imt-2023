import os
import pandas as pd
from datetime import datetime
import math

class EssayDataDiggestor:

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

	def _get_closest_time_line(self, target_in_seconds:float, df:pd.DataFrame, time_in_seconds_column_name='Time'):
		abs_diff = abs(df[time_in_seconds_column_name] - target_in_seconds)
		min_index = abs_diff.idxmin()
		return min_index

	def get_essay_number_from(self, filename:str):
		return int(filename.split('\\')[1].split('E')[1][0:2])

	def get_labeled_essays(self, data_path:str):
		essays_df = pd.DataFrame()
		final_df = pd.DataFrame()

		for dir_filename in os.listdir(data_path):
			filename = os.path.join(data_path, dir_filename)
			if os.path.isfile(filename):
				essay_number = self.get_essay_number_from(filename)

				if (dir_filename.startswith('E')): # Essay files
					df = pd.read_excel(filename)
					df = self._convert_time_column_to_relative_seconds(df)
					df['Ensaio'] = essay_number
					essays_df = pd.concat([essays_df, df.copy()]).reset_index(drop=True)

				if (dir_filename.startswith('U')): # Humidity files
					humidity_collected_time_in_seconds = int(dir_filename[5:dir_filename.find('_min')]) * 60
					current_essay = essays_df[essays_df['Ensaio'] == essay_number]
					closest_line = self._get_closest_time_line(humidity_collected_time_in_seconds, current_essay)

					df = pd.read_excel(filename, dtype=str)
					humidity = self._get_humidity_levels(df)

					current_humidity_essay_line = dict(essays_df.loc[closest_line])
					current_humidity_essay_line['Umidade Produto [%]'] = humidity
					current_humidity_essay_line['Ensaio'] = essay_number

					final_df = pd.concat([final_df, pd.DataFrame([current_humidity_essay_line])]).reset_index(drop=True)

		return final_df

	def get_essays(self, data_path:str):
		essays_df = pd.DataFrame()
		for dir_file in os.listdir(data_path):
			filename = os.path.join(data_path, dir_file)
			if os.path.isfile(filename):
				essay_number = self.get_essay_number_from(filename)
				if (dir_file.startswith('E')):
					df = pd.read_excel(filename)
					df = self._convert_time_column_to_relative_seconds(df)
					df['Ensaio'] = essay_number
					essays_df = pd.concat([essays_df, df.copy()]).reset_index(drop=True)

		return essays_df