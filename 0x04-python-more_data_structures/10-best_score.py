#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        new_dict = dict(sorted(a_dictionary.items(),
                        key=lambda x: x[1], reverse=True))
        for k, v in new_dict.items():
            return k
