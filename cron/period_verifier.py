def verify_cron_period(period_spec: str) -> bool:
    def verify_minute(minute: str):
        pass

    periods_parts = filter(lambda a: a != '', period_spec.split(' '))

    if not verify_minute(periods_parts[0]):
        return False

    return True
