import frelatage

from validators import ip_address, ValidationFailure
from stringtools.validators import Validator


def is_result_valid(result):
  if type(result) == ValidationFailure:
    return False
  elif type(result) == bool:
    return result
  return False

def test_validate_ipv6(ip):
  is_valid_stringtools = Validator.validate_ipv6(ip)
  is_valid_validators = is_result_valid(ip_address.ipv6(ip))
  assert is_valid_validators == is_valid_stringtools

input = frelatage.Input(value='0::0')
f = frelatage.Fuzzer(test_validate_ipv6, [[input]])
f.fuzz()