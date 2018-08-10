# spb_zsd
`python travel_calс.py --orig latitude,longitude --dest latitude,longitude --avoid tolls,highways`

#### Где:
* --orig (обязательный параметр) - координаты точки отправления (точка А);
* --dest (обязательный параметр) - координаты точки назначения (одна или несколько точек);
* --file (обязательный параметр) - указывает на файл с координатами;
* --avoid (необязательный параметр) - исключить (параметры перечислять через запятую без пробелов): tolls - платные участки, highways - шоссе, ferries - паромные переправы, indoor - ?

#### Дополнительные поддерживаемые параметры:
* --traffic_model (необязательный параметр) - определяет модель трафика при расчета времени проезда (best_guess (default), optimistc, pessimistic). Чтобы параметр работал корректно, необходимо использовать с параметром --key;
* --query_time (необязательный параметр)- время, когда запрос будет выполнен;
* --duration (необязательный параметр)- продолжительность мониторинга в часах;
* --key (необязательный параметр) - уникальный идентификационный ключ для работы с Google Maps API.
	
## Пример вызова из командной строки (с указанием координат):
`python cmdrunner.py --orig 59.97241,30.2133597 --dest 59.9177427,30.2103535 --avoid tolls,highways`
#### или
`python cmdrunner.py --file coord.csv`

## Пример вызова из командной строки (с указанием адресов или наименований точек):
`python cmdrunner.py --orig Saint-Petersburg+Birzhevaya+14 --dest London+Ye+Olde+Chesihire+Cheese+Pub`

## Пример вызова метода:
#### Первоначально создаем экземпляр объекта:
`runner = travel_calc.TravelCalculate()`

# Пример вызова метода с указанием файла координат будет выглядеть следующим образом:
`runner.calculate_from_file("coord.csv", ["", "tolls"], [17, 18, 19], duration=8)`

#### Где:
* ["", "tolls"]: "" - запрос без ограничений; "tolls" - запрос с исключением проезда по платным участкам, т.е. в указанное время будет выполнено 2 запроса: первый - запрос без ограничений, второй - исключая платные участки дорог. Если необходимо в одном запросе учесть сразу несколько условий, например, исключить проезд по платным участкам дорог и шоссе, то необходимо в кавычках перечислить их через запятую: ["tolls,highways"]
* [17, 18, 19]: параметр query_time (время, когда будут выполняться запросы);
* duration=8: параметр duration (продолжительность работы скрипта в часах);

# Пример вызова метода из коммандной строки будет выглядеть следующим образом:
`runner.calculate_from_file("59.97241,30.2133597","59.9177427,30.2103535", avoid tolls, [17, 18, 19], duration=8)`