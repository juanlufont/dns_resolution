dns_resolution Cookbook
=======================
Chef example cookbook, it performs a basic package dependency check and proceeds to install the Python script resolution.py. This script resolves DNS queries froma given file.


Requirements
------------


#### packages
- `python` - dns_resolution needs python >= 2.7
- `python-argparse` - dns-resolution will check and try to install this package when RHEL/CentOS systems are detected

Attributes
----------

#### dns_resolution::default
<table>
  <tr>
    <th>Key</th>
    <th>Type</th>
    <th>Description</th>
    <th>Default</th>
  </tr>
  <tr>
    <td><tt>['dns_resolution']['bacon']</tt></td>
    <td>Boolean</td>
    <td>whether to include bacon</td>
    <td><tt>true</tt></td>
  </tr>
</table>

Usage
-----
#### dns_resolution::default

Just include `dns_resolution` in your node's `run_list`:

```json
{
  "name":"my_node",
  "run_list": [
    "recipe[dns_resolution]"
  ]
}
```

Contributing
------------

1. Fork the repository on Github
2. Create a named feature branch (like `add_component_x`)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github

License and Authors
-------------------
Authors: Juan Luis Font
