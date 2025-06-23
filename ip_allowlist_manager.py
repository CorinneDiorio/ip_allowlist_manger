def update_allow_list(allow_file, remove_list):
    # Read the current list of IPs
    with open(allow_file, 'r') as file:
        ip_addresses = file.read().split()

    # Remove IPs listed in remove_list
    for ip in remove_list:
        if ip in ip_addresses:
            ip_addresses.remove(ip)

    # Write the updated IPs back to the file
    with open(allow_file, 'w') as file:
        file.write('\n'.join(ip_addresses))

    # Re-read and return the updated list (for verification or printout)
    with open(allow_file, 'r') as file:
        return file.read()


# Example usage:
if __name__ == "__main__":
    allow_file = 'allow_list.txt'
    remove_list = ['192.168.1.100', '10.0.0.50']

    updated_ips = update_allow_list(allow_file, remove_list)
    print("Updated IP Allow List:\n", updated_ips)
