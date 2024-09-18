def verify_cron_period(period_spec: str) -> bool:
    def verify_minute(minute: str):
        pass

    periods_parts = filter(lambda a: a != '', period_spec.split(' '))

    if not verify_minute(periods_parts[0]):
        return False

    chunk = '5,8,9'
    amin = 0
    amax = 23
    comma_chunks = chunk.split(',')
    if all(c.isdigit() and amin <= int(c) <= amax for c in comma_chunks):
        return True


    for c in comma_chunks:
        if not (c.isdigit() and amin <= int(c) <= amax):
            return False
    return True



    return True

