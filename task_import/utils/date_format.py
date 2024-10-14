def date_formatter(date_str):
    parts = date_str.split('-')

    if len(parts) ==3 and len(parts[0]) ==4:
        year, month, day = parts
        changed_date = f'{day}-{month}-{year}'

    elif len(parts) ==3 and len(parts[2]) ==4:
        month, day, year = parts
        changed_date =f'{day}-{month}-{year}'  

    else:
        changed_date = "The data format you entered is invalid"

    return changed_date          