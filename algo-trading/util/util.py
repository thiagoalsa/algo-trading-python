def compra(ativo, quantidade, sl, tp):
    print('Compra efetuada')
    lot = float(quantidade)
    symbol = ativo
    price = mt5.symbol_info_tick(symbol).ask
    point = mt5.symbol_info(symbol).point
    deviation = 0

    request = {
        'action': mt5.TRADE_ACTION_DEAL,
        'symbol': symbol,
        'volume': lot,
        'type': mt5.ORDER_TYPE_BUY,
        'price': price,
        'sl': sl,
        'tp': tp,
        'deviation': deviation,
        'magic': 12345678,
        'comment': 'Ordem de compra enviada',
        'type_time': mt5.ORDER_TIME_GTC,
        'type_filling': mt5.ORDER_FILLING_RETURN
    }

    resultado = mt5.order_send(request)
    return resultado


def venda(ativo, quantidade, sl, tp):
    print('Venda efetuada')
    lot = float(quantidade)
    symbol = ativo
    price = mt5.symbol_info_tick(symbol).bid
    point = mt5.symbol_info(symbol).point
    deviation = 0

    request = {
        'action': mt5.TRADE_ACTION_DEAL,
        'symbol': symbol,
        'volume': lot,
        'type': mt5.ORDER_TYPE_SELL,
        'price': price,
        'sl': sl,
        'tp': tp,
        'deviation': deviation,
        'magic': 12345678,
        'comment': 'Ordem de venda enviada',
        'type_time': mt5.ORDER_TIME_GTC,
        'type_filling': mt5.ORDER_FILLING_RETURN
    }

    resultado = mt5.order_send(request)
    return resultado
