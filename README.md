# pyramid_shopify_oauth

### in your .ini file, add the following
```
shopify.oauth.login_url = /oauth_login	            # The entry point of your shopify app, defaults to shopify_oauth_login_url (different from App Home)
shopify.oauth.redirect_url = /oauth_redirect        # The redirect app url for OAuth, defaults to shopify_oauth_redirect_url
shopify.oauth.scope = read_products,read_orders     # Permission scope you need from the shop (comma seperated)
shopify.oauth.app_home = /		            # Your app home url
shopify.oauth.api_key = *************               # Your api key
shopify.oauth.secret = *************                # Your api secret
```

### in your app __init__ file, add the following
```
config.include('pyramid_shopify_oauth')
```

### after oauth login, you can get shopify instance from request
```
shopify = request.shopify
if shopify is None:
  # the user is not signed in

# you can access shopify API now
shopify.Shop.current()
...
...
```

### To make oauth work, make sure you have pre-configured a session factory, for example
```
from pyramid_beaker import session_factory_from_settings

session_factory = session_factory_from_settings(settings)
config.set_session_factory(session_factory)
```
