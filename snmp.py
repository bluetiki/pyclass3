#!/usr/bin/env python

import pysnmp
import snmp_helper

def main():

    OIDs = ['1.3.6.1.2.1.1.1.0', '1.3.6.1.2.1.1.5.0']
    community_str = 'galileo'

    pynet_rtr1 = ('184.105.247.70', community_str, '161')
    pynet_rtr2 = ('184.105.247.71', community_str, '161')

    routers = [pynet_rtr1, pynet_rtr2]
    rtr_names = ['pynet_rtr1', 'pynet_rtr2']

    count = 0
    for i in routers:
        for j in OIDs:
            out = snmp_helper.snmp_get_oid(i, j)
            print ("this is OID " + j + " for " + rtr_names[count]) 
            print (snmp_helper.snmp_extract(out) + '\n')
        count += 1

if __name__ == "__main__":
    main()
