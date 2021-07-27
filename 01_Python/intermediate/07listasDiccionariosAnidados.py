def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname" : "sebastian", "lastname" : "calderon"}

    super_list = [
        {"firstname" : "sebastian", "lastname" : "calderon"},
        {"firstname" : "karelys", "lastname" : "calderon"},
        {"firstname" : "jorge", "lastname" : "calderon"},
        {"firstname" : "martha", "lastname" : "araque"},
        {"firstname" : "terry", "lastname" : "calderon"},
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5,6,7,8,9],
        "integer_nums" : [-3,-2,-1,0,1,2,3],
        "floating_nums" : [1.1, 1.2, 3.1]
    }

    for key, value in super_dict.items():
        print(key, " - ", value)
    
    for  in super_list.items():
        print(key, " - ", value)

if __name__ == "__main__":
    run()