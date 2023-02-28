#!/usr/bin/env python3
# 
import os
import json

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", action="store_true", help="Search only in keys of the JSON object")
    parser.add_argument("-v", action="store_true", help="Search only in values of the JSON object")
    parser.add_argument("-x", action="store_true", help="Ignore lines containing invalid JSON (see section below)")
    parser.add_argument("-i", action="store_true", help="Case insensitive search")
    parser.add_argument("-c", action="store_true", help="Show only the total number of lines matched instead of printing the matched lines")
    parser.add_argument("-d", action="store_true", help="Print only the lines which DO not match the pattern provided")
    parser.add_argument("pattern", help="add value")
    parser.add_argument('filename', type=argparse.FileType('r'))
    
    args = parser.parse_args()
    pattern = args.pattern
    file = args.filename
    tweets = []
    errors = []
    lines = 0
    ans = []
    show_error = True
    keys = []
    values = []
    not_matched = []
    if args.i :
        pattern = pattern.lower()

    for line in open(file.name, 'r'):
        
        try :
            json_file = json.loads(line)
        except :
            if args.x :
                continue
            else :
                errors.append(lines+1)
                break
                
                
        tweets.append(json.loads(line))

        if args.k :
            found = False
            for val in json_file.keys() :
                if args.i :
                    val = str(val).lower()
                if pattern in str(val) :
                    ans.append(json_file)
                    found = True
                    break
            if found == False :
                not_matched.append(json_file)
        
        elif args.v :
            found = False

            for val in json_file.values() :
                if args.i :
                    val = str(val).lower()
                if pattern in str(val) :
                    ans.append(json_file)
                    found = True
                    break
            if found == False :
                not_matched.append(json_file)
        else :
            found = False
            for val in json_file.keys() :
                if args.i :
                    val = str(val).lower()
                if pattern in str(val) :
                    ans.append(json_file)
                    found = True
                    break
            if found == False :
                for val in json_file.values() :
                    if args.i :
                        val = str(val).lower()
                    if pattern in str(val) :
                        ans.append(json_file)
                        found = True
                        break
            if found == False :
                not_matched.append(json_file)
        lines+=1

    if args.c :
        print(len(ans))
    elif args.d :
        for i in not_matched :
            print(i)
    else :
        for i in ans :
            print(i)

    if len(errors)>0 :
        print(f"Invalid JSON on line number {errors[0]}")
            

