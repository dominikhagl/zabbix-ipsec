# zabbix-ipsec

## Zabbix template for monitoring Strongswan IPsec connections

Originally written by andre@schild.ws, adapted by Dominik Hagl

####Prerequirements
To run all checks fping and python must be installed. The paths in the scripts
are adapted to the default CentOS 7 installation directories.

####Installation
The configuration files and scripts have to be placed in the correct
directories as shown in the repository.
The locations are for CentOs 7 with Zabbix 3.2.x installed.

######"Template App IPSEC VPN.xml"
    -> Import this template on your Zabbix server and assign it to your
       monitored IPSEC gateways

######"/etc/zabbix/ipsec.conf"
    -> Place this file on your IPSEC gateway and modify it accordingly.
       This is the tunnel definition to be monitored.
       It is used for autodiscovery.

######"/etc/zabbix/zabbix_agentd.d/userparameter_ipsec.conf"
    -> Place in the file on your IPSEC gateway no modification needed, 
       unless you place the external script in another location.

######"/etc/sudoers.d/zabbix_ipsec"
    -> Make sure to have sudo installed on your IPsec gateway.
       The Zabbix agent does not have the required privileges to monitor
       the ipsec status. With this sudo config we allow it.

######"/var/lib/zabbix/ipsec/scripts/discover_conns.py"
    -> The script scans /etc/strongswan/ipsec.conf for connections.
       If you place this script in another location, you will have to
       change sudoers.d and the zabbix files accordingly

######"/var/lib/zabbix/ipsec/scripts/check_ipsec.sh"
    -> The script doing the actual ipsec tests.
       If you place this script in another location, you will have to
       change sudoers.d and the zabbix files accordingly

######Supported macros

   #TUNNEL        is the name of your ipsec tunnel,
                  it has to match the name used in your ipsec config

   #TARGETIP      Use this IP as ping target to check if the tunnel is running
                  and for monitoring the RTT

   #SOURCEIP      Use this IP as ping source IP to check if the tunnel is running
                  and for monitoring the RTT
                  Since VPN gateways ususally have multiple interfaces and
                  IP addresses assigned, you have to define the source IP

   #RTT_TIME_WARN Trigger a warning if the round trip times between 
                  #SOURCEIP and #TARGETIP are higher than this value

   #RTT_TIME_WERR Trigger a error if the round trip times between 
                  #SOURCEIP and #TARGETIP are higher than this value

