def validate_ip_address(queryIP):
    ipv4, ipv6 = False, False

    for i in range(len(queryIP)):
        if queryIP[i] == '.':
            ipv4 = True
            break

        if queryIP[i] == ':':
            ipv6 = True
            break

    i, seperator = 0, 0
    res = 'Neither'
    if ipv4:
        if queryIP[0] != '.' and queryIP[len(queryIP) - 1] != '.':
            for j in range(len(queryIP)):
                if queryIP[j] == '.' or j == len(queryIP) - 1:
                    seperator += 1
                    if seperator <= 4:
                        s = queryIP[i:j + 1 if j == len(queryIP) - 1 else j]
                        if (len(s) >= 2 and s[0] == '0') or len(s) <= 0 or int(s) < 0 or int(s) > 255:
                            return res
                        i = j + 1
                elif queryIP[j] != '.' and not('0' <= queryIP[j] <= '9'):
                    return res

            if seperator == 4:
                return 'IPv4'
    elif ipv6:
        if queryIP[0] != ':' or queryIP[len(queryIP) - 1] != ':':
            for j in range(len(queryIP)):
                if queryIP[j] == ':' or j == len(queryIP) - 1:
                    s = queryIP[i:j + 1 if j == len(queryIP) - 1 else j]
                    if len(s) <= 0 or len(s) > 4:
                        return res
                    i = j + 1
                    seperator += 1
                elif queryIP[j] != ':' and not queryIP[j].isalnum() or ('g' <= queryIP[j] <= 'z') or (
                        'G' <= queryIP[j] <= 'Z'):
                    return res

            if seperator == 8:
                return 'IPv6'

    return res


if __name__ == '__main__':
    ip1 = '172.6.254.255'
    ip2 = '2001:0db8:85a3:0:0:8A2E:0370:7334'
    ip3 = '256.256.256.256'
    ip4 = '2001:0db8:85a3::8A2E:037j:7334'
    ip5 = '02001:0db8:85a3:0000:0000:8a2e:0370:7334'
    ip6 = '1.1.1.1.'
    ip7 = '.1.1.1.1.'
    ip8 = '1.1.1.01'
    ip9 = '20EE:FGb8:85a3:0:0:8A2E:0370:7334'
    ip10 = '20EE:Fb8:85a3:0:0:8A2E:0370:7334:12'
    print(validate_ip_address(ip10))
