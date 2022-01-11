#Hackerrank - Fradulent Activity Notifications (Sorting)
def search_for_fradulent_activities(expenditures, d):
    notification_count = 0

    div = int(d/2)
    if d % 2 == 1:
        for i in range(d, len(expenditures) - 1):
            medianlist = sorted(expenditures[i-d : i])
            if expenditures[i] >= (medianlist[div] * 2):
                notification_count += 1
    else:
        for i in range(d, len(expenditures) - 1):
            medianlist = sorted(expenditures[i-d : i])
            med = (medianlist[div] + medianlist[div-1])/2
            if expenditures[i] >= (med * 2):
                notification_count += 1
    print(notification_count)


if __name__ == '__main__':
    expenditures = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 4
    search_for_fradulent_activities(expenditures, d)
