# spb_zsd

	python travel_calс.py --orig latitude,longitude --dest latitude,longitude --avoid tolls,highways 
где:
	--orig (обязательный параметр) - координаты точки отправления (точка А);
	--dest (обязательный параметр) - координаты точки назначения (точка Б);
	--avoid (необязательный параметр) - исключить (параметры перечислять через запятую без пробелов): tolls - платные участки, highways - шоссе, ferries - паромные переправы, indoor - ?
дополнительные поддерживаемые параметры:
	--traffic_model (необязательный параметр) - определяет модель трафика при расчета времени проезда (best_guess (default), optimistc, pessimistic). Чтобы параметр работал корректно, необходимо использовать с параметром --key
	--key (необязательный параметр) - уникальный идентификационный ключ для работы с Google Maps API
	Пример вызова из командной строки (с указанием координат):
	python travel_calc.py --orig 59.97241,30.2133597 --dest 59.9177427,30.2103535 --avoid tolls,highways

Пример вызова из командной строки (с указанием адресов или наименований точек):

	python travel_calc.py --orig Saint-Petersburg+Birzhevaya+14 --dest London+Ye+Olde+Chesihire+Cheese+Pub

Пример вызова функции:

	start_calc("59.97241,30.2133597", "59.9177427,30.2103535", "tolls,highways")