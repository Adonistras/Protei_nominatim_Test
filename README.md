# Protei_nominatim_Test
Тестовое задание API nominatim для Protei

data_generators.py - для генерации 100 случайных мест по рандомным координатам 

services.py - вспомогательные функции

test_nominatim.py - основной файл для прогонки тестов.

Тестирование настроено для прогонки различных сгенерированных мест. 10% координат, при тестировании возвращают с точки зрения тестов
неверный результат из за географических погрешностей генерации. Также некоторые сгенерированные географические наименования при повторном запросе могут иначе называться,
различия в названиях - минимальны.
В тесте также настроены и негативные сценарии, включающие и проверку некоторых параметров апи запросов
