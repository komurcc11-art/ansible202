#!/usr/bin/python3
"""Alta3 Research || rzfeeser@alta3.com
   Dynamic Inventory script"""


#for accepting arguments form user at cli
import argparse

# required for working with JSON
import json

def main():
  #this is what will be returned
  inventory = {}

  #called with --list
  if args.list:
    inventory = example_inventory()

  #called with --host
  elif args.host:
    # not implemented since we return _meta info --list
    # lets put api request logic here
    inventory = empty_inventory()

  else:
    inventory = empty_inventory()


  # print the result inventory
  print(json.dumps(inventory))

def example_inventory():
  return {
        'group': {
            'hosts': ['bender', 'fry'],
            'vars': {
                'example_var1': 'proxyeast',
                'example_var2': 'proxywest',
                'ansible_ssh_pass': 'alta3',
                'ansible_python_interpreter': '/usr/bin/python3'
            }
        },
        '_meta': {
            'hostvars': {
                'bender': {
                    'ansible_user': 'bender',
                    'ansible_host': '10.10.2.3'
                },
                'fry': {
                    'ansible_user': 'fry',
                    'ansible_host': '10.10.2.4'
                }
            }
        }
    }

# Empty inventory for testing.
def empty_inventory():
    return {'_meta': {'hostvars': {}}}


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--list', action = 'store_true')
  parser.add_argument('--host', action = 'store')
  args = parser.parse_args()
  main()
