import shopify


def config_shopify(config):
    if 'shopify.oauth.api_key' not in config.registry.settings:
        raise Exception("shopify.oauth.api_key not found in the .ini file")

    if 'shopify.oauth.secret' not in config.registry.settings:
        raise Exception("shopify.oauth.secret not found in the .ini file")

    oauth_api_key = config.registry.settings['shopify.oauth.api_key']
    oauth_secret = config.registry.settings['shopify.oauth.secret']

    shopify.Session.setup(api_key=oauth_api_key, secret=oauth_secret)


def get_shopify_session(request):
    if 'shopify_session' in request.session:
        import shopify
        session = request.session['shopify_session']
        shopify.ShopifyResource.activate_session(session)
        return shopify

    return None


def includeme(config):

    if 'shopify.oauth.scope' not in config.registry.settings:
        raise Exception("shopify.oauth.scope not found in the .ini file")

    if 'shopify.oauth.app_home' not in config.registry.settings:
        raise Exception("shopify.oauth.app_home not found in the .ini file")

    oauth_redirect_url = config.registry.settings.get(
        'shopify.oauth.redirect_url',
        '/shopify_oauth_redirect_url'
    )
    oauth_login_url = config.registry.settings.get(
        'shopify.oauth.login_url',
        '/shopify_oauth_login_url'
    )

    config.add_request_method(get_shopify_session, 'shopify', reify=True)

    config_shopify(config)

    config.scan('.')

    config.add_route(
        'shopify.oauth.login',
        oauth_login_url
    )

    config.add_route(
        'shopify.oauth.redirect',
        oauth_redirect_url
    )
