import shopify
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


@view_config(
    route_name='shopify.oauth.login',
    request_method='GET',
    renderer='json'
)
def login_view(request):
    if 'shop' not in request.GET:
        return {
            'error': 'Shop name is not specified'
        }

    shop = request.GET['shop']
    scope = request.registry.settings['shopify.oauth.scope'].split(",")

    session = shopify.Session(shop)
    oauth_redirect_url = request.route_url('shopify.oauth.redirect')

    permission_url = session.create_permission_url(scope, oauth_redirect_url)

    return HTTPFound(location=permission_url)


@view_config(
    route_name='shopify.oauth.redirect',
    request_method='GET',
    renderer='json'
)
def redirect_view(request):
    params = dict(request.GET)

    if set(params.keys()) != set(['code', 'hmac', 'timestamp', 'shop']):
        return {
            'error': 'URL format is wrong'
        }

    shop = params['shop']

    session = shopify.Session(shop)
    session.request_token(params)

    shopify.ShopifyResource.activate_session(session)

    home_url = request.registry.settings['shopify.oauth.app_home']
    request.session['shopify_session'] = session

    return HTTPFound(location=home_url)
