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


class OptionSet(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'slug': 'str',
        'description': 'str',
        'status': 'str',
        'options': 'list[Option]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'slug': 'slug',
        'description': 'description',
        'status': 'status',
        'options': 'options'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, slug=None, description=None, status=None, options=None):
        """OptionSet - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._slug = None
        self._description = None
        self._status = None
        self._options = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.slug = slug
        if description is not None:
            self.description = description
        self.status = status
        if options is not None:
            self.options = options

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
        """Gets the meta of this OptionSet.


        :return: The meta of this OptionSet.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this OptionSet.


        :param meta: The meta of this OptionSet.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this OptionSet.


        :return: The name of this OptionSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OptionSet.


        :param name: The name of this OptionSet.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this OptionSet.


        :return: The slug of this OptionSet.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this OptionSet.


        :param slug: The slug of this OptionSet.
        :type: str
        """

        self._slug = slug

    @property
    def description(self):
        """Gets the description of this OptionSet.


        :return: The description of this OptionSet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OptionSet.


        :param description: The description of this OptionSet.
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this OptionSet.


        :return: The status of this OptionSet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OptionSet.


        :param status: The status of this OptionSet.
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
    def options(self):
        """Gets the options of this OptionSet.


        :return: The options of this OptionSet.
        :rtype: list[Option]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this OptionSet.


        :param options: The options of this OptionSet.
        :type: list[Option]
        """

        self._options = options

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
        if issubclass(OptionSet, dict):
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
        if not isinstance(other, OptionSet):
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
        return cls.list_all_option_sets()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_option_sets(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_option_sets(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_option_set_by_id(id)

    def create(self):
        new_instance = self.create_option_set(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_option_set_by_id(self.id, self)

    def delete(self):
        return self.delete_option_set_by_id(self.id)



    @classmethod
    def create_option_set(cls, option_set, **kwargs):
        """Create OptionSet

        Create a new OptionSet
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_option_set(option_set, async=True)
        >>> result = thread.get()

        :param async bool
        :param OptionSet option_set: Attributes of optionSet to create (required)
        :return: OptionSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_option_set_with_http_info(option_set, **kwargs)
        else:
            (data) = cls._create_option_set_with_http_info(option_set, **kwargs)
            return data

    @classmethod
    def _create_option_set_with_http_info(cls, option_set, **kwargs):
        """Create OptionSet

        Create a new OptionSet
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_option_set_with_http_info(option_set, async=True)
        >>> result = thread.get()

        :param async bool
        :param OptionSet option_set: Attributes of optionSet to create (required)
        :return: OptionSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_set']
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
        # verify the required parameter 'option_set' is set
        if ('option_set' not in params or
                params['option_set'] is None):
            raise ValueError("Missing the required parameter `option_set` when calling `create_option_set`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'option_set' in params:
            body_params = params['option_set']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/optionSets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OptionSet',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_option_set_by_id(cls, option_set_id, **kwargs):
        """Delete OptionSet

        Delete an instance of OptionSet by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_option_set_by_id(option_set_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_set_id: ID of optionSet to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_option_set_by_id_with_http_info(option_set_id, **kwargs)
        else:
            (data) = cls._delete_option_set_by_id_with_http_info(option_set_id, **kwargs)
            return data

    @classmethod
    def _delete_option_set_by_id_with_http_info(cls, option_set_id, **kwargs):
        """Delete OptionSet

        Delete an instance of OptionSet by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_option_set_by_id_with_http_info(option_set_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_set_id: ID of optionSet to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_set_id']
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
        # verify the required parameter 'option_set_id' is set
        if ('option_set_id' not in params or
                params['option_set_id'] is None):
            raise ValueError("Missing the required parameter `option_set_id` when calling `delete_option_set_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_set_id' in params:
            path_params['optionSetId'] = params['option_set_id']


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
            '/optionSets/{optionSetId}', 'DELETE',
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
    def get_option_set_by_id(cls, option_set_id, **kwargs):
        """Find OptionSet

        Return single instance of OptionSet by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_option_set_by_id(option_set_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_set_id: ID of optionSet to return (required)
        :return: OptionSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_option_set_by_id_with_http_info(option_set_id, **kwargs)
        else:
            (data) = cls._get_option_set_by_id_with_http_info(option_set_id, **kwargs)
            return data

    @classmethod
    def _get_option_set_by_id_with_http_info(cls, option_set_id, **kwargs):
        """Find OptionSet

        Return single instance of OptionSet by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_option_set_by_id_with_http_info(option_set_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_set_id: ID of optionSet to return (required)
        :return: OptionSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_set_id']
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
        # verify the required parameter 'option_set_id' is set
        if ('option_set_id' not in params or
                params['option_set_id'] is None):
            raise ValueError("Missing the required parameter `option_set_id` when calling `get_option_set_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_set_id' in params:
            path_params['optionSetId'] = params['option_set_id']


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
            '/optionSets/{optionSetId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OptionSet',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_option_sets(cls, **kwargs):
        """List OptionSets

        Return a list of OptionSets
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_option_sets(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[OptionSet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_option_sets_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_option_sets_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_option_sets_with_http_info(cls, **kwargs):
        """List OptionSets

        Return a list of OptionSets
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_option_sets_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[OptionSet]
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
            '/optionSets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[OptionSet]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_option_set_by_id(cls, option_set_id, option_set, **kwargs):
        """Replace OptionSet

        Replace all attributes of OptionSet
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_option_set_by_id(option_set_id, option_set, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_set_id: ID of optionSet to replace (required)
        :param OptionSet option_set: Attributes of optionSet to replace (required)
        :return: OptionSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_option_set_by_id_with_http_info(option_set_id, option_set, **kwargs)
        else:
            (data) = cls._replace_option_set_by_id_with_http_info(option_set_id, option_set, **kwargs)
            return data

    @classmethod
    def _replace_option_set_by_id_with_http_info(cls, option_set_id, option_set, **kwargs):
        """Replace OptionSet

        Replace all attributes of OptionSet
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_option_set_by_id_with_http_info(option_set_id, option_set, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_set_id: ID of optionSet to replace (required)
        :param OptionSet option_set: Attributes of optionSet to replace (required)
        :return: OptionSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_set_id', 'option_set']
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
        # verify the required parameter 'option_set_id' is set
        if ('option_set_id' not in params or
                params['option_set_id'] is None):
            raise ValueError("Missing the required parameter `option_set_id` when calling `replace_option_set_by_id`")
        # verify the required parameter 'option_set' is set
        if ('option_set' not in params or
                params['option_set'] is None):
            raise ValueError("Missing the required parameter `option_set` when calling `replace_option_set_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_set_id' in params:
            path_params['optionSetId'] = params['option_set_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'option_set' in params:
            body_params = params['option_set']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/optionSets/{optionSetId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OptionSet',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_option_set_by_id(cls, option_set_id, option_set, **kwargs):
        """Update OptionSet

        Update attributes of OptionSet
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_option_set_by_id(option_set_id, option_set, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_set_id: ID of optionSet to update. (required)
        :param OptionSet option_set: Attributes of optionSet to update. (required)
        :return: OptionSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_option_set_by_id_with_http_info(option_set_id, option_set, **kwargs)
        else:
            (data) = cls._update_option_set_by_id_with_http_info(option_set_id, option_set, **kwargs)
            return data

    @classmethod
    def _update_option_set_by_id_with_http_info(cls, option_set_id, option_set, **kwargs):
        """Update OptionSet

        Update attributes of OptionSet
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_option_set_by_id_with_http_info(option_set_id, option_set, async=True)
        >>> result = thread.get()

        :param async bool
        :param str option_set_id: ID of optionSet to update. (required)
        :param OptionSet option_set: Attributes of optionSet to update. (required)
        :return: OptionSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_set_id', 'option_set']
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
        # verify the required parameter 'option_set_id' is set
        if ('option_set_id' not in params or
                params['option_set_id'] is None):
            raise ValueError("Missing the required parameter `option_set_id` when calling `update_option_set_by_id`")
        # verify the required parameter 'option_set' is set
        if ('option_set' not in params or
                params['option_set'] is None):
            raise ValueError("Missing the required parameter `option_set` when calling `update_option_set_by_id`")

        collection_formats = {}

        path_params = {}
        if 'option_set_id' in params:
            path_params['optionSetId'] = params['option_set_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'option_set' in params:
            body_params = params['option_set']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/optionSets/{optionSetId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OptionSet',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
