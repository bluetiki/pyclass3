#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cfg_obj = CiscoConfParse("cisco_ipsec.txt")

crypto_maps = cfg_obj.find_objects(r"^crypto map")

print ("Part 1:")
for i in crypto_maps:
    print (i.text)
    for j in i.all_children:
        print (j.text)


print ("\n\nPart2:")
for i in crypto_maps:
    for j in i.all_children:
        if j.text == " set pfs group2":
            print (j.parent.text)
            for k in j.parent.all_children:
                print (k.text)

print ("\n\nPart 3:")
no_aes = cfg_obj.find_objects_wo_child(parentspec=r"^crypto map", childspec=r"^ set transform-set AES")
for i in no_aes:
    print (i.text)
    for j in i.all_children:
           print (j.text)

