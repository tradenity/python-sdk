# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


from __future__ import absolute_import

import re
import pprint

# python 2 and python 3 compatibility library
import six

from tradenity.api_client import ApiClient


class Product(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'slug': 'str',
        'model': 'str',
        'status': 'str',
        'type': 'str',
        'short_description': 'str',
        'full_description': 'str',
        'free_shipping': 'bool',
        'sku': 'str',
        'price': 'int',
        'cost_price': 'int',
        'retail_price': 'int',
        'sale_price': 'int',
        'manage_inventory': 'bool',
        'stock_level': 'int',
        'minimum_stock_level': 'int',
        'maximum_sell_count': 'int',
        'item_dimensions': 'Dimensions',
        'package_dimensions': 'Dimensions',
        'package_weight': 'Weight',
        'require_shipping': 'bool',
        'availability': 'str',
        'availability_date': 'date',
        'allow_pre_order': 'bool',
        'brand': 'Brand',
        'main_photo': 'Photo',
        'photos': 'list[Photo]',
        'files': 'list[StorageFile]',
        'promotions': 'list[Promotion]',
        'related_products': 'list[Product]',
        'stock_status': 'str',
        'categories': 'list[Category]',
        'tax_class': 'TaxClass',
        'option_set': 'OptionSet',
        'variants': 'list[Variant]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'slug': 'slug',
        'model': 'model',
        'status': 'status',
        'type': 'type',
        'short_description': 'shortDescription',
        'full_description': 'fullDescription',
        'free_shipping': 'freeShipping',
        'sku': 'sku',
        'price': 'price',
        'cost_price': 'costPrice',
        'retail_price': 'retailPrice',
        'sale_price': 'salePrice',
        'manage_inventory': 'manageInventory',
        'stock_level': 'stockLevel',
        'minimum_stock_level': 'minimumStockLevel',
        'maximum_sell_count': 'maximumSellCount',
        'item_dimensions': 'itemDimensions',
        'package_dimensions': 'packageDimensions',
        'package_weight': 'packageWeight',
        'require_shipping': 'requireShipping',
        'availability': 'availability',
        'availability_date': 'availabilityDate',
        'allow_pre_order': 'allowPreOrder',
        'brand': 'brand',
        'main_photo': 'mainPhoto',
        'photos': 'photos',
        'files': 'files',
        'promotions': 'promotions',
        'related_products': 'relatedProducts',
        'stock_status': 'stockStatus',
        'categories': 'categories',
        'tax_class': 'taxClass',
        'option_set': 'optionSet',
        'variants': 'variants'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, slug=None, model=None, status=None, type=None, short_description=None, full_description=None, free_shipping=None, sku=None, price=None, cost_price=None, retail_price=None, sale_price=None, manage_inventory=None, stock_level=None, minimum_stock_level=None, maximum_sell_count=None, item_dimensions=None, package_dimensions=None, package_weight=None, require_shipping=None, availability=None, availability_date=None, allow_pre_order=None, brand=None, main_photo=None, photos=None, files=None, promotions=None, related_products=None, stock_status=None, categories=None, tax_class=None, option_set=None, variants=None):
        """Product - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._slug = None
        self._model = None
        self._status = None
        self._type = None
        self._short_description = None
        self._full_description = None
        self._free_shipping = None
        self._sku = None
        self._price = None
        self._cost_price = None
        self._retail_price = None
        self._sale_price = None
        self._manage_inventory = None
        self._stock_level = None
        self._minimum_stock_level = None
        self._maximum_sell_count = None
        self._item_dimensions = None
        self._package_dimensions = None
        self._package_weight = None
        self._require_shipping = None
        self._availability = None
        self._availability_date = None
        self._allow_pre_order = None
        self._brand = None
        self._main_photo = None
        self._photos = None
        self._files = None
        self._promotions = None
        self._related_products = None
        self._stock_status = None
        self._categories = None
        self._tax_class = None
        self._option_set = None
        self._variants = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.slug = slug
        if model is not None:
            self.model = model
        self.status = status
        self.type = type
        if short_description is not None:
            self.short_description = short_description
        if full_description is not None:
            self.full_description = full_description
        if free_shipping is not None:
            self.free_shipping = free_shipping
        self.sku = sku
        self.price = price
        if cost_price is not None:
            self.cost_price = cost_price
        if retail_price is not None:
            self.retail_price = retail_price
        if sale_price is not None:
            self.sale_price = sale_price
        if manage_inventory is not None:
            self.manage_inventory = manage_inventory
        if stock_level is not None:
            self.stock_level = stock_level
        if minimum_stock_level is not None:
            self.minimum_stock_level = minimum_stock_level
        if maximum_sell_count is not None:
            self.maximum_sell_count = maximum_sell_count
        if item_dimensions is not None:
            self.item_dimensions = item_dimensions
        if package_dimensions is not None:
            self.package_dimensions = package_dimensions
        if package_weight is not None:
            self.package_weight = package_weight
        if require_shipping is not None:
            self.require_shipping = require_shipping
        if availability is not None:
            self.availability = availability
        if availability_date is not None:
            self.availability_date = availability_date
        if allow_pre_order is not None:
            self.allow_pre_order = allow_pre_order
        if brand is not None:
            self.brand = brand
        if main_photo is not None:
            self.main_photo = main_photo
        if photos is not None:
            self.photos = photos
        if files is not None:
            self.files = files
        if promotions is not None:
            self.promotions = promotions
        if related_products is not None:
            self.related_products = related_products
        if stock_status is not None:
            self.stock_status = stock_status
        self.categories = categories
        if tax_class is not None:
            self.tax_class = tax_class
        if option_set is not None:
            self.option_set = option_set
        if variants is not None:
            self.variants = variants

    @property
    def id(self):
        if self._id:
            return self._id
        elif self.meta is None:
            return None
        else:
            self._id = self.meta.href.split("/")[-1]
            return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def meta(self):
        """Gets the meta of this Product.


        :return: The meta of this Product.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Product.


        :param meta: The meta of this Product.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Product.


        :return: The name of this Product.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Product.


        :param name: The name of this Product.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Product.


        :return: The slug of this Product.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Product.


        :param slug: The slug of this Product.
        :type: str
        """

        self._slug = slug

    @property
    def model(self):
        """Gets the model of this Product.


        :return: The model of this Product.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Product.


        :param model: The model of this Product.
        :type: str
        """

        self._model = model

    @property
    def status(self):
        """Gets the status of this Product.


        :return: The status of this Product.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Product.


        :param status: The status of this Product.
        :type: str
        """
        allowed_values = ["enabled", "disabled"]
        if status is not None and status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """Gets the type of this Product.


        :return: The type of this Product.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Product.


        :param type: The type of this Product.
        :type: str
        """
        allowed_values = ["digital", "physical"]
        if type is not None and type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def short_description(self):
        """Gets the short_description of this Product.


        :return: The short_description of this Product.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this Product.


        :param short_description: The short_description of this Product.
        :type: str
        """

        self._short_description = short_description

    @property
    def full_description(self):
        """Gets the full_description of this Product.


        :return: The full_description of this Product.
        :rtype: str
        """
        return self._full_description

    @full_description.setter
    def full_description(self, full_description):
        """Sets the full_description of this Product.


        :param full_description: The full_description of this Product.
        :type: str
        """

        self._full_description = full_description

    @property
    def free_shipping(self):
        """Gets the free_shipping of this Product.


        :return: The free_shipping of this Product.
        :rtype: bool
        """
        return self._free_shipping

    @free_shipping.setter
    def free_shipping(self, free_shipping):
        """Sets the free_shipping of this Product.


        :param free_shipping: The free_shipping of this Product.
        :type: bool
        """

        self._free_shipping = free_shipping

    @property
    def sku(self):
        """Gets the sku of this Product.


        :return: The sku of this Product.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this Product.


        :param sku: The sku of this Product.
        :type: str
        """

        self._sku = sku

    @property
    def price(self):
        """Gets the price of this Product.


        :return: The price of this Product.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Product.


        :param price: The price of this Product.
        :type: int
        """

        self._price = price

    @property
    def cost_price(self):
        """Gets the cost_price of this Product.


        :return: The cost_price of this Product.
        :rtype: int
        """
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        """Sets the cost_price of this Product.


        :param cost_price: The cost_price of this Product.
        :type: int
        """

        self._cost_price = cost_price

    @property
    def retail_price(self):
        """Gets the retail_price of this Product.


        :return: The retail_price of this Product.
        :rtype: int
        """
        return self._retail_price

    @retail_price.setter
    def retail_price(self, retail_price):
        """Sets the retail_price of this Product.


        :param retail_price: The retail_price of this Product.
        :type: int
        """

        self._retail_price = retail_price

    @property
    def sale_price(self):
        """Gets the sale_price of this Product.


        :return: The sale_price of this Product.
        :rtype: int
        """
        return self._sale_price

    @sale_price.setter
    def sale_price(self, sale_price):
        """Sets the sale_price of this Product.


        :param sale_price: The sale_price of this Product.
        :type: int
        """

        self._sale_price = sale_price

    @property
    def manage_inventory(self):
        """Gets the manage_inventory of this Product.


        :return: The manage_inventory of this Product.
        :rtype: bool
        """
        return self._manage_inventory

    @manage_inventory.setter
    def manage_inventory(self, manage_inventory):
        """Sets the manage_inventory of this Product.


        :param manage_inventory: The manage_inventory of this Product.
        :type: bool
        """

        self._manage_inventory = manage_inventory

    @property
    def stock_level(self):
        """Gets the stock_level of this Product.


        :return: The stock_level of this Product.
        :rtype: int
        """
        return self._stock_level

    @stock_level.setter
    def stock_level(self, stock_level):
        """Sets the stock_level of this Product.


        :param stock_level: The stock_level of this Product.
        :type: int
        """

        self._stock_level = stock_level

    @property
    def minimum_stock_level(self):
        """Gets the minimum_stock_level of this Product.


        :return: The minimum_stock_level of this Product.
        :rtype: int
        """
        return self._minimum_stock_level

    @minimum_stock_level.setter
    def minimum_stock_level(self, minimum_stock_level):
        """Sets the minimum_stock_level of this Product.


        :param minimum_stock_level: The minimum_stock_level of this Product.
        :type: int
        """

        self._minimum_stock_level = minimum_stock_level

    @property
    def maximum_sell_count(self):
        """Gets the maximum_sell_count of this Product.


        :return: The maximum_sell_count of this Product.
        :rtype: int
        """
        return self._maximum_sell_count

    @maximum_sell_count.setter
    def maximum_sell_count(self, maximum_sell_count):
        """Sets the maximum_sell_count of this Product.


        :param maximum_sell_count: The maximum_sell_count of this Product.
        :type: int
        """

        self._maximum_sell_count = maximum_sell_count

    @property
    def item_dimensions(self):
        """Gets the item_dimensions of this Product.


        :return: The item_dimensions of this Product.
        :rtype: Dimensions
        """
        return self._item_dimensions

    @item_dimensions.setter
    def item_dimensions(self, item_dimensions):
        """Sets the item_dimensions of this Product.


        :param item_dimensions: The item_dimensions of this Product.
        :type: Dimensions
        """

        self._item_dimensions = item_dimensions

    @property
    def package_dimensions(self):
        """Gets the package_dimensions of this Product.


        :return: The package_dimensions of this Product.
        :rtype: Dimensions
        """
        return self._package_dimensions

    @package_dimensions.setter
    def package_dimensions(self, package_dimensions):
        """Sets the package_dimensions of this Product.


        :param package_dimensions: The package_dimensions of this Product.
        :type: Dimensions
        """

        self._package_dimensions = package_dimensions

    @property
    def package_weight(self):
        """Gets the package_weight of this Product.


        :return: The package_weight of this Product.
        :rtype: Weight
        """
        return self._package_weight

    @package_weight.setter
    def package_weight(self, package_weight):
        """Sets the package_weight of this Product.


        :param package_weight: The package_weight of this Product.
        :type: Weight
        """

        self._package_weight = package_weight

    @property
    def require_shipping(self):
        """Gets the require_shipping of this Product.


        :return: The require_shipping of this Product.
        :rtype: bool
        """
        return self._require_shipping

    @require_shipping.setter
    def require_shipping(self, require_shipping):
        """Sets the require_shipping of this Product.


        :param require_shipping: The require_shipping of this Product.
        :type: bool
        """

        self._require_shipping = require_shipping

    @property
    def availability(self):
        """Gets the availability of this Product.


        :return: The availability of this Product.
        :rtype: str
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this Product.


        :param availability: The availability of this Product.
        :type: str
        """
        allowed_values = ["available", "comingSoon", "retired"]
        if availability is not None and availability not in allowed_values:
            raise ValueError(
                "Invalid value for `availability` ({0}), must be one of {1}"
                .format(availability, allowed_values)
            )

        self._availability = availability

    @property
    def availability_date(self):
        """Gets the availability_date of this Product.


        :return: The availability_date of this Product.
        :rtype: date
        """
        return self._availability_date

    @availability_date.setter
    def availability_date(self, availability_date):
        """Sets the availability_date of this Product.


        :param availability_date: The availability_date of this Product.
        :type: date
        """

        self._availability_date = availability_date

    @property
    def allow_pre_order(self):
        """Gets the allow_pre_order of this Product.


        :return: The allow_pre_order of this Product.
        :rtype: bool
        """
        return self._allow_pre_order

    @allow_pre_order.setter
    def allow_pre_order(self, allow_pre_order):
        """Sets the allow_pre_order of this Product.


        :param allow_pre_order: The allow_pre_order of this Product.
        :type: bool
        """

        self._allow_pre_order = allow_pre_order

    @property
    def brand(self):
        """Gets the brand of this Product.


        :return: The brand of this Product.
        :rtype: Brand
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this Product.


        :param brand: The brand of this Product.
        :type: Brand
        """

        self._brand = brand

    @property
    def main_photo(self):
        """Gets the main_photo of this Product.


        :return: The main_photo of this Product.
        :rtype: Photo
        """
        return self._main_photo

    @main_photo.setter
    def main_photo(self, main_photo):
        """Sets the main_photo of this Product.


        :param main_photo: The main_photo of this Product.
        :type: Photo
        """

        self._main_photo = main_photo

    @property
    def photos(self):
        """Gets the photos of this Product.


        :return: The photos of this Product.
        :rtype: list[Photo]
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """Sets the photos of this Product.


        :param photos: The photos of this Product.
        :type: list[Photo]
        """

        self._photos = photos

    @property
    def files(self):
        """Gets the files of this Product.


        :return: The files of this Product.
        :rtype: list[StorageFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Product.


        :param files: The files of this Product.
        :type: list[StorageFile]
        """

        self._files = files

    @property
    def promotions(self):
        """Gets the promotions of this Product.


        :return: The promotions of this Product.
        :rtype: list[Promotion]
        """
        return self._promotions

    @promotions.setter
    def promotions(self, promotions):
        """Sets the promotions of this Product.


        :param promotions: The promotions of this Product.
        :type: list[Promotion]
        """

        self._promotions = promotions

    @property
    def related_products(self):
        """Gets the related_products of this Product.


        :return: The related_products of this Product.
        :rtype: list[Product]
        """
        return self._related_products

    @related_products.setter
    def related_products(self, related_products):
        """Sets the related_products of this Product.


        :param related_products: The related_products of this Product.
        :type: list[Product]
        """

        self._related_products = related_products

    @property
    def stock_status(self):
        """Gets the stock_status of this Product.


        :return: The stock_status of this Product.
        :rtype: str
        """
        return self._stock_status

    @stock_status.setter
    def stock_status(self, stock_status):
        """Sets the stock_status of this Product.


        :param stock_status: The stock_status of this Product.
        :type: str
        """
        allowed_values = ["available", "alert", "unavailable"]
        if stock_status is not None and stock_status not in allowed_values:
            raise ValueError(
                "Invalid value for `stock_status` ({0}), must be one of {1}"
                .format(stock_status, allowed_values)
            )

        self._stock_status = stock_status

    @property
    def categories(self):
        """Gets the categories of this Product.


        :return: The categories of this Product.
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Product.


        :param categories: The categories of this Product.
        :type: list[Category]
        """

        self._categories = categories

    @property
    def tax_class(self):
        """Gets the tax_class of this Product.


        :return: The tax_class of this Product.
        :rtype: TaxClass
        """
        return self._tax_class

    @tax_class.setter
    def tax_class(self, tax_class):
        """Sets the tax_class of this Product.


        :param tax_class: The tax_class of this Product.
        :type: TaxClass
        """

        self._tax_class = tax_class

    @property
    def option_set(self):
        """Gets the option_set of this Product.


        :return: The option_set of this Product.
        :rtype: OptionSet
        """
        return self._option_set

    @option_set.setter
    def option_set(self, option_set):
        """Sets the option_set of this Product.


        :param option_set: The option_set of this Product.
        :type: OptionSet
        """

        self._option_set = option_set

    @property
    def variants(self):
        """Gets the variants of this Product.


        :return: The variants of this Product.
        :rtype: list[Variant]
        """
        return self._variants

    @variants.setter
    def variants(self, variants):
        """Sets the variants of this Product.


        :param variants: The variants of this Product.
        :type: list[Variant]
        """

        self._variants = variants

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Product, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    @classmethod
    def get_api_client(cls):
        if cls.api_client is None:
            cls.api_client = ApiClient.instance()
        return cls.api_client


    @classmethod
    def find_all(cls, **kwargs):
        return cls.list_all_products(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_products(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_products(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_product_by_id(id)

    def create(self):
        new_instance = self.create_product(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_product_by_id(self.id, self)

    def delete(self):
        return self.delete_product_by_id(self.id)



    @classmethod
    def create_product(cls, product, **kwargs):
        """Create Product

        Create a new Product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_product(product, async=True)
        >>> result = thread.get()

        :param async bool
        :param Product product: Attributes of product to create (required)
        :return: Product
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_product_with_http_info(product, **kwargs)
        else:
            (data) = cls._create_product_with_http_info(product, **kwargs)
            return data

    @classmethod
    def _create_product_with_http_info(cls, product, **kwargs):
        """Create Product

        Create a new Product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_product_with_http_info(product, async=True)
        >>> result = thread.get()

        :param async bool
        :param Product product: Attributes of product to create (required)
        :return: Product
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product' is set
        if ('product' not in params or
                params['product'] is None):
            raise ValueError("Missing the required parameter `product` when calling `create_product`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'product' in params:
            body_params = params['product']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/products', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Product',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_product_by_id(cls, product_id, **kwargs):
        """Delete Product

        Delete an instance of Product by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_product_by_id(product_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str product_id: ID of product to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_product_by_id_with_http_info(product_id, **kwargs)
        else:
            (data) = cls._delete_product_by_id_with_http_info(product_id, **kwargs)
            return data

    @classmethod
    def _delete_product_by_id_with_http_info(cls, product_id, **kwargs):
        """Delete Product

        Delete an instance of Product by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_product_by_id_with_http_info(product_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str product_id: ID of product to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `delete_product_by_id`")

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['productId'] = params['product_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/products/{productId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def get_product_by_id(cls, product_id, **kwargs):
        """Find Product

        Return single instance of Product by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_product_by_id(product_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str product_id: ID of product to return (required)
        :return: Product
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_product_by_id_with_http_info(product_id, **kwargs)
        else:
            (data) = cls._get_product_by_id_with_http_info(product_id, **kwargs)
            return data

    @classmethod
    def _get_product_by_id_with_http_info(cls, product_id, **kwargs):
        """Find Product

        Return single instance of Product by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_product_by_id_with_http_info(product_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str product_id: ID of product to return (required)
        :return: Product
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_by_id`")

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['productId'] = params['product_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/products/{productId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Product',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_products(cls, **kwargs):
        """List Products

        Return a list of Products
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_products(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Product]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_products_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_products_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_products_with_http_info(cls, **kwargs):
        """List Products

        Return a list of Products
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_products_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Product]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'size', 'sort']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        if 'page' in params:
            query_params.append(('page', params['page']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Product]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_product_by_id(cls, product_id, product, **kwargs):
        """Replace Product

        Replace all attributes of Product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_product_by_id(product_id, product, async=True)
        >>> result = thread.get()

        :param async bool
        :param str product_id: ID of product to replace (required)
        :param Product product: Attributes of product to replace (required)
        :return: Product
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_product_by_id_with_http_info(product_id, product, **kwargs)
        else:
            (data) = cls._replace_product_by_id_with_http_info(product_id, product, **kwargs)
            return data

    @classmethod
    def _replace_product_by_id_with_http_info(cls, product_id, product, **kwargs):
        """Replace Product

        Replace all attributes of Product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_product_by_id_with_http_info(product_id, product, async=True)
        >>> result = thread.get()

        :param async bool
        :param str product_id: ID of product to replace (required)
        :param Product product: Attributes of product to replace (required)
        :return: Product
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'product']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `replace_product_by_id`")
        # verify the required parameter 'product' is set
        if ('product' not in params or
                params['product'] is None):
            raise ValueError("Missing the required parameter `product` when calling `replace_product_by_id`")

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['productId'] = params['product_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'product' in params:
            body_params = params['product']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/products/{productId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Product',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_product_by_id(cls, product_id, product, **kwargs):
        """Update Product

        Update attributes of Product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_product_by_id(product_id, product, async=True)
        >>> result = thread.get()

        :param async bool
        :param str product_id: ID of product to update. (required)
        :param Product product: Attributes of product to update. (required)
        :return: Product
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_product_by_id_with_http_info(product_id, product, **kwargs)
        else:
            (data) = cls._update_product_by_id_with_http_info(product_id, product, **kwargs)
            return data

    @classmethod
    def _update_product_by_id_with_http_info(cls, product_id, product, **kwargs):
        """Update Product

        Update attributes of Product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_product_by_id_with_http_info(product_id, product, async=True)
        >>> result = thread.get()

        :param async bool
        :param str product_id: ID of product to update. (required)
        :param Product product: Attributes of product to update. (required)
        :return: Product
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'product']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `update_product_by_id`")
        # verify the required parameter 'product' is set
        if ('product' not in params or
                params['product'] is None):
            raise ValueError("Missing the required parameter `product` when calling `update_product_by_id`")

        collection_formats = {}

        path_params = {}
        if 'product_id' in params:
            path_params['productId'] = params['product_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'product' in params:
            body_params = params['product']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/products/{productId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Product',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
