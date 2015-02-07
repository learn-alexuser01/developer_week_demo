from cloudfs import Session

def get_filesystem():
	# application credentials 
	CLIENT_ID = 'JGSsOf2xYH08OOhqdEK_3A0hPfjzCU2Cv71ExHHiqYU'
	CLIENT_SECRET = 'RhOUcbdKKyejjcHQ8VFGiHMbRCZtqLtuXSnN1OX_U1NOqsCqb5a7JsRLSrdxoSGEahsN7izEo3i9TKdtUo6jHA'
	BASE_URL = 'developerweek.cloudfs.io'

	# user credentials
	TEST_USERNAME = 'demo'
	TEST_USER_PASSWORD = '111111'

	# Connect to application
	s = Session(BASE_URL,
	    CLIENT_ID,
	    CLIENT_SECRET
	    )

	# log into the demo user's account
	s.authenticate(TEST_USERNAME, TEST_USER_PASSWORD)

	# return users' filesystem
	return s.get_filesystem()