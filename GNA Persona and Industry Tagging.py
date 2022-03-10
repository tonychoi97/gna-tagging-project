import csv
import re
from collections import Counter
    
def main():
    # Opening csv file using DictReader
    persona_list = []
    industry_list = []
    with open('SegmentMembers.csv') as csv_file:
        reader = csv.DictReader(csv_file, delimiter = ',')
        for row in reader:
            persona_list.append(row['GNA Persona'])
            industry_list.append(row['GNA Industry'])
            
    # https://www.adamsmith.haus/python/answers/how-to-remove-empty-strings-from-a-list-of-strings-in-python
    # "A lambda function is a single-line function declared with no name, which can have any number of arguments, but it can only have one expression."
    # Filters out cells with no values inside
    filter_object_blank = filter(lambda x: x != '', persona_list)
    persona_list_filt = list(filter_object_blank)
    
    # Filters out cells with 'Please Select' as a value
    filter_object_ps = filter(lambda x: x != 'Please Select', persona_list_filt)
    persona_list_filt = list(filter_object_ps)
    
    persona_list_to_dict = Counter(persona_list_filt)
    for value, count in persona_list_to_dict.most_common():
        print(value, count)
        
    print()
    
    string = ' '.join(industry_list)
    new_list = re.split('::| |;|:', string)
    
    # Filters out cells with no values inside
    filter_object_blank = filter(lambda x: x != '', new_list)
    industry_list_filt = list(filter_object_blank)
    
    # Filters out cells with 'Please Select' as a value
    filter_object_ps = filter(lambda x: x != 'Please Select', industry_list_filt)
    industry_list_filt = list(filter_object_ps)
    
    # (THIS METHOD IS FOR LISTS, SAVE THIS FOR REFERENCE)
    # remove_whitespace = [x.strip() for x in industry_list]
        
    industry_list_to_dict = Counter(industry_list_filt)
    for value, count in industry_list_to_dict.most_common():
        print(value, count)
        
if __name__ == '__main__':
    main()
    
