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


class TaxRate(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'percentage': 'float',
        'fixed_rate': 'int',
        'status': 'str',
        'tax_class': 'TaxClass',
        'geo_zone': 'GeoZone',
        'customer_groups': 'list[CustomerGroup]',
        'based_on': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'percentage': 'percentage',
        'fixed_rate': 'fixedRate',
        'status': 'status',
        'tax_class': 'taxClass',
        'geo_zone': 'geoZone',
        'customer_groups': 'customerGroups',
        'based_on': 'basedOn'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, description=None, type=None, percentage=None, fixed_rate=None, status=None, tax_class=None, geo_zone=None, customer_groups=None, based_on=None):
        """TaxRate - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._description = None
        self._type = None
        self._percentage = None
        self._fixed_rate = None
        self._status = None
        self._tax_class = None
        self._geo_zone = None
        self._customer_groups = None
        self._based_on = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        self.percentage = percentage
        self.fixed_rate = fixed_rate
        self.status = status
        self.tax_class = tax_class
        self.geo_zone = geo_zone
        if customer_groups is not None:
            self.customer_groups = customer_groups
        if based_on is not None:
            self.based_on = based_on

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
        """Gets the meta of this TaxRate.


        :return: The meta of this TaxRate.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this TaxRate.


        :param meta: The meta of this TaxRate.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this TaxRate.


        :return: The name of this TaxRate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaxRate.


        :param name: The name of this TaxRate.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this TaxRate.


        :return: The description of this TaxRate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaxRate.


        :param description: The description of this TaxRate.
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this TaxRate.


        :return: The type of this TaxRate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaxRate.


        :param type: The type of this TaxRate.
        :type: str
        """
        allowed_values = ["percentage", "fixed"]
        if type is not None and type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def percentage(self):
        """Gets the percentage of this TaxRate.


        :return: The percentage of this TaxRate.
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this TaxRate.


        :param percentage: The percentage of this TaxRate.
        :type: float
        """

        self._percentage = percentage

    @property
    def fixed_rate(self):
        """Gets the fixed_rate of this TaxRate.


        :return: The fixed_rate of this TaxRate.
        :rtype: int
        """
        return self._fixed_rate

    @fixed_rate.setter
    def fixed_rate(self, fixed_rate):
        """Sets the fixed_rate of this TaxRate.


        :param fixed_rate: The fixed_rate of this TaxRate.
        :type: int
        """

        self._fixed_rate = fixed_rate

    @property
    def status(self):
        """Gets the status of this TaxRate.


        :return: The status of this TaxRate.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaxRate.


        :param status: The status of this TaxRate.
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
    def tax_class(self):
        """Gets the tax_class of this TaxRate.


        :return: The tax_class of this TaxRate.
        :rtype: TaxClass
        """
        return self._tax_class

    @tax_class.setter
    def tax_class(self, tax_class):
        """Sets the tax_class of this TaxRate.


        :param tax_class: The tax_class of this TaxRate.
        :type: TaxClass
        """

        self._tax_class = tax_class

    @property
    def geo_zone(self):
        """Gets the geo_zone of this TaxRate.


        :return: The geo_zone of this TaxRate.
        :rtype: GeoZone
        """
        return self._geo_zone

    @geo_zone.setter
    def geo_zone(self, geo_zone):
        """Sets the geo_zone of this TaxRate.


        :param geo_zone: The geo_zone of this TaxRate.
        :type: GeoZone
        """

        self._geo_zone = geo_zone

    @property
    def customer_groups(self):
        """Gets the customer_groups of this TaxRate.


        :return: The customer_groups of this TaxRate.
        :rtype: list[CustomerGroup]
        """
        return self._customer_groups

    @customer_groups.setter
    def customer_groups(self, customer_groups):
        """Sets the customer_groups of this TaxRate.


        :param customer_groups: The customer_groups of this TaxRate.
        :type: list[CustomerGroup]
        """

        self._customer_groups = customer_groups

    @property
    def based_on(self):
        """Gets the based_on of this TaxRate.


        :return: The based_on of this TaxRate.
        :rtype: str
        """
        return self._based_on

    @based_on.setter
    def based_on(self, based_on):
        """Sets the based_on of this TaxRate.


        :param based_on: The based_on of this TaxRate.
        :type: str
        """
        allowed_values = ["shippingAddress", "billingAddress"]
        if based_on is not None and based_on not in allowed_values:
            raise ValueError(
                "Invalid value for `based_on` ({0}), must be one of {1}"
                .format(based_on, allowed_values)
            )

        self._based_on = based_on

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
        if issubclass(TaxRate, dict):
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
        if not isinstance(other, TaxRate):
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
        return cls.list_all_tax_rates(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_tax_rates(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_tax_rates(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_tax_rate_by_id(id)

    def create(self):
        new_instance = self.create_tax_rate(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_tax_rate_by_id(self.id, self)

    def delete(self):
        return self.delete_tax_rate_by_id(self.id)



    @classmethod
    def create_tax_rate(cls, tax_rate, **kwargs):
        """Create TaxRate

        Create a new TaxRate
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_tax_rate(tax_rate, async=True)
        >>> result = thread.get()

        :param async bool
        :param TaxRate tax_rate: Attributes of taxRate to create (required)
        :return: TaxRate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_tax_rate_with_http_info(tax_rate, **kwargs)
        else:
            (data) = cls._create_tax_rate_with_http_info(tax_rate, **kwargs)
            return data

    @classmethod
    def _create_tax_rate_with_http_info(cls, tax_rate, **kwargs):
        """Create TaxRate

        Create a new TaxRate
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_tax_rate_with_http_info(tax_rate, async=True)
        >>> result = thread.get()

        :param async bool
        :param TaxRate tax_rate: Attributes of taxRate to create (required)
        :return: TaxRate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_rate']
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
        # verify the required parameter 'tax_rate' is set
        if ('tax_rate' not in params or
                params['tax_rate'] is None):
            raise ValueError("Missing the required parameter `tax_rate` when calling `create_tax_rate`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tax_rate' in params:
            body_params = params['tax_rate']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/taxRates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaxRate',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_tax_rate_by_id(cls, tax_rate_id, **kwargs):
        """Delete TaxRate

        Delete an instance of TaxRate by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_tax_rate_by_id(tax_rate_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_rate_id: ID of taxRate to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_tax_rate_by_id_with_http_info(tax_rate_id, **kwargs)
        else:
            (data) = cls._delete_tax_rate_by_id_with_http_info(tax_rate_id, **kwargs)
            return data

    @classmethod
    def _delete_tax_rate_by_id_with_http_info(cls, tax_rate_id, **kwargs):
        """Delete TaxRate

        Delete an instance of TaxRate by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_tax_rate_by_id_with_http_info(tax_rate_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_rate_id: ID of taxRate to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_rate_id']
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
        # verify the required parameter 'tax_rate_id' is set
        if ('tax_rate_id' not in params or
                params['tax_rate_id'] is None):
            raise ValueError("Missing the required parameter `tax_rate_id` when calling `delete_tax_rate_by_id`")

        collection_formats = {}

        path_params = {}
        if 'tax_rate_id' in params:
            path_params['taxRateId'] = params['tax_rate_id']


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
            '/taxRates/{taxRateId}', 'DELETE',
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
    def get_tax_rate_by_id(cls, tax_rate_id, **kwargs):
        """Find TaxRate

        Return single instance of TaxRate by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tax_rate_by_id(tax_rate_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_rate_id: ID of taxRate to return (required)
        :return: TaxRate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_tax_rate_by_id_with_http_info(tax_rate_id, **kwargs)
        else:
            (data) = cls._get_tax_rate_by_id_with_http_info(tax_rate_id, **kwargs)
            return data

    @classmethod
    def _get_tax_rate_by_id_with_http_info(cls, tax_rate_id, **kwargs):
        """Find TaxRate

        Return single instance of TaxRate by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tax_rate_by_id_with_http_info(tax_rate_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_rate_id: ID of taxRate to return (required)
        :return: TaxRate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_rate_id']
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
        # verify the required parameter 'tax_rate_id' is set
        if ('tax_rate_id' not in params or
                params['tax_rate_id'] is None):
            raise ValueError("Missing the required parameter `tax_rate_id` when calling `get_tax_rate_by_id`")

        collection_formats = {}

        path_params = {}
        if 'tax_rate_id' in params:
            path_params['taxRateId'] = params['tax_rate_id']


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
            '/taxRates/{taxRateId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaxRate',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_tax_rates(cls, **kwargs):
        """List TaxRates

        Return a list of TaxRates
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_tax_rates(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[TaxRate]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_tax_rates_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_tax_rates_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_tax_rates_with_http_info(cls, **kwargs):
        """List TaxRates

        Return a list of TaxRates
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_tax_rates_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[TaxRate]
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
            '/taxRates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[TaxRate]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_tax_rate_by_id(cls, tax_rate_id, tax_rate, **kwargs):
        """Replace TaxRate

        Replace all attributes of TaxRate
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_tax_rate_by_id(tax_rate_id, tax_rate, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_rate_id: ID of taxRate to replace (required)
        :param TaxRate tax_rate: Attributes of taxRate to replace (required)
        :return: TaxRate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_tax_rate_by_id_with_http_info(tax_rate_id, tax_rate, **kwargs)
        else:
            (data) = cls._replace_tax_rate_by_id_with_http_info(tax_rate_id, tax_rate, **kwargs)
            return data

    @classmethod
    def _replace_tax_rate_by_id_with_http_info(cls, tax_rate_id, tax_rate, **kwargs):
        """Replace TaxRate

        Replace all attributes of TaxRate
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_tax_rate_by_id_with_http_info(tax_rate_id, tax_rate, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_rate_id: ID of taxRate to replace (required)
        :param TaxRate tax_rate: Attributes of taxRate to replace (required)
        :return: TaxRate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_rate_id', 'tax_rate']
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
        # verify the required parameter 'tax_rate_id' is set
        if ('tax_rate_id' not in params or
                params['tax_rate_id'] is None):
            raise ValueError("Missing the required parameter `tax_rate_id` when calling `replace_tax_rate_by_id`")
        # verify the required parameter 'tax_rate' is set
        if ('tax_rate' not in params or
                params['tax_rate'] is None):
            raise ValueError("Missing the required parameter `tax_rate` when calling `replace_tax_rate_by_id`")

        collection_formats = {}

        path_params = {}
        if 'tax_rate_id' in params:
            path_params['taxRateId'] = params['tax_rate_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tax_rate' in params:
            body_params = params['tax_rate']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/taxRates/{taxRateId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaxRate',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_tax_rate_by_id(cls, tax_rate_id, tax_rate, **kwargs):
        """Update TaxRate

        Update attributes of TaxRate
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_tax_rate_by_id(tax_rate_id, tax_rate, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_rate_id: ID of taxRate to update. (required)
        :param TaxRate tax_rate: Attributes of taxRate to update. (required)
        :return: TaxRate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_tax_rate_by_id_with_http_info(tax_rate_id, tax_rate, **kwargs)
        else:
            (data) = cls._update_tax_rate_by_id_with_http_info(tax_rate_id, tax_rate, **kwargs)
            return data

    @classmethod
    def _update_tax_rate_by_id_with_http_info(cls, tax_rate_id, tax_rate, **kwargs):
        """Update TaxRate

        Update attributes of TaxRate
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_tax_rate_by_id_with_http_info(tax_rate_id, tax_rate, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_rate_id: ID of taxRate to update. (required)
        :param TaxRate tax_rate: Attributes of taxRate to update. (required)
        :return: TaxRate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_rate_id', 'tax_rate']
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
        # verify the required parameter 'tax_rate_id' is set
        if ('tax_rate_id' not in params or
                params['tax_rate_id'] is None):
            raise ValueError("Missing the required parameter `tax_rate_id` when calling `update_tax_rate_by_id`")
        # verify the required parameter 'tax_rate' is set
        if ('tax_rate' not in params or
                params['tax_rate'] is None):
            raise ValueError("Missing the required parameter `tax_rate` when calling `update_tax_rate_by_id`")

        collection_formats = {}

        path_params = {}
        if 'tax_rate_id' in params:
            path_params['taxRateId'] = params['tax_rate_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tax_rate' in params:
            body_params = params['tax_rate']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/taxRates/{taxRateId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaxRate',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
