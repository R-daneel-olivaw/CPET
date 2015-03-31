

def generate_op(o_dict, file_path):
    
    with open(file_path, "w+") as text_file:
        for ko, vo in o_dict.items():
            print(ko, file=text_file)   
            for ki, vi in vo.items():
                print(ki + '\t' + " ".join(map(str, vi)), file=text_file)
