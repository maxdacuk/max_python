from period_verifier import verify_cron_period

for test_case in (

    # Test index | Test period spec | Expected Result
    (1, "* * * * *",     True,),
    (2, "*/2 * * * *",   True,),
    (3, "* 73 * * *",    False,),
    (4, "* * - * *",     False,),
    (5, "59 23 31 12 *", True,),
    (6, "0  23 * * 6",   True,),

):
    r_prefix = f'Test case {test_case[0]} :: "{test_case[1]}"'
    r_prefix += ' '*(15-len(test_case[1]))
    if verify_cron_period(test_case[1]) == test_case[2]:
        print(f'{r_prefix} - \\/ Passed')
    else:
        print(f'{r_prefix} - ! Failed')
