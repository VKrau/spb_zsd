# spb_zsd
python travel_calс.py --orig latitude,longitude --dest latitude,longitude --avoid tolls,highways 
	где --orig (обязательный параметр) - координаты точки отправления (точка А);
		--dest (обязательный параметр) - координаты точки назначения (точка Б);
		--avoid (необязательный параметр) - исключить (параметры перечислять через запятую без пробелов): tolls - платные участки, highways - шоссе, ferries - паромные переправы, indoor - ?
Пример вызова из командной строки:
python travel_calc.py --orig 59.97241,30.2133597 --dest 59.9177427,30.2103535 --avoid tolls,highways

Пример вызова функции:
start_calc("59.97241,30.2133597", "59.9177427,30.2103535", "tolls,highways")