# pyramid_shopify_oauth

## in your .ini file, add the following
```
shopify.oauth.login_url = /oauth_login					    # The entry point of your shopify app, defaults to shopify_oauth_login_url (different from App Home)
shopify.oauth.redirect_url = /oauth_redirect        # The redirect app url for OAuth, defaults to shopify_oauth_redirect_url
shopify.oauth.scope = read_products,read_orders     # Permission scope you need from the shop
shopify.oauth.app_home = /												  # Your app home url
shopify.oauth.api_key = *************               # Your api key
shopify.oauth.secret = *************                # Your api secret
```

## in your app __init__ file, add the following
```
config.include('pyramid_shopify_oauth')
```
