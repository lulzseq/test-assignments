## 1. Задание на внешний сбор данных:
### Этап 1: Написать класс по работе с парсингом внешних данных
* Получить на вход страницу в виде:
https://www.ozon.ru/product/kapsulnaya-kofemashina-krups-piccolo-xs-krasnyy-178842724/?sh=yr-vOjksrA
https://www.wildberries.ru/catalog/18256273/detail.aspx?targetUrl=MI
https://market.yandex.ru/offer/gXBC9f3VsTCE8tua_dKwkA?cpa=1&onstock=1
* Сделать парсинг вводимой страницы
### Этап 2: Матчинг
* Получить из БД мастер товар
* К мастеру товару добавить матчинг (добавление товара из ссылки и введение всех данных)
### Этап 3: Интеллектуальный поиск
* Получить из БД товар
* Найти этот товар на площадках
* Найти по нему параметры
* Внести в БД

## 2. Задание на внутренний сбор данных:
### Этап 1: Написать класс по работе с API Озон
Есть API Озон. Метод получения списка акций.
https://api-seller.ozon.ru/v1/actions
* Получить все акции
* Получить все товары доступные для акций
https://api-seller.ozon.ru/v1/actions/candidates
* Получить условия для добавления товаров в акции (обсудить с куратором)
* Добавить товары в акции подходящие под условия
https://api-seller.ozon.ru/v1/actions/products/deactivate

### Этап 2: Сформировать историю (логирование действий)
* В предоставленной БД сделать запись действий.

### Этап 3: Формировать интеллектуальный модуль для работы с добавлением в акции
* Обсудить с куратором

### Этап 4: в предоставленной БД сделать анализ участия в акциях на других площадках
* Обсудить с куратором