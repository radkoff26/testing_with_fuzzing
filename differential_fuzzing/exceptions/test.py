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
  if is_valid_stringtools and not is_valid_validators:
    raise Exception("stringtools: True; validators: False; input: " + ip)

input = frelatage.Input(value='0::0')
f = frelatage.Fuzzer(test_validate_ipv6, [[input]])
f.fuzz()