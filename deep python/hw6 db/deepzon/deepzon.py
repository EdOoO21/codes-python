import mongomock


class OrderDB:
    def __init__(self, db_name: str = "orders") -> None:
        client: mongomock.MongoClient = mongomock.MongoClient()
        self.db = client[db_name]
        self.orders = self.db["orders"]

    """
    Описание документа

    order_id -- идентификатор заказа
    customer_name -- имя клиента, оформившего заказ
    product -- наименование продукта, который заказан (строка!)
    quantity -- кол-во заказанного товара
    status -- текущий статус заказа
    price -- цена единицы товара
    """

    # !!! для большего погружения, откройте файлик с тестами
    #  и посмотрите что должно происходить!!

    def add_order(
            self,
            order_id: int,
            customer_name: str,
            product: str,
            quantity: int,
            status: str,
            price: float) -> None:
        self.orders.insert_one({
            "order_id": order_id,
            "customer_name": customer_name,
            "product": product,
            "quantity": quantity,
            "status": status,
            "price": price
        })

    def get_order_by_id(self, order_id: int):
        """
        Получить заказ по order_id
        """
        return self.orders.find_one({"order_id": order_id})

    def update_order_status(self, order_id: int, new_status: str) -> None:
        """
        Обновить статус заказа
        """
        self.orders.update_one({"order_id": order_id}, {
            "$set": {"status": new_status}})

    def get_orders_by_customer(self, customer_name: str):
        """
        Получить заказ по заказчику
        """
        return self.orders.find_one({"customer_name": customer_name})

    def delete_order(self, order_id: int) -> None:
        """
        Удалить заказ по ID
        """
        self.orders.delete({"order_id": order_id})

    def update_order_quantity(self, order_id: int, new_quantity: int) -> None:
        """
        Обновляем количество товара в заказе.
        """
        self.orders.update_one({"order_id": order_id}, {
                               "$set": {"quantity": new_quantity}})

    def get_all_orders(self):
        """
        Возвращаем все заказы в коллекции.
        """
        return [x for x in self.orders.find()]

    def get_orders_by_status(self, status: str):
        """
        Возвращаем заказы с указанным статусом.
        """
        return [x for x in self.orders.find({"status": status})]

    def count_orders_by_customer(self, customer_name: str) -> int:
        """
        Возвращаем количество заказов для указанного клиента.
        """
        return len([1 for x in self.orders.find(
            {"customer_name": customer_name})])

    def get_total_quantity_by_customer(self, customer_name: str) -> int:
        """
        Возвращаем общее количество товаров, заказанных клиентом
        """
        orders = self.orders.find({"customer_name": customer_name})
        return sum([x["quantity"] for x in orders])

    def delete_orders_by_status(self, status: str) -> None:
        """
        Удаляеем все заказы с указанным статусом
        """
        self.orders.delete_many({"status": status})

    def get_total_quantity_per_customer(self):
        """
        Возвращать общее количество товаров, заказанных каждым клиентом
        """
        d = dict()
        for x in self.orders.find():
            try:
                d[x["customer_name"]] += x["quantity"]
            except KeyError:
                d[x["customer_name"]] = x["quantity"]

        ans = [{} for _ in range(len(d))]
        for k, x in enumerate(d.items()):
            ans[k] = {"_id": x[0], "total_quantity": x[1]}
        return ans

    def get_total_sales_by_product(self):
        """
        Возвращать общую сумму продаж для каждого продукта
        """
        d = dict()
        for x in self.orders.find():
            try:
                d[x["product"]] += (x["price"] * x["quantity"])
            except KeyError:
                d[x["product"]] = (x["price"] * x["quantity"])

        ans = [{} for _ in range(len(d))]
        for k, x in enumerate(d.items()):
            ans[k] = {"_id": x[0], "total_sales": x[1]}
        return ans

    def get_average_order_value_per_customer(self):
        """
        Возвращаем среднюю стоимость заказа для каждого клиента
        """
        d = dict()
        for x in self.orders.find():
            try:
                num = d[x["customer_name"]][0] + (x["quantity"] * x["price"])
                d[x["customer_name"]] = [num, d[x["customer_name"]][1] + 1]
            except KeyError:
                d[x["customer_name"]] = [x["quantity"] * x["price"], 1]
        ans = [{} for _ in range(len(d))]
        for k, x in enumerate(d.items()):
            ans[k] = {"_id": x[0], "average_order_value": x[1][0] / x[1][1]}
        return ans

    def get_order_count_by_status(self):
        """
        Возвращаем количество заказов в каждом статусе!
        """
        d = dict()
        for x in self.orders.find():
            try:
                d[x["status"]] += 1
            except KeyError:
                d[x["status"]] = 1

        ans = [{} for _ in range(len(d))]
        for k, x in enumerate(d.items()):
            ans[k] = {"_id": x[0], "order_count": x[1]}

        return ans

    def get_highest_quantity_order(self):
        """
        Возвращаем заказ с наибольшим количеством товаров
        """
        maxv = [-1, 0]
        for x in self.orders.find():
            if x["quantity"] > maxv[0]:
                maxv[0] = x["quantity"]
                maxv[1] = x
        return maxv[1]
