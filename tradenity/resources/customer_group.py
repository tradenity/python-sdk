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


class CustomerGroup(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'slug': 'str',
        'status': 'str',
        'description': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'slug': 'slug',
        'status': 'status',
        'description': 'description'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, slug=None, status=None, description=None):
        """CustomerGroup - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._slug = None
        self._status = None
        self._description = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.slug = slug
        self.status = status
        if description is not None:
            self.description = description

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
        """Gets the meta of this CustomerGroup.


        :return: The meta of this CustomerGroup.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this CustomerGroup.


        :param meta: The meta of this CustomerGroup.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this CustomerGroup.


        :return: The name of this CustomerGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerGroup.


        :param name: The name of this CustomerGroup.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this CustomerGroup.


        :return: The slug of this CustomerGroup.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this CustomerGroup.


        :param slug: The slug of this CustomerGroup.
        :type: str
        """

        self._slug = slug

    @property
    def status(self):
        """Gets the status of this CustomerGroup.


        :return: The status of this CustomerGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CustomerGroup.


        :param status: The status of this CustomerGroup.
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
    def description(self):
        """Gets the description of this CustomerGroup.


        :return: The description of this CustomerGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomerGroup.


        :param description: The description of this CustomerGroup.
        :type: str
        """

        self._description = description

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
        if issubclass(CustomerGroup, dict):
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
        if not isinstance(other, CustomerGroup):
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
        return cls.list_all_customer_groups(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_customer_groups(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_customer_groups(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_customer_group_by_id(id)

    def create(self):
        new_instance = self.create_customer_group(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_customer_group_by_id(self.id, self)

    def delete(self):
        return self.delete_customer_group_by_id(self.id)



    @classmethod
    def create_customer_group(cls, customer_group, **kwargs):
        """Create CustomerGroup

        Create a new CustomerGroup
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_customer_group(customer_group, async=True)
        >>> result = thread.get()

        :param async bool
        :param CustomerGroup customer_group: Attributes of customerGroup to create (required)
        :return: CustomerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_customer_group_with_http_info(customer_group, **kwargs)
        else:
            (data) = cls._create_customer_group_with_http_info(customer_group, **kwargs)
            return data

    @classmethod
    def _create_customer_group_with_http_info(cls, customer_group, **kwargs):
        """Create CustomerGroup

        Create a new CustomerGroup
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_customer_group_with_http_info(customer_group, async=True)
        >>> result = thread.get()

        :param async bool
        :param CustomerGroup customer_group: Attributes of customerGroup to create (required)
        :return: CustomerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_group']
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
        # verify the required parameter 'customer_group' is set
        if ('customer_group' not in params or
                params['customer_group'] is None):
            raise ValueError("Missing the required parameter `customer_group` when calling `create_customer_group`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'customer_group' in params:
            body_params = params['customer_group']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/customerGroups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomerGroup',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_customer_group_by_id(cls, customer_group_id, **kwargs):
        """Delete CustomerGroup

        Delete an instance of CustomerGroup by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_customer_group_by_id(customer_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_group_id: ID of customerGroup to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_customer_group_by_id_with_http_info(customer_group_id, **kwargs)
        else:
            (data) = cls._delete_customer_group_by_id_with_http_info(customer_group_id, **kwargs)
            return data

    @classmethod
    def _delete_customer_group_by_id_with_http_info(cls, customer_group_id, **kwargs):
        """Delete CustomerGroup

        Delete an instance of CustomerGroup by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_customer_group_by_id_with_http_info(customer_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_group_id: ID of customerGroup to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_group_id']
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
        # verify the required parameter 'customer_group_id' is set
        if ('customer_group_id' not in params or
                params['customer_group_id'] is None):
            raise ValueError("Missing the required parameter `customer_group_id` when calling `delete_customer_group_by_id`")

        collection_formats = {}

        path_params = {}
        if 'customer_group_id' in params:
            path_params['customerGroupId'] = params['customer_group_id']


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
            '/customerGroups/{customerGroupId}', 'DELETE',
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
    def get_customer_group_by_id(cls, customer_group_id, **kwargs):
        """Find CustomerGroup

        Return single instance of CustomerGroup by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_customer_group_by_id(customer_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_group_id: ID of customerGroup to return (required)
        :return: CustomerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_customer_group_by_id_with_http_info(customer_group_id, **kwargs)
        else:
            (data) = cls._get_customer_group_by_id_with_http_info(customer_group_id, **kwargs)
            return data

    @classmethod
    def _get_customer_group_by_id_with_http_info(cls, customer_group_id, **kwargs):
        """Find CustomerGroup

        Return single instance of CustomerGroup by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_customer_group_by_id_with_http_info(customer_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_group_id: ID of customerGroup to return (required)
        :return: CustomerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_group_id']
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
        # verify the required parameter 'customer_group_id' is set
        if ('customer_group_id' not in params or
                params['customer_group_id'] is None):
            raise ValueError("Missing the required parameter `customer_group_id` when calling `get_customer_group_by_id`")

        collection_formats = {}

        path_params = {}
        if 'customer_group_id' in params:
            path_params['customerGroupId'] = params['customer_group_id']


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
            '/customerGroups/{customerGroupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomerGroup',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_customer_groups(cls, **kwargs):
        """List CustomerGroups

        Return a list of CustomerGroups
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_customer_groups(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[CustomerGroup]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_customer_groups_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_customer_groups_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_customer_groups_with_http_info(cls, **kwargs):
        """List CustomerGroups

        Return a list of CustomerGroups
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_customer_groups_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[CustomerGroup]
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
            '/customerGroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[CustomerGroup]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_customer_group_by_id(cls, customer_group_id, customer_group, **kwargs):
        """Replace CustomerGroup

        Replace all attributes of CustomerGroup
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_customer_group_by_id(customer_group_id, customer_group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_group_id: ID of customerGroup to replace (required)
        :param CustomerGroup customer_group: Attributes of customerGroup to replace (required)
        :return: CustomerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_customer_group_by_id_with_http_info(customer_group_id, customer_group, **kwargs)
        else:
            (data) = cls._replace_customer_group_by_id_with_http_info(customer_group_id, customer_group, **kwargs)
            return data

    @classmethod
    def _replace_customer_group_by_id_with_http_info(cls, customer_group_id, customer_group, **kwargs):
        """Replace CustomerGroup

        Replace all attributes of CustomerGroup
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_customer_group_by_id_with_http_info(customer_group_id, customer_group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_group_id: ID of customerGroup to replace (required)
        :param CustomerGroup customer_group: Attributes of customerGroup to replace (required)
        :return: CustomerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_group_id', 'customer_group']
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
        # verify the required parameter 'customer_group_id' is set
        if ('customer_group_id' not in params or
                params['customer_group_id'] is None):
            raise ValueError("Missing the required parameter `customer_group_id` when calling `replace_customer_group_by_id`")
        # verify the required parameter 'customer_group' is set
        if ('customer_group' not in params or
                params['customer_group'] is None):
            raise ValueError("Missing the required parameter `customer_group` when calling `replace_customer_group_by_id`")

        collection_formats = {}

        path_params = {}
        if 'customer_group_id' in params:
            path_params['customerGroupId'] = params['customer_group_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'customer_group' in params:
            body_params = params['customer_group']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/customerGroups/{customerGroupId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomerGroup',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_customer_group_by_id(cls, customer_group_id, customer_group, **kwargs):
        """Update CustomerGroup

        Update attributes of CustomerGroup
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_customer_group_by_id(customer_group_id, customer_group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_group_id: ID of customerGroup to update. (required)
        :param CustomerGroup customer_group: Attributes of customerGroup to update. (required)
        :return: CustomerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_customer_group_by_id_with_http_info(customer_group_id, customer_group, **kwargs)
        else:
            (data) = cls._update_customer_group_by_id_with_http_info(customer_group_id, customer_group, **kwargs)
            return data

    @classmethod
    def _update_customer_group_by_id_with_http_info(cls, customer_group_id, customer_group, **kwargs):
        """Update CustomerGroup

        Update attributes of CustomerGroup
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_customer_group_by_id_with_http_info(customer_group_id, customer_group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_group_id: ID of customerGroup to update. (required)
        :param CustomerGroup customer_group: Attributes of customerGroup to update. (required)
        :return: CustomerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_group_id', 'customer_group']
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
        # verify the required parameter 'customer_group_id' is set
        if ('customer_group_id' not in params or
                params['customer_group_id'] is None):
            raise ValueError("Missing the required parameter `customer_group_id` when calling `update_customer_group_by_id`")
        # verify the required parameter 'customer_group' is set
        if ('customer_group' not in params or
                params['customer_group'] is None):
            raise ValueError("Missing the required parameter `customer_group` when calling `update_customer_group_by_id`")

        collection_formats = {}

        path_params = {}
        if 'customer_group_id' in params:
            path_params['customerGroupId'] = params['customer_group_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'customer_group' in params:
            body_params = params['customer_group']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/customerGroups/{customerGroupId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomerGroup',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
