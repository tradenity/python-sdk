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


class Variant(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'slug': 'str',
        'sku': 'str',
        'description': 'str',
        'status': 'str',
        'price_change': 'int',
        'stock_level': 'int',
        'minimum_stock_level': 'int',
        'maximum_sell_count': 'int',
        'item_dimensions': 'Dimensions',
        'package_dimensions': 'Dimensions',
        'package_weight': 'Weight',
        'product': 'Product',
        'option_set': 'OptionSet',
        'option_values': 'list[OptionValue]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'slug': 'slug',
        'sku': 'sku',
        'description': 'description',
        'status': 'status',
        'price_change': 'priceChange',
        'stock_level': 'stockLevel',
        'minimum_stock_level': 'minimumStockLevel',
        'maximum_sell_count': 'maximumSellCount',
        'item_dimensions': 'itemDimensions',
        'package_dimensions': 'packageDimensions',
        'package_weight': 'packageWeight',
        'product': 'product',
        'option_set': 'optionSet',
        'option_values': 'optionValues'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, slug=None, sku=None, description=None, status=None, price_change=None, stock_level=None, minimum_stock_level=None, maximum_sell_count=None, item_dimensions=None, package_dimensions=None, package_weight=None, product=None, option_set=None, option_values=None):
        """Variant - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._slug = None
        self._sku = None
        self._description = None
        self._status = None
        self._price_change = None
        self._stock_level = None
        self._minimum_stock_level = None
        self._maximum_sell_count = None
        self._item_dimensions = None
        self._package_dimensions = None
        self._package_weight = None
        self._product = None
        self._option_set = None
        self._option_values = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.slug = slug
        self.sku = sku
        if description is not None:
            self.description = description
        self.status = status
        if price_change is not None:
            self.price_change = price_change
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
        self.product = product
        self.option_set = option_set
        if option_values is not None:
            self.option_values = option_values

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
        """Gets the meta of this Variant.


        :return: The meta of this Variant.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Variant.


        :param meta: The meta of this Variant.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Variant.


        :return: The name of this Variant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Variant.


        :param name: The name of this Variant.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Variant.


        :return: The slug of this Variant.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Variant.


        :param slug: The slug of this Variant.
        :type: str
        """

        self._slug = slug

    @property
    def sku(self):
        """Gets the sku of this Variant.


        :return: The sku of this Variant.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this Variant.


        :param sku: The sku of this Variant.
        :type: str
        """

        self._sku = sku

    @property
    def description(self):
        """Gets the description of this Variant.


        :return: The description of this Variant.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Variant.


        :param description: The description of this Variant.
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Variant.


        :return: The status of this Variant.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Variant.


        :param status: The status of this Variant.
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
    def price_change(self):
        """Gets the price_change of this Variant.


        :return: The price_change of this Variant.
        :rtype: int
        """
        return self._price_change

    @price_change.setter
    def price_change(self, price_change):
        """Sets the price_change of this Variant.


        :param price_change: The price_change of this Variant.
        :type: int
        """

        self._price_change = price_change

    @property
    def stock_level(self):
        """Gets the stock_level of this Variant.


        :return: The stock_level of this Variant.
        :rtype: int
        """
        return self._stock_level

    @stock_level.setter
    def stock_level(self, stock_level):
        """Sets the stock_level of this Variant.


        :param stock_level: The stock_level of this Variant.
        :type: int
        """

        self._stock_level = stock_level

    @property
    def minimum_stock_level(self):
        """Gets the minimum_stock_level of this Variant.


        :return: The minimum_stock_level of this Variant.
        :rtype: int
        """
        return self._minimum_stock_level

    @minimum_stock_level.setter
    def minimum_stock_level(self, minimum_stock_level):
        """Sets the minimum_stock_level of this Variant.


        :param minimum_stock_level: The minimum_stock_level of this Variant.
        :type: int
        """

        self._minimum_stock_level = minimum_stock_level

    @property
    def maximum_sell_count(self):
        """Gets the maximum_sell_count of this Variant.


        :return: The maximum_sell_count of this Variant.
        :rtype: int
        """
        return self._maximum_sell_count

    @maximum_sell_count.setter
    def maximum_sell_count(self, maximum_sell_count):
        """Sets the maximum_sell_count of this Variant.


        :param maximum_sell_count: The maximum_sell_count of this Variant.
        :type: int
        """

        self._maximum_sell_count = maximum_sell_count

    @property
    def item_dimensions(self):
        """Gets the item_dimensions of this Variant.


        :return: The item_dimensions of this Variant.
        :rtype: Dimensions
        """
        return self._item_dimensions

    @item_dimensions.setter
    def item_dimensions(self, item_dimensions):
        """Sets the item_dimensions of this Variant.


        :param item_dimensions: The item_dimensions of this Variant.
        :type: Dimensions
        """

        self._item_dimensions = item_dimensions

    @property
    def package_dimensions(self):
        """Gets the package_dimensions of this Variant.


        :return: The package_dimensions of this Variant.
        :rtype: Dimensions
        """
        return self._package_dimensions

    @package_dimensions.setter
    def package_dimensions(self, package_dimensions):
        """Sets the package_dimensions of this Variant.


        :param package_dimensions: The package_dimensions of this Variant.
        :type: Dimensions
        """

        self._package_dimensions = package_dimensions

    @property
    def package_weight(self):
        """Gets the package_weight of this Variant.


        :return: The package_weight of this Variant.
        :rtype: Weight
        """
        return self._package_weight

    @package_weight.setter
    def package_weight(self, package_weight):
        """Sets the package_weight of this Variant.


        :param package_weight: The package_weight of this Variant.
        :type: Weight
        """

        self._package_weight = package_weight

    @property
    def product(self):
        """Gets the product of this Variant.


        :return: The product of this Variant.
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Variant.


        :param product: The product of this Variant.
        :type: Product
        """

        self._product = product

    @property
    def option_set(self):
        """Gets the option_set of this Variant.


        :return: The option_set of this Variant.
        :rtype: OptionSet
        """
        return self._option_set

    @option_set.setter
    def option_set(self, option_set):
        """Sets the option_set of this Variant.


        :param option_set: The option_set of this Variant.
        :type: OptionSet
        """

        self._option_set = option_set

    @property
    def option_values(self):
        """Gets the option_values of this Variant.


        :return: The option_values of this Variant.
        :rtype: list[OptionValue]
        """
        return self._option_values

    @option_values.setter
    def option_values(self, option_values):
        """Sets the option_values of this Variant.


        :param option_values: The option_values of this Variant.
        :type: list[OptionValue]
        """

        self._option_values = option_values

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
        if issubclass(Variant, dict):
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
        if not isinstance(other, Variant):
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
    def find_all(cls, page_request=None):
        return cls.list_all_variants()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_variants(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_variants(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_variant_by_id(id)

    def create(self):
        new_instance = self.create_variant(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_variant_by_id(self.id, self)

    def delete(self):
        return self.delete_variant_by_id(self.id)



    @classmethod
    def create_variant(cls, variant, **kwargs):
        """Create Variant

        Create a new Variant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_variant(variant, async=True)
        >>> result = thread.get()

        :param async bool
        :param Variant variant: Attributes of variant to create (required)
        :return: Variant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_variant_with_http_info(variant, **kwargs)
        else:
            (data) = cls._create_variant_with_http_info(variant, **kwargs)
            return data

    @classmethod
    def _create_variant_with_http_info(cls, variant, **kwargs):
        """Create Variant

        Create a new Variant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_variant_with_http_info(variant, async=True)
        >>> result = thread.get()

        :param async bool
        :param Variant variant: Attributes of variant to create (required)
        :return: Variant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['variant']
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
        # verify the required parameter 'variant' is set
        if ('variant' not in params or
                params['variant'] is None):
            raise ValueError("Missing the required parameter `variant` when calling `create_variant`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'variant' in params:
            body_params = params['variant']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/variants', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Variant',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_variant_by_id(cls, variant_id, **kwargs):
        """Delete Variant

        Delete an instance of Variant by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_variant_by_id(variant_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str variant_id: ID of variant to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_variant_by_id_with_http_info(variant_id, **kwargs)
        else:
            (data) = cls._delete_variant_by_id_with_http_info(variant_id, **kwargs)
            return data

    @classmethod
    def _delete_variant_by_id_with_http_info(cls, variant_id, **kwargs):
        """Delete Variant

        Delete an instance of Variant by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_variant_by_id_with_http_info(variant_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str variant_id: ID of variant to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['variant_id']
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
        # verify the required parameter 'variant_id' is set
        if ('variant_id' not in params or
                params['variant_id'] is None):
            raise ValueError("Missing the required parameter `variant_id` when calling `delete_variant_by_id`")

        collection_formats = {}

        path_params = {}
        if 'variant_id' in params:
            path_params['variantId'] = params['variant_id']


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
            '/variants/{variantId}', 'DELETE',
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
    def get_variant_by_id(cls, variant_id, **kwargs):
        """Find Variant

        Return single instance of Variant by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_variant_by_id(variant_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str variant_id: ID of variant to return (required)
        :return: Variant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_variant_by_id_with_http_info(variant_id, **kwargs)
        else:
            (data) = cls._get_variant_by_id_with_http_info(variant_id, **kwargs)
            return data

    @classmethod
    def _get_variant_by_id_with_http_info(cls, variant_id, **kwargs):
        """Find Variant

        Return single instance of Variant by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_variant_by_id_with_http_info(variant_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str variant_id: ID of variant to return (required)
        :return: Variant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['variant_id']
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
        # verify the required parameter 'variant_id' is set
        if ('variant_id' not in params or
                params['variant_id'] is None):
            raise ValueError("Missing the required parameter `variant_id` when calling `get_variant_by_id`")

        collection_formats = {}

        path_params = {}
        if 'variant_id' in params:
            path_params['variantId'] = params['variant_id']


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
            '/variants/{variantId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Variant',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_variants(cls, **kwargs):
        """List Variants

        Return a list of Variants
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_variants(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Variant]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_variants_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_variants_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_variants_with_http_info(cls, **kwargs):
        """List Variants

        Return a list of Variants
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_variants_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Variant]
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
            '/variants', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Variant]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_variant_by_id(cls, variant_id, variant, **kwargs):
        """Replace Variant

        Replace all attributes of Variant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_variant_by_id(variant_id, variant, async=True)
        >>> result = thread.get()

        :param async bool
        :param str variant_id: ID of variant to replace (required)
        :param Variant variant: Attributes of variant to replace (required)
        :return: Variant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_variant_by_id_with_http_info(variant_id, variant, **kwargs)
        else:
            (data) = cls._replace_variant_by_id_with_http_info(variant_id, variant, **kwargs)
            return data

    @classmethod
    def _replace_variant_by_id_with_http_info(cls, variant_id, variant, **kwargs):
        """Replace Variant

        Replace all attributes of Variant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_variant_by_id_with_http_info(variant_id, variant, async=True)
        >>> result = thread.get()

        :param async bool
        :param str variant_id: ID of variant to replace (required)
        :param Variant variant: Attributes of variant to replace (required)
        :return: Variant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['variant_id', 'variant']
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
        # verify the required parameter 'variant_id' is set
        if ('variant_id' not in params or
                params['variant_id'] is None):
            raise ValueError("Missing the required parameter `variant_id` when calling `replace_variant_by_id`")
        # verify the required parameter 'variant' is set
        if ('variant' not in params or
                params['variant'] is None):
            raise ValueError("Missing the required parameter `variant` when calling `replace_variant_by_id`")

        collection_formats = {}

        path_params = {}
        if 'variant_id' in params:
            path_params['variantId'] = params['variant_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'variant' in params:
            body_params = params['variant']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/variants/{variantId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Variant',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_variant_by_id(cls, variant_id, variant, **kwargs):
        """Update Variant

        Update attributes of Variant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_variant_by_id(variant_id, variant, async=True)
        >>> result = thread.get()

        :param async bool
        :param str variant_id: ID of variant to update. (required)
        :param Variant variant: Attributes of variant to update. (required)
        :return: Variant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_variant_by_id_with_http_info(variant_id, variant, **kwargs)
        else:
            (data) = cls._update_variant_by_id_with_http_info(variant_id, variant, **kwargs)
            return data

    @classmethod
    def _update_variant_by_id_with_http_info(cls, variant_id, variant, **kwargs):
        """Update Variant

        Update attributes of Variant
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_variant_by_id_with_http_info(variant_id, variant, async=True)
        >>> result = thread.get()

        :param async bool
        :param str variant_id: ID of variant to update. (required)
        :param Variant variant: Attributes of variant to update. (required)
        :return: Variant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['variant_id', 'variant']
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
        # verify the required parameter 'variant_id' is set
        if ('variant_id' not in params or
                params['variant_id'] is None):
            raise ValueError("Missing the required parameter `variant_id` when calling `update_variant_by_id`")
        # verify the required parameter 'variant' is set
        if ('variant' not in params or
                params['variant'] is None):
            raise ValueError("Missing the required parameter `variant` when calling `update_variant_by_id`")

        collection_formats = {}

        path_params = {}
        if 'variant_id' in params:
            path_params['variantId'] = params['variant_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'variant' in params:
            body_params = params['variant']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/variants/{variantId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Variant',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
