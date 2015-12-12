import flickr_api

flickr_api.set_keys(api_key = '92d918b1eb42cc8936cfe03e9b705339', api_secret = '2481a8689941b019')
auth = flickr_api.auth.AuthHandler()
url = auth.get_authorization_url("delete")
print url
oauth_verifier = raw_input('oauth_verifier = ')
auth.set_verifier(oauth_verifier)
auth.save('oauth_verifier.txt')
