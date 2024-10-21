def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as data_file:
            employees_data = data_file.readlines()
            sum = 0
            for data in employees_data:
                sum += float(data.strip().split(",")[1])
            return sum, sum / len(employees_data)
    except FileNotFoundError:
        print("Incorrect path to file or file does not exist")
    except UnicodeDecodeError:
        print("Incorrect file format")
    except IOError:
        print("Could not read file")
    except ValueError:
        print("Incorrect salary value format")
    except IndexError:
        print("Incorrect file data format")
    return (0, 0)


def total_salary2(path):
    with open(path, "r", encoding="utf-8") as data_file:
        employees_data = data_file.readlines()
        sum = 0
        for data in employees_data:
            sum += float(data.strip().split(",")[1])
        return sum, sum / len(employees_data)




total, average = total_salary("task_1/test_data.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
