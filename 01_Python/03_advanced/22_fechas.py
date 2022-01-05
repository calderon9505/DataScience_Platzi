import datetime
import pytz

print('Fecha y hora:', datetime.datetime.now())
print('Fecha:', datetime.date.today())
print('Mes:', datetime.date.today().month)
print('Fecha y hora UTC:', datetime.datetime.utcnow())
print('Fecha y hora formato feo:', datetime.date.today().strftime('%m/%d/%Y'))

# pytz: módulo para trabajar con zonas horarias
bogota_timezone = pytz.timezone('America/Bogota')
bogota_datetime = datetime.datetime.now(bogota_timezone)
print('\nBogota:', bogota_datetime) # Bogota: 2022-01-03 14:53:08.205470-05:00

mexico_timezone = pytz.timezone('America/Mexico_City')
mexico_time = datetime.datetime.now(mexico_timezone)
print("México:", mexico_time)

caracas_timezone = pytz.timezone('America/Caracas')
caracas_time = datetime.datetime.now(caracas_timezone)
print("Caracas:", caracas_time)