# encoding: utf-8
# module binascii
# from (built-in)
# by generator 1.147
""" Conversion between binary data and ASCII """
# no imports

# functions

def a2b_base64(*args, **kwargs): # real signature unknown
    """ Decode a line of base64 data. """
    pass

def a2b_hex(*args, **kwargs): # real signature unknown
    """
    Binary data of hexadecimal representation.
    
    hexstr must contain an even number of hex digits (upper or lower case).
    This function is also available as "unhexlify()".
    """
    pass

def a2b_hqx(*args, **kwargs): # real signature unknown
    """ Decode .hqx coding. """
    pass

def a2b_qp(*args, **kwargs): # real signature unknown
    """ Decode a string of qp-encoded data. """
    pass

def a2b_uu(*args, **kwargs): # real signature unknown
    """ Decode a line of uuencoded data. """
    pass

def b2a_base64(*args, **kwargs): # real signature unknown
    """ Base64-code line of data. """
    pass

def b2a_hex(*args, **kwargs): # real signature unknown
    """
    Hexadecimal representation of binary data.
    
    The return value is a bytes object.  This function is also
    available as "hexlify()".
    """
    pass

def b2a_hqx(*args, **kwargs): # real signature unknown
    """ Encode .hqx data. """
    pass

def b2a_qp(*args, **kwargs): # real signature unknown
    """
    Encode a string using quoted-printable encoding.
    
    On encoding, when istext is set, newlines are not encoded, and white
    space at end of lines is.  When istext is not set, \r and \n (CR/LF)
    are both encoded.  When quotetabs is set, space and tabs are encoded.
    """
    pass

def b2a_uu(*args, **kwargs): # real signature unknown
    """ Uuencode line of data. """
    pass

def crc32(*args, **kwargs): # real signature unknown
    """ Compute CRC-32 incrementally. """
    pass

def crc_hqx(*args, **kwargs): # real signature unknown
    """ Compute CRC-CCITT incrementally. """
    pass

def hexlify(data): # known case of binascii.hexlify
    """
    Hexadecimal representation of binary data.
    
    The return value is a bytes object.
    """
    return b""

def rlecode_hqx(*args, **kwargs): # real signature unknown
    """ Binhex RLE-code binary data. """
    pass

def rledecode_hqx(*args, **kwargs): # real signature unknown
    """ Decode hexbin RLE-coded string. """
    pass

def unhexlify(hexstr): # known case of binascii.unhexlify
    """
    Binary data of hexadecimal representation.
    
    hexstr must contain an even number of hex digits (upper or lower case).
    """
    return b""

# classes

class Error(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Incomplete(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0x000001ED907815C0>, 'find_spec': <classmethod object at 0x000001ED907815F8>, 'find_module': <classmethod object at 0x000001ED90781630>, 'create_module': <classmethod object at 0x000001ED90781668>, 'exec_module': <classmethod object at 0x000001ED907816A0>, 'get_code': <classmethod object at 0x000001ED90781710>, 'get_source': <classmethod object at 0x000001ED90781780>, 'is_package': <classmethod object at 0x000001ED907817F0>, 'load_module': <classmethod object at 0x000001ED90781828>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='binascii', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

