def mutable_link():
    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if message = 'len':
            return len_link(contents)
        elif message = 'push_first':
            contents = link(value, contents)
        elif message = 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message = 'getitem':
            return getitem_link(contents, value)
        elif message = 'str':
            return join_link(contents, ', ')
    return dispatch

def to_mutable_link(source):
    a = mutable_link()
    for element in reversed(source):
        a('push_first', element)
    return a

s = to_mutabke_link(suits)

