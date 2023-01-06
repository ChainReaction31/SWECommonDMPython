from enum import Enum


class ByteEncoding(Enum):
    RAW = 'raw'
    BASE64 = 'base64'


class ByteOrder(Enum):
    BIG_ENDIAN = 'bigEndian'
    LITTLE_ENDIAN = 'littleEndian'


class TextEncoding:
    """
    The “TextEncoding” class defines a method allowing encoding arbitrarily complex data
    using a text based delimiter separated values (DSV) format. -  OGC 08-094r1 pg. 59
    """

    token_sep = ','
    block_sep = '\n'
    decimal_sep = '.'
    collapse_white_spaces = False

    def __init__(self, token=',', block='\n', decimal='.', collapse_white_space=False):
        self.token_sep = token
        self.block_sep = block
        self.decimal_sep = decimal
        self.collapse_white_spaces = collapse_white_space


class BinaryEncoding:
    """
    The “BinaryEncoding” class defines a method that allows encoding complex structured
    data using primitive data types encoded directly at the byte level, in the same way that
    they are usually represented in memory.
    The binary encoding method can lead to very compact streams that can be optimized for
    efficient parsing and fast random access. However, this comes with the lack of human
    readability of the data and sometimes lack of compatibility with other software (i.e.
    software that is not SWE Common enabled). - OGC 08-094r1 pg. 62
    """

    byte_length: int
    byte_encoding: ByteEncoding
    byte_order: ByteOrder
    member = None

    def __init__(self, byte_encoding: ByteEncoding = ByteEncoding.RAW, byte_order: ByteOrder = ByteOrder.LITTLE_ENDIAN,
                 byte_length: int = None):
        """
        :param byte_encoding: whether the stream is raw binary, base64, or some other encoding later added
        :param byte_order: The endianness of the bytes
        :param byte_length: optional, useful when data size is known in advance for more efficient memory allocation
        """
        self.byte_encoding = byte_encoding
        self.byte_order = byte_order
        self.byte_length = byte_length
