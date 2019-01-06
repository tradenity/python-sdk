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


class Option(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'slug': 'str',
        'description': 'str',
        'required': 'bool',
        'data_type': 'str',
        'status': 'str',
        'position': 'int',
        'values': 'list[OptionValue]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'slug': 'slug',
        'description': 'description',
        'required': 'required',
        'data_type': 'dataType',
        'status': 'status',
        'position': 'position',
        'values': 'values'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, slug=None, description=None, required=None, data_type=None, status=None, position=None, values=None):
        """Option - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._slug = None
        self._description = None
        self._required = None
        self._data_type = None
        self._status = None
        self._position = None
        self._values = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.slug = slug
        if description is not None:
            self.description = description
        if required is not None:
            self.required = required
        self.data_type = data_type
        self.status = status
        self.position = position
        if values is not None:
            self.values = values

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
        """Gets the meta of this Option.


        :return: The meta of this Option.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Option.


        :param meta: The meta of this Option.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Option.


        :return: The name of this Option.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Option.


        :param name: The name of this Option.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Option.


        :return: The slug of this Option.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Option.


        :param slug: The slug of this Option.
        :type: str
        """

        self._slug = slug

    @property
    def description(self):
        """Gets the description of this Option.


        :return: The description of this Option.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Option.


        :param description: The description of this Option.
        :type: str
        """

        self._description = description

    @property
    def required(self):
        """Gets the required of this Option.


        :return: The required of this Option.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this Option.


        :param required: The required of this Option.
        :type: bool
        """

        self._required = required

    @property
    def data_type(self):
        """Gets the data_type of this Option.


        :return: The data_type of this Option.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Option.


        :param data_type: The data_type of this Option.
        :type: str
        """
        allowed_values = ["string", "number", "date", "color"]
        if data_type is not None and data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

    @property
    def status(self):
        """Gets the status of this Option.


        :return: The status of this Option.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Option.


        :param status: The status of this Option.
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
    def position(self):
        """Gets the position of this Option.


        :return: The position of this Option.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Option.


        :param position: The position of this Option.
        :type: int
        """

        self._position = position

    @property
    def values(self):
        """Gets the values of this Option.


        :return: The values of this Option.
        :rtype: list[OptionValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Option.


        :param values: The values of this Option.
        :type: list[OptionValue]
        """

        self._values = values

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
        if issubclass(Option, dict):
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
        if not isinstance(other, Option):
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
        return cls.list_all_options()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_options(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_options(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_option_by_id(id)

    def create(self):
        new_instance = self.create_option(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_option_by_id(self.id, self)

    def delete(self):
        return self.delete_option_by_id(self.id)



    @classmethod
    def create_option(cls, option, **kwargs):
        """Create Option

        Create a new Option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_option(option, async=True)
        >>> result = thread.get()

        :param async bool
        :param Option option: Attributes of option to create (required)
        :return: Option
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_option_with_http_info(option, **kwargs)
        else:
            (data) = cls._create_option_with_http_info(option, **kwargs)
            return data

    @classmethod
    def _create_option_with_http_info(cls, option, **kwargs):
        """Create Option

        Create a new Option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_option_with_http_info(option, async=True)
        >>> result = thread.get()

        :param async bool
        :param Option option: Attributes of option to create (required)
        :return: Option
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option']
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
        # verify the required parameter 'option' is set
        if ('option' not in params or
                params['option'] is None):
            raise ValueError("Missing the required parameter `option` when calling `create_option`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'option' in params:
            body_params = params['option']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/options', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Option',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_option_by_id(cls, option_id, **kwargs):
        """Delete Option

        Delete an instance of Option by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_option_by_id(option_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_id: ID of option to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_option_by_id_with_http_info(option_id, **kwargs)
        else:
            (data) = cls._delete_option_by_id_with_http_info(option_id, **kwargs)
            return data

    @classmethod
    def _delete_option_by_id_with_http_info(cls, option_id, **kwargs):
        """Delete Option

        Delete an instance of Option by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_option_by_id_with_http_info(option_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_id: ID of option to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_id']
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
        # verify the required parameter 'option_id' is set
        if ('option_id' not in params or
                params['option_id'] is None):
            raise ValueError("Missing the required parameter `option_id` when calling `delete_option_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_id' in params:
            path_params['optionId'] = params['option_id']


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
            '/options/{optionId}', 'DELETE',
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
    def get_option_by_id(cls, option_id, **kwargs):
        """Find Option

        Return single instance of Option by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_option_by_id(option_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_id: ID of option to return (required)
        :return: Option
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_option_by_id_with_http_info(option_id, **kwargs)
        else:
            (data) = cls._get_option_by_id_with_http_info(option_id, **kwargs)
            return data

    @classmethod
    def _get_option_by_id_with_http_info(cls, option_id, **kwargs):
        """Find Option

        Return single instance of Option by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_option_by_id_with_http_info(option_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_id: ID of option to return (required)
        :return: Option
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_id']
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
        # verify the required parameter 'option_id' is set
        if ('option_id' not in params or
                params['option_id'] is None):
            raise ValueError("Missing the required parameter `option_id` when calling `get_option_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_id' in params:
            path_params['optionId'] = params['option_id']


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
            '/options/{optionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Option',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_options(cls, **kwargs):
        """List Options

        Return a list of Options
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_options(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Option]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_options_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_options_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_options_with_http_info(cls, **kwargs):
        """List Options

        Return a list of Options
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_options_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Option]
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
            '/options', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Option]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_option_by_id(cls, option_id, option, **kwargs):
        """Replace Option

        Replace all attributes of Option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_option_by_id(option_id, option, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_id: ID of option to replace (required)
        :param Option option: Attributes of option to replace (required)
        :return: Option
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_option_by_id_with_http_info(option_id, option, **kwargs)
        else:
            (data) = cls._replace_option_by_id_with_http_info(option_id, option, **kwargs)
            return data

    @classmethod
    def _replace_option_by_id_with_http_info(cls, option_id, option, **kwargs):
        """Replace Option

        Replace all attributes of Option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_option_by_id_with_http_info(option_id, option, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_id: ID of option to replace (required)
        :param Option option: Attributes of option to replace (required)
        :return: Option
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_id', 'option']
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
        # verify the required parameter 'option_id' is set
        if ('option_id' not in params or
                params['option_id'] is None):
            raise ValueError("Missing the required parameter `option_id` when calling `replace_option_by_id`")
        # verify the required parameter 'option' is set
        if ('option' not in params or
                params['option'] is None):
            raise ValueError("Missing the required parameter `option` when calling `replace_option_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_id' in params:
            path_params['optionId'] = params['option_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'option' in params:
            body_params = params['option']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/options/{optionId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Option',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_option_by_id(cls, option_id, option, **kwargs):
        """Update Option

        Update attributes of Option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_option_by_id(option_id, option, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_id: ID of option to update. (required)
        :param Option option: Attributes of option to update. (required)
        :return: Option
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_option_by_id_with_http_info(option_id, option, **kwargs)
        else:
            (data) = cls._update_option_by_id_with_http_info(option_id, option, **kwargs)
            return data

    @classmethod
    def _update_option_by_id_with_http_info(cls, option_id, option, **kwargs):
        """Update Option

        Update attributes of Option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_option_by_id_with_http_info(option_id, option, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_id: ID of option to update. (required)
        :param Option option: Attributes of option to update. (required)
        :return: Option
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_id', 'option']
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
        # verify the required parameter 'option_id' is set
        if ('option_id' not in params or
                params['option_id'] is None):
            raise ValueError("Missing the required parameter `option_id` when calling `update_option_by_id`")
        # verify the required parameter 'option' is set
        if ('option' not in params or
                params['option'] is None):
            raise ValueError("Missing the required parameter `option` when calling `update_option_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_id' in params:
            path_params['optionId'] = params['option_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'option' in params:
            body_params = params['option']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/options/{optionId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Option',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
