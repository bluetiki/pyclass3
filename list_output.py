#!/usr/bin/env python
import yaml
import json
import random
from pprint import pprint as pp

#generate a list of length num_strings of strings that are composed of random sample from letters and of random lenth betwwen min_length and max_length
def generate_strings(num_strings,min_length=3,max_length=10):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    str_list = []
    for i in range(0,num_strings):
        str_gen = ''
        for j in range(0,random.randint(min_length,max_length)):
            str_gen = str_gen + random.choice(letters)
        str_list.append(str_gen)
    return str_list

#generate a list of length num_elements of random ints between 0 and upper_bound
def generate_ints(num_elements,upper_bound=1000):
    int_list = []
    for i in range(0,num_elements):
        int_list.append(random.randint(0,upper_bound))
    return int_list

#generate a list containing num_items of random numbers, random strings, then a dict of random strings with key values of random numbers
def generate_list(num_items):
    my_list = []
    my_list = generate_ints(num_items,10000) + generate_strings(num_items)
    my_list.append({})
    for i in range(0,num_items):
        my_list[-1] [str(generate_strings(1)).lstrip("['").rstrip("']")] = str(generate_ints(1,1000000))
    return my_list

#convert list to json and yaml formats and output with filename file_name
def output_files(file_name,my_list):
	with open(file_name + ".yml", "w") as f:
		f.write(yaml.dump(my_list, default_flow_style=False))
	with open(file_name + ".json", "w") as f:
		f.write(json.dumps(my_list))

#read json file
def read_json_file(json_file):
	with open(json_file, "r") as f:
		return json.load(f)

#read yaml file
def read_yaml_file(yaml_file):
	with open(yaml_file, "r") as f:
		return yaml.load(f)

def main():
    file_name = str(generate_strings(1)).lstrip("['").rstrip("']")
    print (type(file_name))
    print (file_name)
    output_files(file_name,generate_list(10))
    pp(read_json_file(file_name + ".json"))
    pp(read_yaml_file(file_name + ".yml"))
    

if __name__ == "__main__":
    main()
