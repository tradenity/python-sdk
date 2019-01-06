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


class ShippingMethod(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'slug': 'str',
        'message': 'str',
        'description': 'str',
        'geo_zone': 'GeoZone',
        'customer_groups': 'list[CustomerGroup]',
        'status': 'str',
        'use_discounted_subtotal': 'bool',
        'include_taxes': 'bool'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'slug': 'slug',
        'message': 'message',
        'description': 'description',
        'geo_zone': 'geoZone',
        'customer_groups': 'customerGroups',
        'status': 'status',
        'use_discounted_subtotal': 'useDiscountedSubtotal',
        'include_taxes': 'includeTaxes'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, slug=None, message=None, description=None, geo_zone=None, customer_groups=None, status=None, use_discounted_subtotal=None, include_taxes=None):
        """ShippingMethod - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._slug = None
        self._message = None
        self._description = None
        self._geo_zone = None
        self._customer_groups = None
        self._status = None
        self._use_discounted_subtotal = None
        self._include_taxes = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.slug = slug
        if message is not None:
            self.message = message
        if description is not None:
            self.description = description
        self.geo_zone = geo_zone
        if customer_groups is not None:
            self.customer_groups = customer_groups
        self.status = status
        if use_discounted_subtotal is not None:
            self.use_discounted_subtotal = use_discounted_subtotal
        if include_taxes is not None:
            self.include_taxes = include_taxes

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
        """Gets the meta of this ShippingMethod.


        :return: The meta of this ShippingMethod.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ShippingMethod.


        :param meta: The meta of this ShippingMethod.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this ShippingMethod.


        :return: The name of this ShippingMethod.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShippingMethod.


        :param name: The name of this ShippingMethod.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this ShippingMethod.


        :return: The slug of this ShippingMethod.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this ShippingMethod.


        :param slug: The slug of this ShippingMethod.
        :type: str
        """

        self._slug = slug

    @property
    def message(self):
        """Gets the message of this ShippingMethod.


        :return: The message of this ShippingMethod.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShippingMethod.


        :param message: The message of this ShippingMethod.
        :type: str
        """

        self._message = message

    @property
    def description(self):
        """Gets the description of this ShippingMethod.


        :return: The description of this ShippingMethod.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShippingMethod.


        :param description: The description of this ShippingMethod.
        :type: str
        """

        self._description = description

    @property
    def geo_zone(self):
        """Gets the geo_zone of this ShippingMethod.


        :return: The geo_zone of this ShippingMethod.
        :rtype: GeoZone
        """
        return self._geo_zone

    @geo_zone.setter
    def geo_zone(self, geo_zone):
        """Sets the geo_zone of this ShippingMethod.


        :param geo_zone: The geo_zone of this ShippingMethod.
        :type: GeoZone
        """

        self._geo_zone = geo_zone

    @property
    def customer_groups(self):
        """Gets the customer_groups of this ShippingMethod.


        :return: The customer_groups of this ShippingMethod.
        :rtype: list[CustomerGroup]
        """
        return self._customer_groups

    @customer_groups.setter
    def customer_groups(self, customer_groups):
        """Sets the customer_groups of this ShippingMethod.


        :param customer_groups: The customer_groups of this ShippingMethod.
        :type: list[CustomerGroup]
        """

        self._customer_groups = customer_groups

    @property
    def status(self):
        """Gets the status of this ShippingMethod.


        :return: The status of this ShippingMethod.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShippingMethod.


        :param status: The status of this ShippingMethod.
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
    def use_discounted_subtotal(self):
        """Gets the use_discounted_subtotal of this ShippingMethod.


        :return: The use_discounted_subtotal of this ShippingMethod.
        :rtype: bool
        """
        return self._use_discounted_subtotal

    @use_discounted_subtotal.setter
    def use_discounted_subtotal(self, use_discounted_subtotal):
        """Sets the use_discounted_subtotal of this ShippingMethod.


        :param use_discounted_subtotal: The use_discounted_subtotal of this ShippingMethod.
        :type: bool
        """

        self._use_discounted_subtotal = use_discounted_subtotal

    @property
    def include_taxes(self):
        """Gets the include_taxes of this ShippingMethod.


        :return: The include_taxes of this ShippingMethod.
        :rtype: bool
        """
        return self._include_taxes

    @include_taxes.setter
    def include_taxes(self, include_taxes):
        """Sets the include_taxes of this ShippingMethod.


        :param include_taxes: The include_taxes of this ShippingMethod.
        :type: bool
        """

        self._include_taxes = include_taxes

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
        if issubclass(ShippingMethod, dict):
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
        if not isinstance(other, ShippingMethod):
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
        return cls.list_all_shipping_methods()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_shipping_methods(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_shipping_methods(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_all_for_order(cls, order_id, **kwargs):
        """Find shipping methods for order.

        Find all shipping methods suitable for an order.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_all_for_order(order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_id: Order ID to get shipping methods for. (required)
        :return: page[ShippingMethod]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._find_all_for_order_with_http_info(order_id, **kwargs)
        else:
            (data) = cls._find_all_for_order_with_http_info(order_id, **kwargs)
            return data

    @classmethod
    def _find_all_for_order_with_http_info(cls, order_id, **kwargs):
        """Find shipping methods for order.

        Find all shipping methods suitable for an order.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.find_all_for_order_with_http_info(order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_id: Order ID to get shipping methods for. (required)
        :return: page[ShippingMethod]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']
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
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `find_all_for_order`")

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']


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
            '/shippingMethods/order/{orderId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[ShippingMethod]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_shipping_methods(cls, **kwargs):
        """List ShippingMethods

        Return a list of ShippingMethods
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_shipping_methods(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[ShippingMethod]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_shipping_methods_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_shipping_methods_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_shipping_methods_with_http_info(cls, **kwargs):
        """List ShippingMethods

        Return a list of ShippingMethods
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_shipping_methods_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[ShippingMethod]
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
            '/shippingMethods', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[ShippingMethod]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
