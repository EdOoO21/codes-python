import yarl
from aiohttp import web
import aiohttp


async def request_handler(request: web.Request) -> web.Response:
    """
    Проверяет, что запрос содержит корректный http(s) URL в параметрах:
    /fetch?url=http%3A%2F%2Fexample.com%2F
    Затем выполняет асинхронную загрузку указанного ресурса
    и возвращает его содержимое с кодом HTTP-статуса.
    Если URL не содержит схему (http или https) или
    является некорректным, возвращается ответ с кодом 400 (Bad Request).
    При ошибках запроса возвращается 502 (Bad Gateway).
    :param request: Объект запроса aiohttp.web.Request
    :return: Объект ответа aiohttp.web.Response
    """
    if "url" not in request.query.keys():
        response = aiohttp.web.Response(status=400, body=b"No url to fetch")
        return response

    url = yarl.URL(request.query["url"])

    if url.scheme == '':
        response = aiohttp.web.Response(status=400, body=b"Empty url scheme")
        return response

    if (url.scheme != 'http') and (url.scheme != 'https'):
        response = aiohttp.web.Response(
            status=400, body=f"Bad url scheme: {url.scheme}".encode())
        return response

    session = request.app['session']
    try:
        async with session.get(url) as ans:
            body = await ans.read()
            return web.Response(status=ans.status, body=body)
    except aiohttp.ClientError:
        return web.Response(status=502, body=b"Bad Gateway")


async def initialize_app(app: web.Application) -> None:
    """
    Настраивает hanler'ы для приложения
    и инициализирует aiohttp-сессию для выполнения запросов.
    :param app: app to apply settings with
    """
    app["session"] = aiohttp.ClientSession()
    app.router.add_get('/fetch', request_handler)
    return


async def close_app(app: web.Application) -> None:
    """
    Завершение приложения
    :param app: приложение которое должно завершиться!
    """
    await app["session"].close()
    return
