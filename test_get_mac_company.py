from get_mac_company import get_mac_company

def test_get_mac_company():
  # Test with a valid MAC address
  mac_address = '00:00:00:00:00:00'
  api_key = 'at_mai6T26AHo5JcXCD8d7qOkfykE3Kc'
  expected_vendor = 'Xerox Corp'
  assert get_mac_company(mac_address, api_key) == expected_vendor

  # Test with an invalid MAC address
  mac_address = 'invalid:mac:address'
  expected_error = 'Invalid MAC or OUI address was received.'
  assert get_mac_company(mac_address, api_key) == expected_error
