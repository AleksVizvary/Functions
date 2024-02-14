def search(group, item):

    group = str(group)
    places = []
    place = -1

    if group.find(item) != -1:
        for signs in group:
            place += 1
            if signs != item:
                pass
            else:
                places.append(place)

    if group.find(item) == -1:
        print('Item not found.')

    return places


def space(subject, sign):

    second_sign = f' {sign} '
    subject = subject.replace(sign, second_sign)

    return subject
