# reading input file
path_file = "input-file.txt"
file = open(path_file, "r")
content_file = file.read()
# print(content_file)

# convert time format to decimal format
def time_to_decimal(t):
    (h, m) = t.split(":")
    result = (int(h) * 3600 + int(m) * 60) / 3600
    #     print(result)
    return result


# compute the value per hour earned according to the schedule
def val_hr(day, t1, t2):

    week_days = ["MO", "TU", "WE", "TH", "FR"]
    weekend_days = ["SA", "SU"]

    if (0 < t1 <= 9) and (0 < t2 <= 9) and week_days.count(day):
        value_per_hr = 25
    elif (9 < t1 <= 18) and (9 < t2 <= 18) and week_days.count(day):
        value_per_hr = 15
    elif (
        ((18 < t1 <= 23.99) and (18 < t2 <= 23.99)) or (t1 > 18 and t2 == 0)
    ) and week_days.count(day):
        value_per_hr = 20
    elif (0 < t1 <= 9) and (0 < t2 <= 9) and weekend_days.count(day):
        value_per_hr = 30
        return value_per_hr
    elif (9 < t1 <= 18) and (9 < t2 <= 18) and weekend_days.count(day):
        value_per_hr = 20
    elif (
        ((18 < t1 <= 23.99) and (18 < t2 <= 23.99)) or (t1 > 18 and t2 == 0)
    ) and weekend_days.count(day):
        value_per_hr = 25

    if (0 <= t2 <= 1) and not (0 <= t1 <= 1):
        t2 += 24
    hrs_day = t2 - t1

    try:
        value_per_hr
    except NameError:
        print("Variable value_per_hr is not defined.")
        print("Check if schedule is selected according to the three options for hours")
        print(
            "The schedule with the problem is in the following data: t1 = {t1}, t2 = {t2}, day = {day} and name = {name}".format(
                t1=t1, t2=t2, day=day, name=name
            )
        )
    except:
        print("Something else went wrong")

    return value_per_hr, hrs_day


# compute the pay of persons according to the input file
def main():

    # structure the data into a dictionary
    arr_str = content_file.split("\n")
    content_dict = {}
    arr_name = []
    # print(arr_str)

    for i in arr_str:

        index_name = i.index("=")
        global name
        name = i[:index_name]
        arr_name.append(name)
        # print(name)

        content_dict[name] = {}

        if "MO" in i:
            index_monday = i.index("MO")
            monday_hr = i[index_monday + 2 : index_monday + 13]
            content_dict[name].update({"MO": monday_hr})

        if "TU" in i:
            index_tuesday = i.index("TU")
            tuesday_hr = i[index_tuesday + 2 : index_tuesday + 13]
            content_dict[name].update({"TU": tuesday_hr})

        if "WE" in i:
            index_wednesday = i.index("WE")
            wednesday_hr = i[index_wednesday + 2 : index_wednesday + 13]
            content_dict[name].update({"WE": wednesday_hr})

        if "TH" in i:
            index_thursday = i.index("TH")
            thursday_hr = i[index_thursday + 2 : index_thursday + 13]
            content_dict[name].update({"TH": thursday_hr})

        if "FR" in i:
            index_friday = i.index("FR")
            friday_hr = i[index_friday + 2 : index_friday + 13]
            content_dict[name].update({"FR": friday_hr})

        if "SA" in i:
            index_saturday = i.index("SA")
            saturday_hr = i[index_saturday + 2 : index_saturday + 13]
            content_dict[name].update({"SA": saturday_hr})

        if "SU" in i:
            index_sunday = i.index("SU")
            sunday_hr = i[index_sunday + 2 : index_sunday + 13]
            content_dict[name].update({"SU": sunday_hr})

    # print(content_dict)

    # adding pay per day and total pay to dictionary
    for name in arr_name:
        total_pay = 0
        if "MO" in content_dict[name]:
            (t1_monday, t2_monday) = content_dict[name]["MO"].split("-")

            t1_mon = time_to_decimal(t1_monday)
            t2_mon = time_to_decimal(t2_monday)
            value_per_hr, hrs_monday = val_hr("MO", t1_mon, t2_mon)

            pay_monday = hrs_monday * value_per_hr
            content_dict[name].update({"PAY_MO": pay_monday})
            total_pay += pay_monday

        if "TU" in content_dict[name]:
            (t1_tuesday, t2_tuesday) = content_dict[name]["TU"].split("-")

            t1_tue = time_to_decimal(t1_tuesday)
            t2_tue = time_to_decimal(t2_tuesday)
            value_per_hr, hrs_tuesday = val_hr("TU", t1_tue, t2_tue)

            pay_tuesday = hrs_tuesday * value_per_hr
            content_dict[name].update({"PAY_TU": pay_tuesday})
            total_pay += pay_tuesday

        if "WE" in content_dict[name]:
            (t1_wednesday, t2_wednesday) = content_dict[name]["WE"].split("-")

            t1_wed = time_to_decimal(t1_wednesday)
            t2_wed = time_to_decimal(t2_wednesday)
            value_per_hr, hrs_wednesday = val_hr("WE", t1_wed, t2_wed)

            pay_wednesday = hrs_wednesday * value_per_hr
            content_dict[name].update({"PAY_WE": pay_wednesday})
            total_pay += pay_wednesday

        if "TH" in content_dict[name]:
            (t1_thursday, t2_thursday) = content_dict[name]["TH"].split("-")

            t1_thu = time_to_decimal(t1_thursday)
            t2_thu = time_to_decimal(t2_thursday)
            value_per_hr, hrs_thursday = val_hr("TH", t1_thu, t2_thu)

            pay_thursday = hrs_thursday * value_per_hr
            content_dict[name].update({"PAY_TH": pay_thursday})
            total_pay += pay_thursday

        if "FR" in content_dict[name]:
            (t1_friday, t2_friday) = content_dict[name]["FR"].split("-")

            t1_fri = time_to_decimal(t1_friday)
            t2_fri = time_to_decimal(t2_friday)
            value_per_hr, hrs_friday = val_hr("FR", t1_fri, t2_fri)

            pay_friday = hrs_friday * value_per_hr
            content_dict[name].update({"PAY_FR": pay_friday})
            total_pay += pay_friday

        if "SA" in content_dict[name]:
            (t1_saturday, t2_saturday) = content_dict[name]["SA"].split("-")

            t1_sat = time_to_decimal(t1_saturday)
            t2_sat = time_to_decimal(t2_saturday)
            value_per_hr, hrs_saturday = val_hr("SA", t1_sat, t2_sat)

            pay_saturday = hrs_saturday * value_per_hr
            content_dict[name].update({"PAY_SA": pay_saturday})
            total_pay += pay_saturday

        if "SU" in content_dict[name]:
            (t1_sunday, t2_sunday) = content_dict[name]["SU"].split("-")

            t1_sun = time_to_decimal(t1_sunday)
            t2_sun = time_to_decimal(t2_sunday)
            value_per_hr, hrs_sunday = val_hr("SU", t1_sun, t2_sun)

            pay_sunday = hrs_sunday * value_per_hr
            content_dict[name].update({"PAY_SU": pay_sunday})
            total_pay += pay_sunday

        content_dict[name].update({"TOTAL_PAY": total_pay})
        print(
            "The amount to pay {name} is: {tot_pay} USD".format(
                name=name, tot_pay=total_pay
            )
        )

    # print(content_dict)


if __name__ == "__main__":
    main()
