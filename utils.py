import yaml


#   ----- READ FILES -----
def yaml_read(dir): 
    content = yaml.load(open(dir, 'r'), Loader=yaml.FullLoader)
    return content

#   ----- 