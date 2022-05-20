def get_count(string,ch):
    count = 0
    for item in string:
        if ch.upper() ==item or ch.lower()==item:
            count += 1
    return count


if __name__ == '__main__':
    s = 'adsdasdasfasfadfsdfgsd'
    ch = input('请输入要统计的字符串：')
    count = get_count(s, ch)
    print(count)