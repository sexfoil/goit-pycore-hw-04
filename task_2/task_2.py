def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as data_file:
            cats_info_array = []
            for data in data_file.readlines():
                cat_data = data.strip().split(",")
                
                id = cat_data[0]
                name = cat_data[1]
                age = int(cat_data[2])
                
                cat = {"id": id, "name": name, "age": str(age)}

                cats_info_array.append(cat)

            return cats_info_array
    except FileNotFoundError:
        print("Incorrect path to file or file does not exist")
    except UnicodeDecodeError:
        print("Incorrect file format")
    except IOError:
        print("Could not read file")
    except ValueError:
        print("Incorrect age value format")
    except IndexError:
        print("Incorrect file data format")
    return dict()


cats_info = get_cats_info("task_2/cats_file.txt")
print(cats_info)