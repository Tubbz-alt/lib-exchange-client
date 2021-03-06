# coding: utf-8

"""
    Blockchain.com Exchange REST API

    ## Introduction Welcome to Blockchain.com's Exchange API and developer documentation. \\ These documents detail and give examples of various functionality offered by the API such as receiving real time market data, requesting balance information and performing trades. ## To Get Started Create or log into your existing Blockchain.com Exchange account \\ Select API from the drop down menu \\ Fill out form and click “Create New API Key Now” \\ Once generated you can view your keys under API Settings. \\ Please be aware that the API key can only be used once it was verified via email.  The API key must be set via the \\ `X-API-Token`\\ header.  The base URL to be used for all calls is \\ `https://api.blockchain.com/v3/exchange`  Autogenerated clients for this API can be found [here](https://github.com/blockchain/lib-exchange-client).   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class SymbolStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'base_currency': 'str',
        'base_currency_scale': 'int',
        'counter_currency': 'str',
        'counter_currency_scale': 'int',
        'min_price_increment': 'int',
        'min_price_increment_scale': 'int',
        'min_order_size': 'int',
        'min_order_size_scale': 'int',
        'max_order_size': 'int',
        'max_order_size_scale': 'int',
        'lot_size': 'int',
        'lot_size_scale': 'int',
        'status': 'str',
        'id': 'int',
        'auction_price': 'float',
        'auction_size': 'float',
        'auction_time': 'str',
        'imbalance': 'float'
    }

    attribute_map = {
        'base_currency': 'base_currency',
        'base_currency_scale': 'base_currency_scale',
        'counter_currency': 'counter_currency',
        'counter_currency_scale': 'counter_currency_scale',
        'min_price_increment': 'min_price_increment',
        'min_price_increment_scale': 'min_price_increment_scale',
        'min_order_size': 'min_order_size',
        'min_order_size_scale': 'min_order_size_scale',
        'max_order_size': 'max_order_size',
        'max_order_size_scale': 'max_order_size_scale',
        'lot_size': 'lot_size',
        'lot_size_scale': 'lot_size_scale',
        'status': 'status',
        'id': 'id',
        'auction_price': 'auction_price',
        'auction_size': 'auction_size',
        'auction_time': 'auction_time',
        'imbalance': 'imbalance'
    }

    def __init__(self, base_currency=None, base_currency_scale=None, counter_currency=None, counter_currency_scale=None, min_price_increment=None, min_price_increment_scale=None, min_order_size=None, min_order_size_scale=None, max_order_size=None, max_order_size_scale=None, lot_size=None, lot_size_scale=None, status=None, id=None, auction_price=None, auction_size=None, auction_time=None, imbalance=None, local_vars_configuration=None):  # noqa: E501
        """SymbolStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base_currency = None
        self._base_currency_scale = None
        self._counter_currency = None
        self._counter_currency_scale = None
        self._min_price_increment = None
        self._min_price_increment_scale = None
        self._min_order_size = None
        self._min_order_size_scale = None
        self._max_order_size = None
        self._max_order_size_scale = None
        self._lot_size = None
        self._lot_size_scale = None
        self._status = None
        self._id = None
        self._auction_price = None
        self._auction_size = None
        self._auction_time = None
        self._imbalance = None
        self.discriminator = None

        if base_currency is not None:
            self.base_currency = base_currency
        if base_currency_scale is not None:
            self.base_currency_scale = base_currency_scale
        if counter_currency is not None:
            self.counter_currency = counter_currency
        if counter_currency_scale is not None:
            self.counter_currency_scale = counter_currency_scale
        if min_price_increment is not None:
            self.min_price_increment = min_price_increment
        if min_price_increment_scale is not None:
            self.min_price_increment_scale = min_price_increment_scale
        if min_order_size is not None:
            self.min_order_size = min_order_size
        if min_order_size_scale is not None:
            self.min_order_size_scale = min_order_size_scale
        if max_order_size is not None:
            self.max_order_size = max_order_size
        if max_order_size_scale is not None:
            self.max_order_size_scale = max_order_size_scale
        if lot_size is not None:
            self.lot_size = lot_size
        if lot_size_scale is not None:
            self.lot_size_scale = lot_size_scale
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if auction_price is not None:
            self.auction_price = auction_price
        if auction_size is not None:
            self.auction_size = auction_size
        if auction_time is not None:
            self.auction_time = auction_time
        if imbalance is not None:
            self.imbalance = imbalance

    @property
    def base_currency(self):
        """Gets the base_currency of this SymbolStatus.  # noqa: E501

        Blockchain symbol identifier  # noqa: E501

        :return: The base_currency of this SymbolStatus.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this SymbolStatus.

        Blockchain symbol identifier  # noqa: E501

        :param base_currency: The base_currency of this SymbolStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                base_currency is not None and not re.search(r'^[A-Z]{3,5}-[A-Z]{3,5}$', base_currency)):  # noqa: E501
            raise ValueError(r"Invalid value for `base_currency`, must be a follow pattern or equal to `/^[A-Z]{3,5}-[A-Z]{3,5}$/`")  # noqa: E501

        self._base_currency = base_currency

    @property
    def base_currency_scale(self):
        """Gets the base_currency_scale of this SymbolStatus.  # noqa: E501

        The number of decimals the currency can be split in  # noqa: E501

        :return: The base_currency_scale of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._base_currency_scale

    @base_currency_scale.setter
    def base_currency_scale(self, base_currency_scale):
        """Sets the base_currency_scale of this SymbolStatus.

        The number of decimals the currency can be split in  # noqa: E501

        :param base_currency_scale: The base_currency_scale of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._base_currency_scale = base_currency_scale

    @property
    def counter_currency(self):
        """Gets the counter_currency of this SymbolStatus.  # noqa: E501

        Blockchain symbol identifier  # noqa: E501

        :return: The counter_currency of this SymbolStatus.  # noqa: E501
        :rtype: str
        """
        return self._counter_currency

    @counter_currency.setter
    def counter_currency(self, counter_currency):
        """Sets the counter_currency of this SymbolStatus.

        Blockchain symbol identifier  # noqa: E501

        :param counter_currency: The counter_currency of this SymbolStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                counter_currency is not None and not re.search(r'^[A-Z]{3,5}-[A-Z]{3,5}$', counter_currency)):  # noqa: E501
            raise ValueError(r"Invalid value for `counter_currency`, must be a follow pattern or equal to `/^[A-Z]{3,5}-[A-Z]{3,5}$/`")  # noqa: E501

        self._counter_currency = counter_currency

    @property
    def counter_currency_scale(self):
        """Gets the counter_currency_scale of this SymbolStatus.  # noqa: E501

        The number of decimals the currency can be split in  # noqa: E501

        :return: The counter_currency_scale of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._counter_currency_scale

    @counter_currency_scale.setter
    def counter_currency_scale(self, counter_currency_scale):
        """Sets the counter_currency_scale of this SymbolStatus.

        The number of decimals the currency can be split in  # noqa: E501

        :param counter_currency_scale: The counter_currency_scale of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._counter_currency_scale = counter_currency_scale

    @property
    def min_price_increment(self):
        """Gets the min_price_increment of this SymbolStatus.  # noqa: E501

        The price of the instrument must be a multiple of min_price_increment * (10^-min_price_increment_scale)  # noqa: E501

        :return: The min_price_increment of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._min_price_increment

    @min_price_increment.setter
    def min_price_increment(self, min_price_increment):
        """Sets the min_price_increment of this SymbolStatus.

        The price of the instrument must be a multiple of min_price_increment * (10^-min_price_increment_scale)  # noqa: E501

        :param min_price_increment: The min_price_increment of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._min_price_increment = min_price_increment

    @property
    def min_price_increment_scale(self):
        """Gets the min_price_increment_scale of this SymbolStatus.  # noqa: E501


        :return: The min_price_increment_scale of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._min_price_increment_scale

    @min_price_increment_scale.setter
    def min_price_increment_scale(self, min_price_increment_scale):
        """Sets the min_price_increment_scale of this SymbolStatus.


        :param min_price_increment_scale: The min_price_increment_scale of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._min_price_increment_scale = min_price_increment_scale

    @property
    def min_order_size(self):
        """Gets the min_order_size of this SymbolStatus.  # noqa: E501

        The minimum quantity for an order for this instrument must be min_order_size*(10^-min_order_size_scale)  # noqa: E501

        :return: The min_order_size of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._min_order_size

    @min_order_size.setter
    def min_order_size(self, min_order_size):
        """Sets the min_order_size of this SymbolStatus.

        The minimum quantity for an order for this instrument must be min_order_size*(10^-min_order_size_scale)  # noqa: E501

        :param min_order_size: The min_order_size of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._min_order_size = min_order_size

    @property
    def min_order_size_scale(self):
        """Gets the min_order_size_scale of this SymbolStatus.  # noqa: E501


        :return: The min_order_size_scale of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._min_order_size_scale

    @min_order_size_scale.setter
    def min_order_size_scale(self, min_order_size_scale):
        """Sets the min_order_size_scale of this SymbolStatus.


        :param min_order_size_scale: The min_order_size_scale of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._min_order_size_scale = min_order_size_scale

    @property
    def max_order_size(self):
        """Gets the max_order_size of this SymbolStatus.  # noqa: E501

        The maximum quantity for an order for this instrument is max_order_size*(10^-max_order_size_scale). If this equal to zero, there is no limit  # noqa: E501

        :return: The max_order_size of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._max_order_size

    @max_order_size.setter
    def max_order_size(self, max_order_size):
        """Sets the max_order_size of this SymbolStatus.

        The maximum quantity for an order for this instrument is max_order_size*(10^-max_order_size_scale). If this equal to zero, there is no limit  # noqa: E501

        :param max_order_size: The max_order_size of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._max_order_size = max_order_size

    @property
    def max_order_size_scale(self):
        """Gets the max_order_size_scale of this SymbolStatus.  # noqa: E501


        :return: The max_order_size_scale of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._max_order_size_scale

    @max_order_size_scale.setter
    def max_order_size_scale(self, max_order_size_scale):
        """Sets the max_order_size_scale of this SymbolStatus.


        :param max_order_size_scale: The max_order_size_scale of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._max_order_size_scale = max_order_size_scale

    @property
    def lot_size(self):
        """Gets the lot_size of this SymbolStatus.  # noqa: E501


        :return: The lot_size of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._lot_size

    @lot_size.setter
    def lot_size(self, lot_size):
        """Sets the lot_size of this SymbolStatus.


        :param lot_size: The lot_size of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._lot_size = lot_size

    @property
    def lot_size_scale(self):
        """Gets the lot_size_scale of this SymbolStatus.  # noqa: E501


        :return: The lot_size_scale of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._lot_size_scale

    @lot_size_scale.setter
    def lot_size_scale(self, lot_size_scale):
        """Sets the lot_size_scale of this SymbolStatus.


        :param lot_size_scale: The lot_size_scale of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._lot_size_scale = lot_size_scale

    @property
    def status(self):
        """Gets the status of this SymbolStatus.  # noqa: E501

        Symbol status; open, close, suspend, halt, halt-freeze.  # noqa: E501

        :return: The status of this SymbolStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SymbolStatus.

        Symbol status; open, close, suspend, halt, halt-freeze.  # noqa: E501

        :param status: The status of this SymbolStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "close", "suspend", "halt", "halt-freeze"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def id(self):
        """Gets the id of this SymbolStatus.  # noqa: E501


        :return: The id of this SymbolStatus.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SymbolStatus.


        :param id: The id of this SymbolStatus.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def auction_price(self):
        """Gets the auction_price of this SymbolStatus.  # noqa: E501

        If the symbol is halted and will open on an auction, this will be the opening price.  # noqa: E501

        :return: The auction_price of this SymbolStatus.  # noqa: E501
        :rtype: float
        """
        return self._auction_price

    @auction_price.setter
    def auction_price(self, auction_price):
        """Sets the auction_price of this SymbolStatus.

        If the symbol is halted and will open on an auction, this will be the opening price.  # noqa: E501

        :param auction_price: The auction_price of this SymbolStatus.  # noqa: E501
        :type: float
        """

        self._auction_price = auction_price

    @property
    def auction_size(self):
        """Gets the auction_size of this SymbolStatus.  # noqa: E501

        Opening size  # noqa: E501

        :return: The auction_size of this SymbolStatus.  # noqa: E501
        :rtype: float
        """
        return self._auction_size

    @auction_size.setter
    def auction_size(self, auction_size):
        """Sets the auction_size of this SymbolStatus.

        Opening size  # noqa: E501

        :param auction_size: The auction_size of this SymbolStatus.  # noqa: E501
        :type: float
        """

        self._auction_size = auction_size

    @property
    def auction_time(self):
        """Gets the auction_time of this SymbolStatus.  # noqa: E501

        Opening time in HHMM format  # noqa: E501

        :return: The auction_time of this SymbolStatus.  # noqa: E501
        :rtype: str
        """
        return self._auction_time

    @auction_time.setter
    def auction_time(self, auction_time):
        """Sets the auction_time of this SymbolStatus.

        Opening time in HHMM format  # noqa: E501

        :param auction_time: The auction_time of this SymbolStatus.  # noqa: E501
        :type: str
        """

        self._auction_time = auction_time

    @property
    def imbalance(self):
        """Gets the imbalance of this SymbolStatus.  # noqa: E501

        Auction imbalance. If > 0 then there will be buy orders left over at the auction price. If < 0 then there will be sell orders left over at the auction price.  # noqa: E501

        :return: The imbalance of this SymbolStatus.  # noqa: E501
        :rtype: float
        """
        return self._imbalance

    @imbalance.setter
    def imbalance(self, imbalance):
        """Sets the imbalance of this SymbolStatus.

        Auction imbalance. If > 0 then there will be buy orders left over at the auction price. If < 0 then there will be sell orders left over at the auction price.  # noqa: E501

        :param imbalance: The imbalance of this SymbolStatus.  # noqa: E501
        :type: float
        """

        self._imbalance = imbalance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SymbolStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SymbolStatus):
            return True

        return self.to_dict() != other.to_dict()
