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


class TableRateRule(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'minimum': 'int',
        'maximum': 'int',
        'cost': 'int',
        'unit': 'str',
        'table_rate_shipping': 'TableRateShipping'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'minimum': 'minimum',
        'maximum': 'maximum',
        'cost': 'cost',
        'unit': 'unit',
        'table_rate_shipping': 'tableRateShipping'
    }

    api_client = None

    def __init__(self, id=None, meta=None, minimum=None, maximum=None, cost=None, unit=None, table_rate_shipping=None):
        """TableRateRule - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._minimum = None
        self._maximum = None
        self._cost = None
        self._unit = None
        self._table_rate_shipping = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.minimum = minimum
        self.maximum = maximum
        self.cost = cost
        self.unit = unit
        self.table_rate_shipping = table_rate_shipping

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
        """Gets the meta of this TableRateRule.


        :return: The meta of this TableRateRule.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this TableRateRule.


        :param meta: The meta of this TableRateRule.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def minimum(self):
        """Gets the minimum of this TableRateRule.


        :return: The minimum of this TableRateRule.
        :rtype: int
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this TableRateRule.


        :param minimum: The minimum of this TableRateRule.
        :type: int
        """

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this TableRateRule.


        :return: The maximum of this TableRateRule.
        :rtype: int
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this TableRateRule.


        :param maximum: The maximum of this TableRateRule.
        :type: int
        """

        self._maximum = maximum

    @property
    def cost(self):
        """Gets the cost of this TableRateRule.


        :return: The cost of this TableRateRule.
        :rtype: int
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this TableRateRule.


        :param cost: The cost of this TableRateRule.
        :type: int
        """

        self._cost = cost

    @property
    def unit(self):
        """Gets the unit of this TableRateRule.


        :return: The unit of this TableRateRule.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TableRateRule.


        :param unit: The unit of this TableRateRule.
        :type: str
        """

        self._unit = unit

    @property
    def table_rate_shipping(self):
        """Gets the table_rate_shipping of this TableRateRule.


        :return: The table_rate_shipping of this TableRateRule.
        :rtype: TableRateShipping
        """
        return self._table_rate_shipping

    @table_rate_shipping.setter
    def table_rate_shipping(self, table_rate_shipping):
        """Sets the table_rate_shipping of this TableRateRule.


        :param table_rate_shipping: The table_rate_shipping of this TableRateRule.
        :type: TableRateShipping
        """

        self._table_rate_shipping = table_rate_shipping

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
        if issubclass(TableRateRule, dict):
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
        if not isinstance(other, TableRateRule):
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
        return cls.list_all_table_rate_rules(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_table_rate_rules(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_table_rate_rules(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_table_rate_rule_by_id(id)

    def create(self):
        new_instance = self.create_table_rate_rule(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_table_rate_rule_by_id(self.id, self)

    def delete(self):
        return self.delete_table_rate_rule_by_id(self.id)



    @classmethod
    def create_table_rate_rule(cls, table_rate_rule, **kwargs):
        """Create TableRateRule

        Create a new TableRateRule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_table_rate_rule(table_rate_rule, async=True)
        >>> result = thread.get()

        :param async bool
        :param TableRateRule table_rate_rule: Attributes of tableRateRule to create (required)
        :return: TableRateRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_table_rate_rule_with_http_info(table_rate_rule, **kwargs)
        else:
            (data) = cls._create_table_rate_rule_with_http_info(table_rate_rule, **kwargs)
            return data

    @classmethod
    def _create_table_rate_rule_with_http_info(cls, table_rate_rule, **kwargs):
        """Create TableRateRule

        Create a new TableRateRule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_table_rate_rule_with_http_info(table_rate_rule, async=True)
        >>> result = thread.get()

        :param async bool
        :param TableRateRule table_rate_rule: Attributes of tableRateRule to create (required)
        :return: TableRateRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['table_rate_rule']
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
        # verify the required parameter 'table_rate_rule' is set
        if ('table_rate_rule' not in params or
                params['table_rate_rule'] is None):
            raise ValueError("Missing the required parameter `table_rate_rule` when calling `create_table_rate_rule`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'table_rate_rule' in params:
            body_params = params['table_rate_rule']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/tableRateRules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRateRule',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_table_rate_rule_by_id(cls, table_rate_rule_id, **kwargs):
        """Delete TableRateRule

        Delete an instance of TableRateRule by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_table_rate_rule_by_id(table_rate_rule_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str table_rate_rule_id: ID of tableRateRule to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_table_rate_rule_by_id_with_http_info(table_rate_rule_id, **kwargs)
        else:
            (data) = cls._delete_table_rate_rule_by_id_with_http_info(table_rate_rule_id, **kwargs)
            return data

    @classmethod
    def _delete_table_rate_rule_by_id_with_http_info(cls, table_rate_rule_id, **kwargs):
        """Delete TableRateRule

        Delete an instance of TableRateRule by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_table_rate_rule_by_id_with_http_info(table_rate_rule_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str table_rate_rule_id: ID of tableRateRule to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['table_rate_rule_id']
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
        # verify the required parameter 'table_rate_rule_id' is set
        if ('table_rate_rule_id' not in params or
                params['table_rate_rule_id'] is None):
            raise ValueError("Missing the required parameter `table_rate_rule_id` when calling `delete_table_rate_rule_by_id`")

        collection_formats = {}

        path_params = {}
        if 'table_rate_rule_id' in params:
            path_params['tableRateRuleId'] = params['table_rate_rule_id']


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
            '/tableRateRules/{tableRateRuleId}', 'DELETE',
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
    def get_table_rate_rule_by_id(cls, table_rate_rule_id, **kwargs):
        """Find TableRateRule

        Return single instance of TableRateRule by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_rate_rule_by_id(table_rate_rule_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str table_rate_rule_id: ID of tableRateRule to return (required)
        :return: TableRateRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_table_rate_rule_by_id_with_http_info(table_rate_rule_id, **kwargs)
        else:
            (data) = cls._get_table_rate_rule_by_id_with_http_info(table_rate_rule_id, **kwargs)
            return data

    @classmethod
    def _get_table_rate_rule_by_id_with_http_info(cls, table_rate_rule_id, **kwargs):
        """Find TableRateRule

        Return single instance of TableRateRule by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_table_rate_rule_by_id_with_http_info(table_rate_rule_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str table_rate_rule_id: ID of tableRateRule to return (required)
        :return: TableRateRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['table_rate_rule_id']
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
        # verify the required parameter 'table_rate_rule_id' is set
        if ('table_rate_rule_id' not in params or
                params['table_rate_rule_id'] is None):
            raise ValueError("Missing the required parameter `table_rate_rule_id` when calling `get_table_rate_rule_by_id`")

        collection_formats = {}

        path_params = {}
        if 'table_rate_rule_id' in params:
            path_params['tableRateRuleId'] = params['table_rate_rule_id']


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
            '/tableRateRules/{tableRateRuleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRateRule',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_table_rate_rules(cls, **kwargs):
        """List TableRateRules

        Return a list of TableRateRules
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_table_rate_rules(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[TableRateRule]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_table_rate_rules_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_table_rate_rules_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_table_rate_rules_with_http_info(cls, **kwargs):
        """List TableRateRules

        Return a list of TableRateRules
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_table_rate_rules_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[TableRateRule]
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
            '/tableRateRules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[TableRateRule]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_table_rate_rule_by_id(cls, table_rate_rule_id, table_rate_rule, **kwargs):
        """Replace TableRateRule

        Replace all attributes of TableRateRule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_table_rate_rule_by_id(table_rate_rule_id, table_rate_rule, async=True)
        >>> result = thread.get()

        :param async bool
        :param str table_rate_rule_id: ID of tableRateRule to replace (required)
        :param TableRateRule table_rate_rule: Attributes of tableRateRule to replace (required)
        :return: TableRateRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_table_rate_rule_by_id_with_http_info(table_rate_rule_id, table_rate_rule, **kwargs)
        else:
            (data) = cls._replace_table_rate_rule_by_id_with_http_info(table_rate_rule_id, table_rate_rule, **kwargs)
            return data

    @classmethod
    def _replace_table_rate_rule_by_id_with_http_info(cls, table_rate_rule_id, table_rate_rule, **kwargs):
        """Replace TableRateRule

        Replace all attributes of TableRateRule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_table_rate_rule_by_id_with_http_info(table_rate_rule_id, table_rate_rule, async=True)
        >>> result = thread.get()

        :param async bool
        :param str table_rate_rule_id: ID of tableRateRule to replace (required)
        :param TableRateRule table_rate_rule: Attributes of tableRateRule to replace (required)
        :return: TableRateRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['table_rate_rule_id', 'table_rate_rule']
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
        # verify the required parameter 'table_rate_rule_id' is set
        if ('table_rate_rule_id' not in params or
                params['table_rate_rule_id'] is None):
            raise ValueError("Missing the required parameter `table_rate_rule_id` when calling `replace_table_rate_rule_by_id`")
        # verify the required parameter 'table_rate_rule' is set
        if ('table_rate_rule' not in params or
                params['table_rate_rule'] is None):
            raise ValueError("Missing the required parameter `table_rate_rule` when calling `replace_table_rate_rule_by_id`")

        collection_formats = {}

        path_params = {}
        if 'table_rate_rule_id' in params:
            path_params['tableRateRuleId'] = params['table_rate_rule_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'table_rate_rule' in params:
            body_params = params['table_rate_rule']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/tableRateRules/{tableRateRuleId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRateRule',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_table_rate_rule_by_id(cls, table_rate_rule_id, table_rate_rule, **kwargs):
        """Update TableRateRule

        Update attributes of TableRateRule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_table_rate_rule_by_id(table_rate_rule_id, table_rate_rule, async=True)
        >>> result = thread.get()

        :param async bool
        :param str table_rate_rule_id: ID of tableRateRule to update. (required)
        :param TableRateRule table_rate_rule: Attributes of tableRateRule to update. (required)
        :return: TableRateRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_table_rate_rule_by_id_with_http_info(table_rate_rule_id, table_rate_rule, **kwargs)
        else:
            (data) = cls._update_table_rate_rule_by_id_with_http_info(table_rate_rule_id, table_rate_rule, **kwargs)
            return data

    @classmethod
    def _update_table_rate_rule_by_id_with_http_info(cls, table_rate_rule_id, table_rate_rule, **kwargs):
        """Update TableRateRule

        Update attributes of TableRateRule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_table_rate_rule_by_id_with_http_info(table_rate_rule_id, table_rate_rule, async=True)
        >>> result = thread.get()

        :param async bool
        :param str table_rate_rule_id: ID of tableRateRule to update. (required)
        :param TableRateRule table_rate_rule: Attributes of tableRateRule to update. (required)
        :return: TableRateRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['table_rate_rule_id', 'table_rate_rule']
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
        # verify the required parameter 'table_rate_rule_id' is set
        if ('table_rate_rule_id' not in params or
                params['table_rate_rule_id'] is None):
            raise ValueError("Missing the required parameter `table_rate_rule_id` when calling `update_table_rate_rule_by_id`")
        # verify the required parameter 'table_rate_rule' is set
        if ('table_rate_rule' not in params or
                params['table_rate_rule'] is None):
            raise ValueError("Missing the required parameter `table_rate_rule` when calling `update_table_rate_rule_by_id`")

        collection_formats = {}

        path_params = {}
        if 'table_rate_rule_id' in params:
            path_params['tableRateRuleId'] = params['table_rate_rule_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'table_rate_rule' in params:
            body_params = params['table_rate_rule']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/tableRateRules/{tableRateRuleId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableRateRule',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
