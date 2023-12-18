from prettytable import PrettyTable

def get_table_device_list(devices):

    pt = PrettyTable()
    pt.field_names = ["Nombre", "IP", "Tipo"]
    
    for device in devices:
        pt.add_row([device['name'], device['ip'], device['type']])
    print(pt)
