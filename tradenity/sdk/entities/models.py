import bcrypt
from booby import Model, fields
from .base import BaseEntity


class Address(BaseEntity):
    streetLine1 = fields.String()
    streetLine2 = fields.String()
    city = fields.String()
    state = fields.String()
    zipCode = fields.String()
    country = fields.String()
    updatedAt = fields.String()
    createdAt = fields.String()


class Brand(BaseEntity):
    RESOURCE_NAME = 'brands'
    name = fields.String()
    title = fields.String()
    status = fields.String()
    description = fields.String()
    updatedAt = fields.String()
    createdAt = fields.String()


class Category(BaseEntity):
    RESOURCE_NAME = 'categories'
    name = fields.String()
    title = fields.String()
    status = fields.String()
    description = fields.String()
    updatedAt = fields.String()
    createdAt = fields.String()
    depth = fields.Integer()
    position = fields.Integer()


class Gateway(BaseEntity):
    RESOURCE_NAME = 'gateways'
    name = fields.String()
    title = fields.String()
    status = fields.String()
    description = fields.String()
    mode = fields.String()
    accountId = fields.String()
    secretKey = fields.String()
    publicKey = fields.String()
    testSecretKey = fields.String()
    testPublicKey = fields.String()
    updatedAt = fields.String()
    createdAt = fields.String()
    _links = fields.List()


class Currency(BaseEntity):
    RESOURCE_NAME = 'currencies'
    code = fields.String()
    title = fields.String()
    status = fields.String()
    exchangeRate = fields.Float()
    createdAt = fields.String()
    updatedAt = fields.String()


class Photo(Model):
    createdAt = fields.String()
    updatedAt = fields.String()
    name = fields.String()
    url = fields.String()


class Weight(BaseEntity):
    unit = fields.String()
    amount = fields.Float()


class Product(BaseEntity):
    RESOURCE_NAME = 'products'
    name = fields.String()
    title = fields.String()
    status = fields.String()
    description = fields.String()
    shortDescription = fields.String()
    fullDescription = fields.String()
    specifications = fields.String()
    sku = fields.String()
    stockLevel = fields.Integer()
    minimumStockLevel = fields.Integer()
    hasSellLimit = fields.Boolean()
    maximumSellCount = fields.Integer()
    stockStatus = fields.String()
    price = fields.Float()
    updatedAt = fields.String()
    createdAt = fields.String()
    mainPhoto = fields.Embedded(Photo)
    itemWeight = fields.Embedded(Weight)
    packageWeight = fields.Embedded(Weight)
    requireShipping = fields.Boolean()
    photos = fields.Collection(Photo)
    _links = fields.List()

    @classmethod
    def find_all_by_brand(cls, brand):
        if isinstance(brand, str) or isinstance(brand, unicode):
            return cls._search(brand=brand)
        else:
            return cls._search(brand=brand.id)

    @classmethod
    def find_all_by_category(cls, category):
        if isinstance(category, str) or isinstance(category, unicode):
            return cls._search(category=category)
        else:
            return cls._search(category=category.id)


class Collection(BaseEntity):
    RESOURCE_NAME = 'collections'
    name = fields.String()
    title = fields.String()
    status = fields.String()
    description = fields.String()
    updatedAt = fields.String()
    createdAt = fields.String()
    products = fields.Collection(Product)

    @classmethod
    def find_by_name(cls, name):
        results = cls._search(name=name)
        if results.content is not None and len(results.content) > 0:
            return results.content[0]


class LineItem(Model):
    _links = fields.Embedded(dict)
    id = fields.String()
    quantity = fields.Integer()
    product = fields.Embedded(Product)
    unitPrice = fields.Float()
    subtotal = fields.Float()
    total = fields.Float()
    taxes = fields.Float()
    shippingCost = fields.Float()


class ShoppingCart(BaseEntity):
    RESOURCE_NAME = 'shoppingCarts'
    _links = fields.Embedded(dict)
    count = fields.Integer()
    total = fields.Float()
    items = fields.Collection(LineItem)

    @classmethod
    def get(cls):
        result = cls.client().get(cls.resource_base_path())
        return cls(**result.json())

    @classmethod
    def add(cls, product, quantity=1):
        result = cls.client().post(cls.resource_base_path(), data={"product": product, "quantity": quantity})
        return cls(**result.json())

    # todo implement
    @classmethod
    def remove(cls, item_id):
        result = cls.client().delete("{base}/{id}".format(base=cls.resource_base_path(), id=item_id))
        return cls(**result.json())


class Customer(BaseEntity):
    RESOURCE_NAME = 'customers'
    WRITABLE_FIELDS = ["firstName", "lastName", "email", "username", "password"]
    ALL_FIELDS = WRITABLE_FIELDS + ["status", "createdAt", "updatedAt"]
    _links = fields.Embedded(dict)
    firstName = fields.String()
    lastName = fields.String()
    email = fields.String()
    username = fields.String()
    password = fields.String()
    status = fields.String()
    updatedAt = fields.String()
    createdAt = fields.String()

    def is_valid_password(self, password):
        return bcrypt.hashpw(str(password), str(self.password)) == str(self.password)

    @classmethod
    def find_by_username(cls, username):
        return cls._search(username=username).first


class Order(BaseEntity):
    RESOURCE_NAME = 'orders'
    _links = fields.Embedded(dict)
    count = fields.Integer()
    total = fields.Float()
    subtotal = fields.Float()
    shippingCost = fields.Float()
    items = fields.Collection(LineItem)
    customer = fields.Embedded(Customer)
    billingAddress = fields.Embedded(Address)
    shippingAddress = fields.Embedded(Address)
    status = fields.String()
    updatedAt = fields.String()
    createdAt = fields.String()
    purchasedAt = fields.String()
    completedAt = fields.String()

    @classmethod
    def find_all_by_customer(cls, customer):
        return cls._search(customer=customer)

    def _get_create_data(self):
        data = {"customer": self.customer.id}
        data.update(self.billingAddress.as_dict(prefix="billingAddress."))
        data.update(self.shippingAddress.as_dict(prefix="shippingAddress."))
        return data

    def checkout(self, paymentSource):
        data = self._get_create_data()
        data['paymentSource'] = paymentSource
        result = self.client().post(self.resource_base_path(), data=data)
        return Transaction(**result.json())

    @classmethod
    def refund(cls, order_id):
        url = "orders/{id}/refund".format(id=order_id)
        result = cls.client().post(url, data={})
        return Transaction(**result.json())


class Tax(BaseEntity):
    RESOURCE_NAME = 'taxes'
    name = fields.String()
    title = fields.String()
    status = fields.String()
    description = fields.String()
    updatedAt = fields.String(name="updatedAt")
    createdAt = fields.String(name="createdAt")


class Transaction(BaseEntity):
    RESOURCE_NAME = 'transactions'
    type = fields.String()
    status = fields.String()
    gatewayOperationId = fields.String()
    order = fields.Embedded(Order)
    gateway = fields.Embedded(Gateway)
    updatedAt = fields.String(name="updatedAt")
    createdAt = fields.String(name="createdAt")
    _links = fields.List()



