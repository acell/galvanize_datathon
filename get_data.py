import pandas as pd
import requests
import zipfile
import io


def extract_zip_files(zip_url, directory):
    request = requests.get(zip_url)
    zip_content = zipfile.ZipFile(io.BytesIO(request.content))
    zip_content.extractall(f"data/{directory}/")


def download_csvs():
    for year in range(2009, 2022):
        for month in range(1, 13):
            year = str(year)
            month = str(month)

            if len(month) == 1:
                month = '0' + month

            if pd.Timestamp(year + '-' + month) > pd.Timestamp.now():
                return

            scheduled_outage_zip_url = f"http://mis.nyiso.com/public/csv/schedlineoutages/{year}{month}01SCLineOutages_csv.zip"
            real_time_outage_zip_url = f"http://mis.nyiso.com/public/csv/realtimelineoutages/{year}{month}01RTLineOutages_csv.zip"
            load_forecast_zip_url = f"http://mis.nyiso.com/public/csv/isolf/{year}{month}01isolf_csv.zip"
            load_real_time_zip_url = f"http://mis.nyiso.com/public/csv/pal/{year}{month}01pal_csv.zip"
            weather_zip_url = f"http://mis.nyiso.com/public/csv/lfweather/{year}{month}01lfweather_csv.zip"

            directories = ['scheduled_outages', 'real_time_outages', 'forecast_load', 'real_time_load', 'weather']
            urls = [scheduled_outage_zip_url, real_time_outage_zip_url, load_forecast_zip_url,
                    load_real_time_zip_url, weather_zip_url]

            for n in range(len(directories)):
                extract_zip_files(urls[n], directories[n])


def create_dfs(directories):
    dfs = {}
    scheduled_outage_csv = "SCLineOutages.csv"
    real_time_outage_csv = "RTLineOutages.csv"
    forecast_load_csv = "isolf.csv"
    real_time_load_csv = "pal.csv"
    weather_csv = "lfweather.csv"
    csvs = [scheduled_outage_csv, real_time_outage_csv, forecast_load_csv, real_time_load_csv, weather_csv]

    for n in range(len(directories)):
        directory = directories[n]
        df_days = []

        for year in range(2009, 2022):
            for month in range(1, 13):
                for day in range(1, 32):
                    year = str(year)
                    month = str(month)
                    day = str(day)

                    if len(month) == 1:
                        month = '0' + month

                    if len(day) == 1:
                        day = '0' + day

                    try:
                        file = pd.read_csv(f"data/{directory}/{year}{month}{day}{csvs[n]}")
                        df_days.append(file)
                    except:
                        pass

        df_days = pd.concat(df_days, ignore_index=True)
        dfs[directory] = df_days
    return dfs
