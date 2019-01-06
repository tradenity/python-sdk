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


class State(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'code': 'str',
        'country': 'Country'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'code': 'code',
        'country': 'country'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, code=None, country=None):
        """State - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._code = None
        self._country = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        if code is not None:
            self.code = code
        self.country = country

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
        """Gets the meta of this State.


        :return: The meta of this State.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this State.


        :param meta: The meta of this State.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this State.


        :return: The name of this State.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this State.


        :param name: The name of this State.
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this State.


        :return: The code of this State.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this State.


        :param code: The code of this State.
        :type: str
        """

        self._code = code

    @property
    def country(self):
        """Gets the country of this State.


        :return: The country of this State.
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this State.


        :param country: The country of this State.
        :type: Country
        """

        self._country = country

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
        if issubclass(State, dict):
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
        if not isinstance(other, State):
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
        return cls.list_all_states()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_states(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_states(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_state_by_id(id)

    def create(self):
        new_instance = self.create_state(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_state_by_id(self.id, self)

    def delete(self):
        return self.delete_state_by_id(self.id)



    @classmethod
    def create_state(cls, state, **kwargs):
        """Create State

        Create a new State
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_state(state, async=True)
        >>> result = thread.get()

        :param async bool
        :param State state: Attributes of state to create (required)
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_state_with_http_info(state, **kwargs)
        else:
            (data) = cls._create_state_with_http_info(state, **kwargs)
            return data

    @classmethod
    def _create_state_with_http_info(cls, state, **kwargs):
        """Create State

        Create a new State
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_state_with_http_info(state, async=True)
        >>> result = thread.get()

        :param async bool
        :param State state: Attributes of state to create (required)
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['state']
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
        # verify the required parameter 'state' is set
        if ('state' not in params or
                params['state'] is None):
            raise ValueError("Missing the required parameter `state` when calling `create_state`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'state' in params:
            body_params = params['state']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/states', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='State',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_state_by_id(cls, state_id, **kwargs):
        """Delete State

        Delete an instance of State by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_state_by_id(state_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str state_id: ID of state to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_state_by_id_with_http_info(state_id, **kwargs)
        else:
            (data) = cls._delete_state_by_id_with_http_info(state_id, **kwargs)
            return data

    @classmethod
    def _delete_state_by_id_with_http_info(cls, state_id, **kwargs):
        """Delete State

        Delete an instance of State by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_state_by_id_with_http_info(state_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str state_id: ID of state to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['state_id']
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
        # verify the required parameter 'state_id' is set
        if ('state_id' not in params or
                params['state_id'] is None):
            raise ValueError("Missing the required parameter `state_id` when calling `delete_state_by_id`")

        collection_formats = {}

        path_params = {}
        if 'state_id' in params:
            path_params['stateId'] = params['state_id']


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
            '/states/{stateId}', 'DELETE',
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
    def get_state_by_id(cls, state_id, **kwargs):
        """Find State

        Return single instance of State by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_state_by_id(state_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str state_id: ID of state to return (required)
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_state_by_id_with_http_info(state_id, **kwargs)
        else:
            (data) = cls._get_state_by_id_with_http_info(state_id, **kwargs)
            return data

    @classmethod
    def _get_state_by_id_with_http_info(cls, state_id, **kwargs):
        """Find State

        Return single instance of State by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_state_by_id_with_http_info(state_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str state_id: ID of state to return (required)
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['state_id']
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
        # verify the required parameter 'state_id' is set
        if ('state_id' not in params or
                params['state_id'] is None):
            raise ValueError("Missing the required parameter `state_id` when calling `get_state_by_id`")

        collection_formats = {}

        path_params = {}
        if 'state_id' in params:
            path_params['stateId'] = params['state_id']


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
            '/states/{stateId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='State',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_states(cls, **kwargs):
        """List States

        Return a list of States
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_states(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[State]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_states_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_states_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_states_with_http_info(cls, **kwargs):
        """List States

        Return a list of States
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_states_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[State]
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
            '/states', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[State]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_state_by_id(cls, state_id, state, **kwargs):
        """Replace State

        Replace all attributes of State
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_state_by_id(state_id, state, async=True)
        >>> result = thread.get()

        :param async bool
        :param str state_id: ID of state to replace (required)
        :param State state: Attributes of state to replace (required)
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_state_by_id_with_http_info(state_id, state, **kwargs)
        else:
            (data) = cls._replace_state_by_id_with_http_info(state_id, state, **kwargs)
            return data

    @classmethod
    def _replace_state_by_id_with_http_info(cls, state_id, state, **kwargs):
        """Replace State

        Replace all attributes of State
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_state_by_id_with_http_info(state_id, state, async=True)
        >>> result = thread.get()

        :param async bool
        :param str state_id: ID of state to replace (required)
        :param State state: Attributes of state to replace (required)
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['state_id', 'state']
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
        # verify the required parameter 'state_id' is set
        if ('state_id' not in params or
                params['state_id'] is None):
            raise ValueError("Missing the required parameter `state_id` when calling `replace_state_by_id`")
        # verify the required parameter 'state' is set
        if ('state' not in params or
                params['state'] is None):
            raise ValueError("Missing the required parameter `state` when calling `replace_state_by_id`")

        collection_formats = {}

        path_params = {}
        if 'state_id' in params:
            path_params['stateId'] = params['state_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'state' in params:
            body_params = params['state']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/states/{stateId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='State',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_state_by_id(cls, state_id, state, **kwargs):
        """Update State

        Update attributes of State
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_state_by_id(state_id, state, async=True)
        >>> result = thread.get()

        :param async bool
        :param str state_id: ID of state to update. (required)
        :param State state: Attributes of state to update. (required)
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_state_by_id_with_http_info(state_id, state, **kwargs)
        else:
            (data) = cls._update_state_by_id_with_http_info(state_id, state, **kwargs)
            return data

    @classmethod
    def _update_state_by_id_with_http_info(cls, state_id, state, **kwargs):
        """Update State

        Update attributes of State
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_state_by_id_with_http_info(state_id, state, async=True)
        >>> result = thread.get()

        :param async bool
        :param str state_id: ID of state to update. (required)
        :param State state: Attributes of state to update. (required)
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['state_id', 'state']
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
        # verify the required parameter 'state_id' is set
        if ('state_id' not in params or
                params['state_id'] is None):
            raise ValueError("Missing the required parameter `state_id` when calling `update_state_by_id`")
        # verify the required parameter 'state' is set
        if ('state' not in params or
                params['state'] is None):
            raise ValueError("Missing the required parameter `state` when calling `update_state_by_id`")

        collection_formats = {}

        path_params = {}
        if 'state_id' in params:
            path_params['stateId'] = params['state_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'state' in params:
            body_params = params['state']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/states/{stateId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='State',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
