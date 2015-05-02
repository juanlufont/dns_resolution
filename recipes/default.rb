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
    source "dns_resolution.py"
        mode "0755"
        owner "root"
        group "root"
end

cookbook_file "/usr/local/share/query.txt" do
    source "query.txt"
        mode "0644"
        owner "root"
        group "root"
end

python "dns_resolution.py" do
    command "/usr/local/bin/dns_resolution.py"
    attribute "/usr/local/share/query.txt -o resolution.txt"
    cwd "/root/"
    action :run
end
