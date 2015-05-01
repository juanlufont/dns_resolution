#
# Cookbook Name:: dns_resolution
# Recipe:: default
#
# Copyright 2015, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#
#
# forcing the installation of argparse package
# for RHEL/CentOS systems
when "redhat","centos"
    package "python-argparse" do
        action :install
    end 
end 

cookbook_file "/usr/local/bin/dns_resolution.py" do
      source "resolution.py"
        mode "0755"
end

