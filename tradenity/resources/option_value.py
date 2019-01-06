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


class OptionValue(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'option': 'Option',
        'value': 'str',
        'code': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'option': 'option',
        'value': 'value',
        'code': 'code'
    }

    api_client = None

    def __init__(self, id=None, meta=None, option=None, value=None, code=None):
        """OptionValue - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._option = None
        self._value = None
        self._code = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.option = option
        self.value = value
        self.code = code

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
        """Gets the meta of this OptionValue.


        :return: The meta of this OptionValue.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this OptionValue.


        :param meta: The meta of this OptionValue.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def option(self):
        """Gets the option of this OptionValue.


        :return: The option of this OptionValue.
        :rtype: Option
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this OptionValue.


        :param option: The option of this OptionValue.
        :type: Option
        """

        self._option = option

    @property
    def value(self):
        """Gets the value of this OptionValue.


        :return: The value of this OptionValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OptionValue.


        :param value: The value of this OptionValue.
        :type: str
        """

        self._value = value

    @property
    def code(self):
        """Gets the code of this OptionValue.


        :return: The code of this OptionValue.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OptionValue.


        :param code: The code of this OptionValue.
        :type: str
        """

        self._code = code

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
        if issubclass(OptionValue, dict):
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
        if not isinstance(other, OptionValue):
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
        return cls.list_all_option_values()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_option_values(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_option_values(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_option_value_by_id(id)

    def create(self):
        new_instance = self.create_option_value(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_option_value_by_id(self.id, self)

    def delete(self):
        return self.delete_option_value_by_id(self.id)



    @classmethod
    def create_option_value(cls, option_value, **kwargs):
        """Create OptionValue

        Create a new OptionValue
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_option_value(option_value, async=True)
        >>> result = thread.get()

        :param async bool
        :param OptionValue option_value: Attributes of optionValue to create (required)
        :return: OptionValue
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_option_value_with_http_info(option_value, **kwargs)
        else:
            (data) = cls._create_option_value_with_http_info(option_value, **kwargs)
            return data

    @classmethod
    def _create_option_value_with_http_info(cls, option_value, **kwargs):
        """Create OptionValue

        Create a new OptionValue
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_option_value_with_http_info(option_value, async=True)
        >>> result = thread.get()

        :param async bool
        :param OptionValue option_value: Attributes of optionValue to create (required)
        :return: OptionValue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_value']
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
        # verify the required parameter 'option_value' is set
        if ('option_value' not in params or
                params['option_value'] is None):
            raise ValueError("Missing the required parameter `option_value` when calling `create_option_value`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'option_value' in params:
            body_params = params['option_value']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/optionValues', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OptionValue',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_option_value_by_id(cls, option_value_id, **kwargs):
        """Delete OptionValue

        Delete an instance of OptionValue by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_option_value_by_id(option_value_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_value_id: ID of optionValue to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_option_value_by_id_with_http_info(option_value_id, **kwargs)
        else:
            (data) = cls._delete_option_value_by_id_with_http_info(option_value_id, **kwargs)
            return data

    @classmethod
    def _delete_option_value_by_id_with_http_info(cls, option_value_id, **kwargs):
        """Delete OptionValue

        Delete an instance of OptionValue by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_option_value_by_id_with_http_info(option_value_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_value_id: ID of optionValue to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_value_id']
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
        # verify the required parameter 'option_value_id' is set
        if ('option_value_id' not in params or
                params['option_value_id'] is None):
            raise ValueError("Missing the required parameter `option_value_id` when calling `delete_option_value_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_value_id' in params:
            path_params['optionValueId'] = params['option_value_id']


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
            '/optionValues/{optionValueId}', 'DELETE',
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
    def get_option_value_by_id(cls, option_value_id, **kwargs):
        """Find OptionValue

        Return single instance of OptionValue by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_option_value_by_id(option_value_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_value_id: ID of optionValue to return (required)
        :return: OptionValue
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_option_value_by_id_with_http_info(option_value_id, **kwargs)
        else:
            (data) = cls._get_option_value_by_id_with_http_info(option_value_id, **kwargs)
            return data

    @classmethod
    def _get_option_value_by_id_with_http_info(cls, option_value_id, **kwargs):
        """Find OptionValue

        Return single instance of OptionValue by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_option_value_by_id_with_http_info(option_value_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_value_id: ID of optionValue to return (required)
        :return: OptionValue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_value_id']
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
        # verify the required parameter 'option_value_id' is set
        if ('option_value_id' not in params or
                params['option_value_id'] is None):
            raise ValueError("Missing the required parameter `option_value_id` when calling `get_option_value_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_value_id' in params:
            path_params['optionValueId'] = params['option_value_id']


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
            '/optionValues/{optionValueId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OptionValue',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_option_values(cls, **kwargs):
        """List OptionValues

        Return a list of OptionValues
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_option_values(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[OptionValue]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_option_values_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_option_values_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_option_values_with_http_info(cls, **kwargs):
        """List OptionValues

        Return a list of OptionValues
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_option_values_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[OptionValue]
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
            '/optionValues', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[OptionValue]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_option_value_by_id(cls, option_value_id, option_value, **kwargs):
        """Replace OptionValue

        Replace all attributes of OptionValue
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_option_value_by_id(option_value_id, option_value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_value_id: ID of optionValue to replace (required)
        :param OptionValue option_value: Attributes of optionValue to replace (required)
        :return: OptionValue
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_option_value_by_id_with_http_info(option_value_id, option_value, **kwargs)
        else:
            (data) = cls._replace_option_value_by_id_with_http_info(option_value_id, option_value, **kwargs)
            return data

    @classmethod
    def _replace_option_value_by_id_with_http_info(cls, option_value_id, option_value, **kwargs):
        """Replace OptionValue

        Replace all attributes of OptionValue
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_option_value_by_id_with_http_info(option_value_id, option_value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_value_id: ID of optionValue to replace (required)
        :param OptionValue option_value: Attributes of optionValue to replace (required)
        :return: OptionValue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_value_id', 'option_value']
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
        # verify the required parameter 'option_value_id' is set
        if ('option_value_id' not in params or
                params['option_value_id'] is None):
            raise ValueError("Missing the required parameter `option_value_id` when calling `replace_option_value_by_id`")
        # verify the required parameter 'option_value' is set
        if ('option_value' not in params or
                params['option_value'] is None):
            raise ValueError("Missing the required parameter `option_value` when calling `replace_option_value_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_value_id' in params:
            path_params['optionValueId'] = params['option_value_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'option_value' in params:
            body_params = params['option_value']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/optionValues/{optionValueId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OptionValue',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_option_value_by_id(cls, option_value_id, option_value, **kwargs):
        """Update OptionValue

        Update attributes of OptionValue
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_option_value_by_id(option_value_id, option_value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_value_id: ID of optionValue to update. (required)
        :param OptionValue option_value: Attributes of optionValue to update. (required)
        :return: OptionValue
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_option_value_by_id_with_http_info(option_value_id, option_value, **kwargs)
        else:
            (data) = cls._update_option_value_by_id_with_http_info(option_value_id, option_value, **kwargs)
            return data

    @classmethod
    def _update_option_value_by_id_with_http_info(cls, option_value_id, option_value, **kwargs):
        """Update OptionValue

        Update attributes of OptionValue
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_option_value_by_id_with_http_info(option_value_id, option_value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_value_id: ID of optionValue to update. (required)
        :param OptionValue option_value: Attributes of optionValue to update. (required)
        :return: OptionValue
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_value_id', 'option_value']
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
        # verify the required parameter 'option_value_id' is set
        if ('option_value_id' not in params or
                params['option_value_id'] is None):
            raise ValueError("Missing the required parameter `option_value_id` when calling `update_option_value_by_id`")
        # verify the required parameter 'option_value' is set
        if ('option_value' not in params or
                params['option_value'] is None):
            raise ValueError("Missing the required parameter `option_value` when calling `update_option_value_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_value_id' in params:
            path_params['optionValueId'] = params['option_value_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'option_value' in params:
            body_params = params['option_value']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/optionValues/{optionValueId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OptionValue',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
