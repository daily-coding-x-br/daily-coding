def solution(bookings):
	start_dates, end_dates = [x[0] for x in bookings], [x[1] for x in bookings]
	sort(start_dates)
	sort(end_dates)
	maximum = 0
	current = 0
	start = 0
	end = 0
	while (start < len(start_dates)):
		if start_dates[start] < end_dates[end]:
			current += 1
			maximum = max(maximum, current)
			start += 1
		else:
			current -=1
			end += 1
	return maximum
